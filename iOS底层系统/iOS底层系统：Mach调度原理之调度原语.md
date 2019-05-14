# iOS底层系统：Mach调度原理之调度原语

- **线程**：和所有的现代操作系统一样，Mach内核调度的对象是线程。  
- **任务**：Mach中使用一个比进程更轻量级的概念：任务（task）。
  
最基本的单位是线程，一个任务包含一个或多个线程。

## 一、线程（thread）

### 1.什么是线程

#### 线程的定义
线程（thread）定义了match中最小的执行单元。  
#### 线程的含义
线程表示的是**底层的机器寄存器状态以及各种调度统计数据**。
#### 线程的设计
线程从设计上提供了调度所需要的大量信息，同时尽可能地维持最小开销。

### 2.线程的实现

这里以简化的代码为例子：
```
struct thread {
    /* 频繁读，但很少修改的字段 */
    queue_chain_t links;        /* 运行队列/等待队列的链表连接 */
    wait_queue_t wait_queue;        /* 所在的等待队列 */
    
    ...
    ...
    
    /* thread_invoke中更新/使用的数据 */
    vm_offset_t kernel_stack;        /* 当前的内核栈 */
    vm_offset_t reserved_stack;      /* 预留的内核栈 */
    
    ...
    ...
    
    /*
     * 线程状态位
    */
    #define TH_WAIT         0x01        /* 在队列中等待 */
    #define TH_SUSP         0x02        /* 停止，或请求停止 */
    #define TH_RUN          0x04        /* 正在运行或在运行队列中 */
    #define TH_UNINT        0x08        /* 在不可中断的等待 */
    #define TH_TERMINATE    0x10        /* 终止时同时运行 */
    #define TH_TERMINATE2   0x20        /* 添加到终止队列 */
    #define TH_IDLE         0x80        /* 空闲线程 */
    
    ...
    ...
    
    /* 调度信息 */
    sched_mode_t sched_mode;     /* 调度模式 */
    sched_mode_t saved_mode;     /* 在被迫模式降级时保存的模式 */
    
    ...
    ...
    
    /* 调度相关的状态位 */
    integer_t sched_pri;     /* 当前调度的优先级 */
    integer_t priority;      /* 基础优先级 */
    integer_t importance ;   /* 任务相关的重要性 */
    
    ...
    ...
    
    /* 定时相关的数据结构 */
    timer_data_t user_timer;     /* 用户定时器 */
    
    ...
    ...
}
```

#### 线程模板thread_template

可以发现，thread的数据结构是非常巨大的，因此大部分创建线程的时候都是**从一个通用的模板复制而来**，这个模板使用默认值填充这个数据结构。这个模板名为thread_template。  
内核引导的过程中，调用thread_bootstrap()方法负责填充这个模板。  
thread_create_internal()函数会分配新的线程数据结构。  
Mach API的**thread_create() 就是通过thread_create_internal()实现的**。

#### 线程的容器

**Mach将任务定义为线程的容器**。  
资源是在任务这个层次处理的，线程只能**通过端口访问包含这个线程的任务中分配的资源和内存**。

## 二、任务（task）

### 1.任务的定义
任务（task）是一种容器对象。虚拟内存空间和其他资源都是通过这个容器对象管理的。  
资源被进一步抽象为端口。  
因此资源的共享实际上相当于允许对对应端口进行访问。
> 每一个BSD进程（也就是OS X进程）都在底层关联了一个Mach任务对象。

相对于线程，任务是一个比较轻量级的数据结构：
```
struct task {
    /* 同步相关的信息 */
    unit_32_t ref_count;     /* 引用计数 */
    boolean_t active;        /* 任务还没有终止 */
    boolean_t halting;       /* 任务被停止 */
    
    ...
    ...
    
    /* 杂项 */
    vm_map_t map;       /* 地址空间映射 */
    
    ...
    ...
    
    /* 任务中的线程 */
    queue_head_t threads;            /* 用FIFO队列保存线程 */
    int thread_count;                /* 线程队列中的线程数 */
    unit32_t active_thread_count;    /* 活动的线程数 */
    
    integer_t priority;      /* 线程基础优先级 */
    integer_t max_priority;  /* 线程的最高优先级 */
    
    ...
    ...
    
    //每个任务都有自己私有的端口名称空间
    struck ipc_space *itk_space;
    
    ...
    ...
    
    #ifdef MACH_BSD
        void *bsd_info;     //指向BSD进程对象
    #endif
}
```
### 2.任务存在的目的

就本身而言，任务是没有生命的。**任务存在的目的就是要成为一个或多个线程的容器**。  
任务中的线程都在threads成员中维护，这是一个包含thread_count个线程的队列。

### 3.任务的操作

**大部分针对任务的操作实际上就是遍历给定任务中的所有线程，并对这些线程进行对应的线程操作**。

### 4.账本

#### 定义

账本（ledger）是Mach任务的配额记账和设置限制所需要的机制。  
资源（一般指CPU资源和内存资源）可以在账本间转移。

## 三、任务和线程相关的API

### 1.获取当前的任务和线程

在任何时刻，内核都必须能够获得当前任务和当前线程的句柄。  
内核分别通过：
- current_task()
- current_thread()
  
两个函数来完成。

### 2.函数内部实现

以上两个函数都是对“fast”版本的函数调用的宏。既：  
- current_task()调用current_task_fast()
- current_thread()调用current_thread_fast()

## 四、任务相关的API

Mach提供了完整的一套用于操作任务的API。  
这里列举几个接口：
| Mach任务相关API | 用途 |
| ------ | ------ |
| mach_task_self() | 获取任务端口，带有发送权限的名称 |
| task_create(task_t target_task, ledger_array_t ledgers, mach_msg_type_number_t boolean_t task_t *child_task) | 以target_task为父任务创建一个child_task。 |

## 五、线程相关的API

类似任务相关的API，Mach还提供了丰富的线程管理API。这些API大部分都和任务API的功能类似。  
实际上，任务API通常的实现方法就是**遍历任务中的线程列表，然后对每个线程执行对应的操作**。  
这些调用大部分都是通过Mach消息实现的。
