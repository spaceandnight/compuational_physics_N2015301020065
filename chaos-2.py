import matplotlib.pyplot as plt
import numpy as np
import math
a = 0.2
FD = input('FD = ')
n = input('n = ')
j = 0
q = 0.5
dt = 0.04
m = math.pi
m2 = 2 * m
OD = m2 / 10
w = 0
list1 = []
list2 = []
i = 0
t = 0
b = 250.0 * n + 1.0
while i < b:
    j += 1
    wx = w
    ax = a
    Fx = OD * t
    w = wx- dt * np.sin(ax) - q * wx * dt + FD * dt * np.sin(Fx)
    a = ax + w * dt
    while a > m:
        a -= m2
    while -a > m:
        a += m2
    if j >= 250:
        list1.append(a)
        list2.append(w)
        j -= 250
    i += 1
    t = i * dt
As = np.array(list1)
Ws = np.array(list2)
plt.figure(figsize=(8,6))
plt.scatter(As, Ws, s=10)
plt.ylabel("angular velocity (rad/s)")
plt.title("angular velocity versus angle")
plt.xlabel("angle (rad)")
plt.legend()
plt.show()
