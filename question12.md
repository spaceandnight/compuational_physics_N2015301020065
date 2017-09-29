# 第四次作业
## 选做课后习题1.2
* Queation:The position of an object moving horizontally with a constant velocity, v, is described by the equation:
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dx}{dt}=v" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=v" title="\frac{dx}{dt}=v" /></a> (1.9)
Assuming that the velocity is a constant, say v=40m/s, use the Euler method to solve (1.9) for x as a function of time. Compare your result with the exact solution.
* 假设当t=0时x=0，运用欧拉方法求常微分方程（1.9）的近似解，x(n+1)-x(n)=vh，v=40m/s是常量，h为时间间隔，取h=1s，求出相应的x(1)~x(10)的值，并且绘制出x-t曲线。曲线如下图所示。
![question12](https://github.com/spaceandnight/compuational_physics_N2015301020065/blob/master/QQ%E6%88%AA%E5%9B%BE20170929190333.png)
* 实际上常微分方程（1.9）的解为x=vt+c，c为任意常数。若当t=0时x=0，则实际解与求得的近似解完全重合。因为欧拉方法是用直线段来逼近曲线的近似求解方法，而该常微分方程的解就是一条直线，所以近似解与实际解之间不存在误差
* 源代码材料：[material_04](https://github.com/spaceandnight/compuational_physics_N2015301020065/blob/master/question12.py)
