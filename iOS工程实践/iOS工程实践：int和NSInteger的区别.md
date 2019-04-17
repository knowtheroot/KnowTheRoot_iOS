# int和NSInteger有什么区别？
## 首先：
在c语言中，int和long的字节数是和操作系统指针所占位数相等；

但c语言中说，long的长度永远大于或等于int；

objective-c里，苹果的官方文档中总是推荐用NSInteger；

## 区别：
原来在苹果的api实现中，**NSInteger是一个封装**，它会识别当前操作系统的位数，自动返回最大的类型。

## 总结：
NSInteger与int的区别是NSInteger**会根据系统的位数（32or64）自动选择int的最大数值（int or long）**还有就是他和NSString一样都可以是对象。
