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

输入代码：
```
NSMutableString *mutableStr1 = [[NSMutableString alloc] initWithString:@"123"];
NSMutableString *mutableStr2 = [[NSMutableString alloc] initWithString:@"123"];
NSLog(@"mutableStr1 address = %p", mutableStr1);
NSLog(@"mutableStr2 address = %p", mutableStr2);
```
输出结果：
```
mutableStr1 address = 0x600001b4e100
mutableStr2 address = 0x600001b4e400
```
可以看出，mutableStr1和mutableStr2虽然内容相同，但是**指向的内存地址是不同**的。   
**若当NSMutableString改变内容后，指向的依然是自己的内存地址**。

## 三、总结
#### 1.浅拷贝
指针拷贝，指针地址不变，没有创建新的对象。
#### 2.深拷贝
内容拷贝，指针地址改变，创建了新的对象。

#### 3.对于NSString和NSMutbleString

- 对一个NSString字符串进行copy操作不会产生新的对象（浅拷贝）
- 对一个NSMutableString字符串进行copy操作会产生一个新的对象（深拷贝）
- copy产生的新对象为NSString类型
- mutableCopy产生的新对象为NSMutableString类型
- NSMutaleString之所以能改变大小是因为在堆内存上
NSString的调方法增加字符串，会先拿到原理的字符串，然后复制一份，再在新复制的那个对象上进行修改，
**实质返回的是一个新对象**，原来的字符串并没有变化。  
NSMutableString修改字符串，就是在原来的字符串上进行修改的，**操作的是同一个对象**
所有称NSString是不可变的，NSMutableString时可变的。

#### 4.拓展问题

**copy只能复制不可变对象。**  
**1.用@property声明的NSString（或NSArray，NSDictionary）经常使用copy关键字，为什么？如果改用strong关键字，可能造成什么问题？**
- 因为<u>父类指针可以指向子类对象</u>,使用 copy 的目的是为了让本对象的属性不受外界影响,使用 copy 无论给我传入是一个可变对象还是不可对象,我**本身持有的就是一个不可变的副本**。
- 如果我们使用是 strong ,那么这个属性就有可能指向一个可变对象,**如果这个可变对象在外部被修改了,那么会影响该属性**。

**2.如何自己实现拷贝操作？**
- 若想令自己所写的对象具有拷贝功能，则需**实现 NSCopying 协议**。
- 如果自定义的对象分为可变版本与不可变版本，那么就要**同时实现 NSCopying 与 NSMutableCopying 协议**。
注意：NSCopying协议只有一个方法：
```
- (id)copyWithZone:(NSZone *)zone;
```
**3.集合类对象的copy与mutableCopy**  
集合类对象是指 NSArray、NSDictionary、NSSet ... 之类的对象。
- 在非集合类对象中：对 immutable 对象进行 copy 操作，是指针复制，mutableCopy 操作时内容复制；对 mutable 对象进行 copy 和 mutableCopy 都是内容复制。
- 在集合类对象中：对 immutable 对象进行 copy，是指针复制， mutableCopy 是内容复制；对 mutable 对象进行 copy 和 mutableCopy 都是内容复制。

总结：  
##### 可变都是深拷贝，不可变的copy是浅拷贝，mutablecopy是深拷贝。
