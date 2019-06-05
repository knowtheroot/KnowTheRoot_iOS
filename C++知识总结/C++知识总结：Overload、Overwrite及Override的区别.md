# C++知识总结：Overload、Overwrite及Override的区别

## 一、Overload
C语言不允许两个函数出现重名的情况，而一个认真的开发者会花一定的时间来设计每个函数的名称，这对开发者来说是一个不小的负担。  
C++通过重载来避免了这一类的麻烦。

### 1.定义
Overload，既**重载**。  
在C++中，可以将语义、功能相似的几个函数用同一个名字来表示。但函数的参数或者返回值不同（包括类型、顺序不同），则称为重载。  
例如我们定义了重载函数test：
```
int test(int a);
int test(int a, FILE *f)
int test(char const *s)
int test(char const *s, FILE *f)
```

### 2.Overload的特点

- 函数在相同的范围，既同一个类中。
- 函数的名字相同。
- 参数不同，包括类型、顺序。
- virtual关键字可有可无。

### 3.Overload的底层实现


### 4.iOS中的Overload
