# React-Native技术详解：通信机制详解

## 一、JS解析引擎

React Native用**iOS自带的JavaScriptCore作为JS的解析引擎**，但并没有用到JavaScriptCore提供的一些可以让JS与OC互调的特性，而是自己实现了一套机制。  
这套机制可以**通用于所有JS引擎上**，在没有JavaScriptCore的情况下也可以用webview代替，例如可以用webview直接解析rn文件，目的之一就是为了iOS7之前没有JavaScriptCore的系统。

### 例子：JS如何调用OC方法

有一个OC类OCManager，其中有方法query:successCallback:
```
@implement OCManager
- (void)query:(NSString *)queryData successCallback:(RCTResponseSenderBlOCk)responseSender
{
     RCT_EXPORT();
     NSString *ret = @"ret"
     responseSender(ret);
}
@end
```
则JS可以直接调用OCManager.query，并通过回调获取方法的执行结果：
```
OCManager.query("SELECT * FROM table", function(result) {
     //result == "ret";
});
```
## 二、模块配置表

### 1.什么是模块配置表？
从上面的例子思考，JS是如何知道OC有某个方法的呢？这里就要引入一个概念——“**模块配置表**”。  
模块配置表里包含：
- 模块ID（ModuleId）
- 方法ID（MethodId）
- 参数和参数类型（Arguments）
  
当 Objective-C 接收到这三个值后，就可以通过 runtime 唯一确定要调用的是哪个函数，然后调用这个函数。

### 2.bridge

**OC端和JS端分别各有一个bridge**，两个bridge都保存了同样一份模块配置表，JS调用OC模块方法时，通过bridge里的配置表把模块方法转为模块ID和方法ID传给OC，OC通过bridge的模块配置表找到对应的方法执行。

### 3.模块配置表的生成

我们在新建一个OC模块时，JS和OC都不需要为新的模块手动去某个地方添加一些配置，**模块配置表是自动生成的**，只要项目里有一个模块，就会把这个模块加到配置表上，那这个模块配置表是怎样自动生成的呢？  
分以下两个步骤：

#### 3.1 取所有模块的类
每个模块类都实现了RCTBridgeModule接口，所以只要通过runtime的任意一个方法：
- objc_getClassList
- objc_copyClassList
  
获取项目里所有的类，然后判断是否实现了RCTBridgeModule接口，就得到了所有的模块类。

#### 3.2 取模块里暴露给JS的方法
JavaScript 是一种单线程的语言，它不具备自运行的能力，因此总是被动调用，Objective-C 创建了一个单独的线程，这个线程只用于执行 JavaScript 代码，而且 JavaScript 代码只会在这个线程中执行。

