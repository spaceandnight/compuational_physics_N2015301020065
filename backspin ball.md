# 第六次作业
* 物理基地班一班  王裕民  2015301020065
## 选做课后习题2.18
### Question：Calculate the effect of backspin on a fastball. How much does an angular velocity of 1000 rpm (typical for a fastball) affect the trajectory?
* 在计算下旋对于快球的影响时, 取棒球的初速度为*v=110mph(49m/s)*,转速为*1000*,  投出角度为*a=30<sup>o</sup>*, 则水平速度为*v<sub>x</sub>=95mph(42.5m/s)*, 分别绘制无旋球和下旋球的轨迹曲线.
* 引入微分方程，并用欧拉方法计算.
* <a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dx}{dt}=v_{x}\rightarrow&space;x_{i&plus;1}=x_{i}&plus;v_{x,i}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dx}{dt}=v_{x}\rightarrow&space;x_{i&plus;1}=x_{i}&plus;v_{x,i}\Delta&space;t" title="\frac{dx}{dt}=v_{x}\rightarrow x_{i+1}=x_{i}+v_{x,i}\Delta t" /></a>
* <a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dv_{x}}{dt}=-\frac{B_{2}}{m}vv_{x}-\frac{S_{0}}{m}v_{y}w\rightarrow&space;v_{x,i&plus;1}=v_{x,i}-\frac{B_{2}}{m}v_{i}v_{x,i}\Delta&space;t-\frac{S_{0}}{m}v_{y,i}w\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dv_{x}}{dt}=-\frac{B_{2}}{m}vv_{x}-\frac{S_{0}}{m}v_{y}w\rightarrow&space;v_{x,i&plus;1}=v_{x,i}-\frac{B_{2}}{m}v_{i}v_{x,i}\Delta&space;t-\frac{S_{0}}{m}v_{y,i}w\Delta&space;t" title="\frac{dv_{x}}{dt}=-\frac{B_{2}}{m}vv_{x}-\frac{S_{0}}{m}v_{y}w\rightarrow v_{x,i+1}=v_{x,i}-\frac{B_{2}}{m}v_{i}v_{x,i}\Delta t-\frac{S_{0}}{m}v_{y,i}w\Delta t" /></a>
* <a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dy}{dt}=v_{y}\rightarrow&space;y_{i&plus;1}=y_{i}&plus;v_{y,i}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dy}{dt}=v_{y}\rightarrow&space;y_{i&plus;1}=y_{i}&plus;v_{y,i}\Delta&space;t" title="\frac{dy}{dt}=v_{y}\rightarrow y_{i+1}=y_{i}+v_{y,i}\Delta t" /></a>

* 其中*B<sub>2</sub>/m*和*S<sub>0</sub>/m*的值由下式给出.
### 绘制曲线
* 将无旋球和下旋球的轨迹曲线放在一起进行比较， 分析下旋对棒球轨迹的影响.
* ![back](https://github.com/spaceandnight/compuational_physics_N2015301020065/blob/master/backspin.png)
* 显然下旋球轨迹比无旋球轨迹更高一些，落地点也更远一些，两条轨迹的区别在曲线的下落段最明显.
### 结论
* 在两种轨迹比较图图中我们可以看到虽然两种球轨迹有明显区别，但是两者的整体轨迹相差不大.
* 查询资料可知: 快球最容易掷出，因为马格努斯效应对它的影响非常小. 四缝线快球是投手们最经常投出的球.投球时，投手们会非常自然地加入一个后旋.后旋使马格努斯力向上，球的落地速度将慢于其他投掷方法，使人产生一种球在上升的错觉. 其他快球，比如二缝线快球和切球，都是投出的旋转球，但因为球的移动速度非常快，马格努斯效应不会大幅改变其位置.(摘自搜狐@棒球PIE)
* 因此，结论是: 下旋不会大幅改变球的轨迹，但是会使球的落地速度将慢于其他投掷方法，使人产生一种球在上升的错觉.
源材料代码
* [material_06](https://github.com/spaceandnight/compuational_physics_N2015301020065/blob/master/backspin_ball.py)
