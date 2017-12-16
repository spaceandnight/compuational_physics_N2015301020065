import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib import animation
delta_x=0.01
c=300
delta_t=delta_x/c
r=1
x=np.linspace(0,1,int(1/delta_x)+1)
def next_step(y_previous,y_current):
    y_next=[0]
    c1,c2=2*(1-r**2),r**2
    for i in range(1,len(y_current)-1):
        y_next.append(c1*y_current[i]-y_previous[i]+c2*(y_current[i-1]+y_current[i+1]))
    y_next.append(0)
    return y_next
def after_n_step(y0,y1,n):
    for i in range(n):
        y2=next_step(y0,y1)
        y0,y1=y1,y2
    return y0,y1
k0,x0=300,0.6
k1,x1=300,0.6
y_initial=[]
for i in range(1+int(1/delta_x)):
    y_initial.append(math.exp(-k0*(i*delta_x-x0)**2)-2*math.exp(-k1*(i*delta_x-x1)**2))  
fig = plt.figure() 
ax = plt.axes(xlim=(0, 1), ylim=(-2.01,2.01))
line, = ax.plot([], [], lw=1.)  
plt.title('Two Wavepackets On A String With Fixed Ends')
plt.xlabel('x')
plt.ylabel('y')
def init():  
    line.set_data([], []) 
    return line
def animate(j):
    y0,y1=after_n_step(y_initial,y_initial,j)
    line.set_data(x, y1)
    return line
anim1=animation.FuncAnimation(fig, animate, init_func=init, frames=201, interval=50)
plt.show()  