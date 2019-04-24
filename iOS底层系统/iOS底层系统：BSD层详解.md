# iOS底层系统：BSD层详解

## 一、前言

#### 什么是BSD层？

BSD层是建立在Mach之上，是XUN中一个不可分割的一部分。BSD负责提供可靠的、现代的API。其内容包括：
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

