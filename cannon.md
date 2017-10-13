# 第五次作业
## 选做课后习题2.8
### question: In our model of the cannon shell trajectory we have assumed that the acceleration due to gravity, *g*, is a constant. It will, of course, depend on altitude. Add this to the model and calculate how much it affects the range.
* 在模拟大炮射击时，取初速度*v=700.0m/s*，地球表面的重力加速度*g=9.8m/s<sup>2</sup>*，地球半径*R=6371km*,重力加速度随海拔高度*y*变化公式如下：
* <a href="http://www.codecogs.com/eqnedit.php?latex=g(y)=g\left&space;(&space;\frac{R}{R&plus;y}&space;\right&space;)^{2}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?g(y)=g\left&space;(&space;\frac{R}{R&plus;y}&space;\right&space;)^{2}" title="g(y)=g\left ( \frac{R}{R+y} \right )^{2}" /></a> 
* 引入微分方程，并用欧拉方法计算
* <a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dx}{dt}=v_{x}\rightarrow&space;x_{i&plus;1}=x_{i}&plus;v_{x,i}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=v_{x}\rightarrow&space;x_{i&plus;1}=x_{i}&plus;v_{x,i}\Delta&space;t" title="\frac{dx}{dt}=v_{x}\rightarrow x_{i+1}=x_{i}+v_{x,i}\Delta t" /></a>
* <a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dv_{x}}{dt}=0\rightarrow&space;v_{x,i&plus;1}=v_{x,i}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dv_{x}}{dt}=0\rightarrow&space;v_{x,i&plus;1}=v_{x,i}" title="\frac{dv_{x}}{dt}=0\rightarrow v_{x,i+1}=v_{x,i}" /></a>
* <a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dy}{dt}=v_{y}\rightarrow&space;y_{i&plus;1}=y_{i}&plus;v_{y,i}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dy}{dt}=v_{y}\rightarrow&space;y_{i&plus;1}=y_{i}&plus;v_{y,i}\Delta&space;t" title="\frac{dy}{dt}=v_{y}\rightarrow y_{i+1}=y_{i}+v_{y,i}\Delta t" /></a>
* <a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dv_{y}}{dt}=-g\rightarrow&space;v_{y,i&plus;1}=v_{y,i}-g\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dv_{y}}{dt}=-g\rightarrow&space;v_{y,i&plus;1}=v_{y,i}-g\Delta&space;t" title="\frac{dv_{y}}{dt}=-g\rightarrow v_{y,i+1}=v_{y,i}-g\Delta t" /></a>
### 绘制曲线
* 取不同的发射角度，绘制大炮炮弹曲线，比较重力加速度为常数和重力加速度随海拔高度变化两种情况下对大炮炮弹轨迹的影响

## 尝试使用pygame做一个游戏
