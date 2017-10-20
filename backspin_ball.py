import matplotlib.pyplot as plt
import numpy as np
import math
list1 = [0]
list2 = [0]
list3 = [0]
list4 = [0]
v = 49.0
g = 9.8
a = 30.0
s = 0.00041
w = 1000 * 3.1416 / 60
dt = 0.01
plt.figure(figsize=(8,6))
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Backspin_ball")
ra = a * 3.1416 / 180
vx = v * np.cos(ra)
vy = v * np.sin(ra)
i = 0
while list2[i] >= 0:
    b = 0.0039 + 0.0058 / (1 + math.exp((v - 35) / 5))
    x = list1[i] + vx * dt
    list1.append(x)
    y = list2[i] + vy * dt
    list2.append(y)
    dvx = - b * v * vx * dt
    dvy = - b * v * vy * dt - g * dt
    vx += dvx
    vy += dvy
    v = math.sqrt(vx * vx + vy * vy)
    i += 1
v = 49.0
vx = v * np.cos(ra)
vy = v * np.sin(ra)
i = 0
while list4[i] >= 0:
    b = 0.0039 + 0.0058 / (1 + math.exp((v - 35) / 5))
    x = list3[i] + vx * dt
    list3.append(x)
    y = list4[i] + vy * dt
    list4.append(y)
    dvx = - s * vy * w * dt - b * v * vx * dt
    dvy = s * vx * w * dt - b * v * vy * dt - g * dt
    vx += dvx
    vy += dvy
    v = math.sqrt(vx * vx + vy * vy)
    i += 1
plt.xlim(0,150)
plt.ylim(0,150)
X1 = np.array(list1)
Y1 = np.array(list2)
X2 = np.array(list3)
Y2 = np.array(list4)
plt.plot(X1,Y1,color="blue", linewidth=2.5, linestyle="-",label="no-spin_ball")
plt.plot(X2,Y2,color="red", linewidth=2.5, linestyle="-",label="backspin_ball") 
plt.legend()  
plt.show()