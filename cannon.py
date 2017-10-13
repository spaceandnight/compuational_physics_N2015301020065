import matplotlib.pyplot as plt
import numpy as np
list1 = [0,0]
list2 = [0,0]
list3 = [0,0]
list4 = [0,0]
v = 700.0
g = 9.8
a = input('angle=')
ra = a * 3.14 / 180
vx = v * np.cos(ra)
vy = v * np.sin(ra)
dt = 1
list1[1] = list1[0] + vx * dt
list2[1] = list2[0] + vy * dt
vy -= g * dt
i = 1
while list2[i] >= 0:
    x = list1[i] + vx * dt
    list1.append(x)
    y = list2[i] + vy * dt
    list2.append(y)
    vy -= g * dt
    i += 1
X1 = np.array(list1)
Y1 = np.array(list2)
vy = v * np.sin(ra)
list3[1] = list3[0] + vx * dt
list4[1] = list4[0] + vy * dt
vy -= g * dt
j = 1
R = 6371000.0
while list4[j] >= 0:
    x = list3[j] + vx * dt
    list3.append(x)
    y = list4[j] + vy * dt
    list4.append(y)
    r = R + list4[j]
    b = R / r
    c = b**2
    vy -= g * c * dt
    j += 1
X2 = np.array(list3)
Y2 = np.array(list4)
plt.figure(figsize=(8,6))
plt.plot(X1,Y1,color="red", linewidth=2.5, linestyle="-",label="g=g0")
plt.plot(X2,Y2,color="blue", linewidth=2.5, linestyle="-",label="g=g(y)")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("gravity effect")
plt.xlim(0,60000)
plt.ylim(0,20000)
plt.legend()
plt.show()
