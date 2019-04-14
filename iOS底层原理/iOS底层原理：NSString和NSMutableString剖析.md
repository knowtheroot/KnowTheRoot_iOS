# NSString和NSMutableString剖析

## 一、NSString
### 1.NSSting头文件解析
```
NSString : NSObject
//实现协议：
NSCopying/NSMutableCopying/NSSecureCoding
//类别：
//扩展类别
NSString (NSStringExtensionMethods)
//此API是用来检测给定原始数据的字符串编码
NSString (NSStringEncodingDetection)
```
NSString继承自NSObject。

### 2.NSString的C底层实现
