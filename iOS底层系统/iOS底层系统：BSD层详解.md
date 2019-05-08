# iOS底层系统：BSD层详解

## 一、前言

#### 什么是BSD层？

BSD层是建立在Mach之上，是XNU中一个不可分割的一部分。BSD负责提供可靠的、现代的API。其内容包括：
- UNIX进程模型
- POSIX线程模型及相关的同步原语
- UNIX用户和组
- 网络协议栈
- 文件访问系统
- 设备访问

## 二、BSD的相关特性

尽管XUN的绝对核心是Mach，但是**XUN向用户态提供的主要接口是BSD接口**。

### 1.sysctl

sysctl命令用于运行时配置内核参数，这些参数位于/proc/sys目录下。  
在openBSD的描述为：  
> The sysctl utility retrieves kernel state and allows processes with appropriate privilege to set kernel state. The state to be retrieved or set is described using a “Management Information Base” (MIB) style name, using a dotted set of components.  

sysctl(8)命令算得上是一种访问内核内部状态的标准方法。  
#### 作用
通过使用这条命令，系统管理员可以**直接查询内核变量的值，获得重要的运行时诊断信息**。  
ps:只有非常少量的变量会通过这种方式导出。  
内核组件可以在运行时注册额外的sysctl变量值，甚至增加整个名称空间。

### 2.kqueue

#### 定义：
kqueue是BSD中使用的**内核事件通知机制。**

#### 功能：
一个kqueue指的是一个描述符，这个描述符会**阻塞等待直到一个特定的类型和种类的事件发生**。

#### 作用：

用户态或者内核的进程可以等待这个描述符，因而**kqueue提供了一种用于一个或多个<u>进程同步</u>的简单且高效的方法**。    

**kqueue和kevent（表示事件的数据结构）构成了内核异步I/O的基础。**

### 3.审计（OS X）

OS X实现了最基本的安全模块BSM。  
审计子系统对OS X的价值是最大的，而对iOS意义不大，因为**iOS没有启用审计**。  
ps：由于审计是一个和安全密切相关的操作，因此必须在内核层面执行。

### 4.强制访问控制（MAC）

MAC：既Mandatory Access Control，强制访问控制。

#### 关键概念

MAC中的关键概念是标签（label），标签指的是一个预定义的分类，系统中的文件集合或其他对象都可以应用这个标签分类。
> 可以想象谍战片中给文件打上“机密”、“最高机密”等标签

#### 匹配标签

如果请求访问的对象没有提供匹配的标签，那么MAC就会拒绝访问请求。  
每一个系统调用首先必须通过MAC的验证，然后才能真正处理来自用户态的请求。

#### 用途

MAC是OS X的隔离机制既“沙盒机制”的基础。
