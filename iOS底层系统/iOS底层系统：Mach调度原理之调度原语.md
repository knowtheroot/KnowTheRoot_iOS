# iOS底层系统：Mach调度原理之调度原语

- **线程**：和所有的现代操作系统一样，Mach内核调度的对象是线程。  
- **任务**：Mach中使用一个比进程更轻量级的概念：任务（task）。
  
最基本的单位是线程，一个任务包含一个或多个线程。

## 一、线程

### 1.什么是线程

#### 线程的定义
线程（thread）定义了match中最小的执行单元。  
#### 线程的含义
线程表示的是**底层的机器寄存器状态以及各种调度统计数据**。
#### 线程的设计
线程从设计上提供了调度所需要的大量信息，同时尽可能地维持最小开销。

#### 线程的实现

这里以简化的代码为例子：
```
struct thread {
    /* 频繁读，但很少修改的字段 */
    queue_chain_t links;        /* 运行队列/等待队列的链表连接 */
    wait_queue_t wait_queue;        /* 所在的等待队列 */
    
    ...
    ...
    
    /* thread_invoke中更新/使用的数据 */
    vm_offset_t kernel_stack        /* 当前的内核栈 */
    vm_offset_t reserved_stack      /* 预留的内核栈 */
    
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
    
}
```
