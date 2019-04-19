# 贝塞尔曲线

## 一、什么是贝塞尔曲线

定义：贝塞尔曲线所依据的数学公式，是早在1912年就广为人知的**伯恩斯坦多项式**。

#### 伯恩斯坦斯的逼近性质
在[ a, b ] 区间上**所有的连续函数都可以用多项式来逼近**，并且收敛性很强，也就是一致收敛。  
再简单点，就是一个连续函数，你可以将它写成若干个伯恩斯坦多项式相加的形式，并且，随着 n→∞，这个多项式将一致收敛到原函数，这个就是伯恩斯坦斯的逼近性质。

## 二、贝塞尔曲线的绘制原理

在平面内选3个不同线的点并且依次用线段连接。  
![avatar](https://github.com/knowtheroot/KnowTheRoot_iOS/blob/master/Resources/Imgs/BezierPath01.png)  
在AB和BC线段上找出点D和点E，使得AD/AB = BE/BC。  
![avatar](https://github.com/knowtheroot/KnowTheRoot_iOS/blob/master/Resources/Imgs/BezierPath02.png)  
连接DE，并在DE上找出一点F，使得DF/DE = AD/AB = BE/BC。  
![avatar](https://github.com/knowtheroot/KnowTheRoot_iOS/blob/master/Resources/Imgs/BezierPath03.png)  
让选取的点D在第一条线段上从起点A，移动到终点B，找出所有点F，并将它们连起来。  
此时得到的线段就是绘制得结果：  
![avatar](https://github.com/knowtheroot/KnowTheRoot_iOS/blob/master/Resources/Imgs/BezierPath04.png)  

## 三、贝塞尔曲线有什么用？

由于贝塞尔曲线控制简便，而且具有很强的描述能力，因此它在工业设计上已经被广泛使用了。  
在**计算机图形学**领域（特别是矢量图形学），贝塞尔曲线也有着举足轻重的地位。

## 四、如何用贝塞尔曲线

首先，要明确的一点是，对于贝塞尔曲线来说，最重要的点是，数据点和控制点。
- **数据点**：指一条路径的起始点和终止点。
- **控制点**：控制点决定了一条路径的弯曲轨迹
  
根据控制点的个数，贝塞尔曲线被分为一阶贝塞尔曲线（0个控制点）、二阶贝塞尔曲线（1个控制点）、三阶贝塞尔曲线（2个控制点）等等。  
系统给我们提供了一个叫做UIBezierPath类，用它可以画简单的圆形，椭圆，矩形，圆角矩形，也可以通过添加点去生成任意的图形，还可以简单的创建一条二阶贝塞尔曲线和三阶贝塞尔曲线。
