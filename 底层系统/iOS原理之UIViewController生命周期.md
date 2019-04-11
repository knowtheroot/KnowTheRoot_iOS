# UIViewController生命周期

## 一、什么是生命周期

在Object-C中，一个对象的生命周期指这个对象**从创建到销毁的运行时（runtime）生命**。

一个对象的出现有以下两个途径：
- 当程序显示的创建并初始化它的时候
- 当对象作为另外一个对象的副本的时候

## 二、UIViewController的加载方式

苹果为开发者提供了<font color=#DC143C>4种</font>默认的加载方式：
- 通过Xib加载
- 通过StoryBoard加载
- 通过NSCoding协议加载
- 通过纯代码加载

### 1.通过Xib加载

