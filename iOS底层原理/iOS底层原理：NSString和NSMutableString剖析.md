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
以不同的方式创建NSString：
```
NSString *str1 = @"123";
NSLog(@"address = %p",str1);
NSString *str2 = [NSString stringWithFormat:@"123"];
NSLog(@"address = %p",str2);
```
得到不同的字符串对象：
![avatar](https://github.com/knowtheroot/KnowTheRoot_iOS/blob/master/Resources/Imgs/NSStringAndNSMutableString01.png?raw=true)
可以发现，两种声明方式的isa是不同的。  
- 以@""方式声明的字符串是_NSCFConstantString，内存地址一样
- 以stringWithFormat方法声明的字符串是NSCFString，在堆上分配内存

## 二、深拷贝和浅拷贝
### 1.copy和mutableCopy
先做个小测试：
```
NSString *str1 = @"test";
NSString *str2 = [str1 copy];
NSString *str3 = [str1 mutableCopy];
NSLog(@"str1 address = %p", str1);
NSLog(@"str2 address = %p", str2);
NSLog(@"str3 address = %p", str3);
```
输出结果：
```
str1 address = 0x10dd72068
str2 address = 0x10dd72068
str3 address = 0x6000005faac0
```
可以看到：
- **copy操作为浅拷贝**，两个指针指向的是同一个内存地址
- **mutableCopy为深拷贝**，指向的是两个不同的内存地址
#### 原因：
**mutableCopy操作是将对象拷贝到堆上，引用计数加1。**

### 2.NSString和NSMutableString的拷贝

#### 2.1 NSString的拷贝
输入代码：
```
NSString *str1 = @"123";
NSString *str2 = @"123";
NSLog(@"str1 address = %p", str1);
NSLog(@"str2 address = %p", str2);
```
打印输出：
```
str1 address = 0x10aed3068
str2 address = 0x10aed3068
```
发现str1和str2都是_NSCFConstantString，既@"123"存储在文字常量区，**指针str1和str2都指向同一个内存地址**。  
若当str1改变内容后，就创建了新的对象，则str1指向另一块内存地址，换言之，如果此时将str1置为nil，也完全不影响str2，所以得出结论：**NSString为浅拷贝**。

#### 2.2 NSMutableString的拷贝

