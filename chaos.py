import matplotlib.pyplot as plt
import numpy as np
import math
a0 = 0.2
a1 = 0.201
FD = input('FD = ')
Og = 1.0
OD = 0.67
q = 0.5
dt = 0.04
m = math.pi
m2 = 2 * m
wx0 = 0
wx1 = 0
list1 = [0]
list2 = [a0]
list3 = [a1]
n = math.log(0.001)
list4 = [n]
i = 0
while i < 4000:
    t = list1[i]
    ax = list2[i]
    Fx = OD * t
    wx0 = wx0 - Og * dt * np.sin(ax) - q * wx0 * dt + FD * dt * np.sin(Fx)
    a = ax + wx0 * dt
    while a > m:
        a -= m2
    while -a > m:
        a += m2
    list2.append(a)
    ax = list3[i]
    wx1 = wx1 - Og * dt * np.sin(ax) - q * wx1 * dt + FD * dt * np.sin(Fx)
    a = ax + wx1 * dt
    while a > m:
        a -= m2
    while -a > m:
        a += m2
    list3.append(a)
    t += dt
    list1.append(t)
    i += 1
    da0 = list3[i] - list2[i]
    if da0 == 0:
        list4.append(-40)
    else:
        da1 = abs(da0)
        da2 = math.log(da1)
        list4.append(da2)
T = np.array(list1)
A0 = np.array(list2)
A1 = np.array(list3)
DA = np.array(list4)
plt.figure(figsize=(8,6))
plt.plot(T,A0,color="red", linewidth=2.5, linestyle="-",label="a(0)=0.2")
plt.plot(T,A1,color="blue", linewidth=2.5, linestyle="-",label="a(0)=0.201")
plt.ylabel("angle (radians)")
plt.title("angle versus time")
plt.xlabel("time (s)")
plt.legend()
plt.show()
plt.figure(figsize=(8,6))
plt.plot(T,DA,color="red", linewidth=2.5, linestyle="-",label="da(0)=0.01")
plt.ylabel("difference of angle (radians)")
plt.title("difference of angle versus time")
plt.xlabel("time (s)")
plt.legend()
plt.show()