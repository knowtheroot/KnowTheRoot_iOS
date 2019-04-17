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

