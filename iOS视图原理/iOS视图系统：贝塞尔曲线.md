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
