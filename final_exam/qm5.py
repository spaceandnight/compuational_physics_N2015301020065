from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import random
import numpy as np

mg = []
T1 = 3.5
T2 = 4.0
T3 = 4.4
T4 = 5.0

for i in range(0,10):
    we1_i = []
    for j in range(0,10):
        we2_j = []
        for k in range(0,10):
            a = 1
            we2_j.append(a)
        we1_i.append(we2_j)
    mg.append(we1_i)

def func1(mg0,T):
    mgnew = mg0
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                con = mgnew[i][j][k]
                if i == 0:
                    a = mgnew[9][j][k]
                else:
                    a = mgnew[i-1][j][k]
                if i == 9:
                    b = mgnew[0][j][k]
                else:
                    b = mgnew[i+1][j][k]
                if j == 0:
                    c = mgnew[i][9][k]
                else:
                    c = mgnew[i][j-1][k]
                if j == 9:
                    d = mgnew[i][0][k]
                else:
                    d = mgnew[i][j+1][k]
                if k == 0:
                    e = mgnew[i][j][9]
                else:
                    e = mgnew[i][j][k-1]
                if k == 9:
                    f = mgnew[i][j][0]
                else:
                    f = mgnew[i][j][k+1]
                E = 2 * (a + b + c + d + e + f) * con
                if E <= 0:
                    mgnew[i][j][k] = -1 * con
                if E > 0:
                    r = random.random()
                    g = - E / T
                    h = math.exp(g)
                    if r <= h:
                        mgnew[i][j][k] = -1 * con
                    else:
                        mgnew[i][j][k] = con
    return mgnew;

def func2(mg0):
    mgnew = mg0
    x1 = []
    y1 = []
    z1 = []
    x2 = []
    y2 = []
    z2 = []
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                a = mgnew[i][j][k]
                if a > 0:
                    x1.append(i)
                    y1.append(j)
                    z1.append(k)
                else:
                    x2.append(i)
                    y2.append(j)
                    z2.append(k)
    return x1,y1,z1,x2,y2,z2;

n = 0
while n < 200:
    mg = func1(mg,T1)
    n += 1
x11,y11,z11,x12,y12,z12 = func2(mg)
xdata11 = np.array(x11)
ydata11 = np.array(y11)
zdata11 = np.array(z11)
xdata12 = np.array(x12)
ydata12 = np.array(y12)
zdata12 = np.array(z12)

n = 0
while n < 200:
    mg = func1(mg,T2)
    n += 1
x21,y21,z21,x22,y22,z22 = func2(mg)
xdata21 = np.array(x21)
ydata21 = np.array(y21)
zdata21 = np.array(z21)
xdata22 = np.array(x22)
ydata22 = np.array(y22)
zdata22 = np.array(z22)

n = 0
while n < 200:
    mg = func1(mg,T3)
    n += 1
x31,y31,z31,x32,y32,z32 = func2(mg)
xdata31 = np.array(x31)
ydata31 = np.array(y31)
zdata31 = np.array(z31)
xdata32 = np.array(x32)
ydata32 = np.array(y32)
zdata32 = np.array(z32)

n = 0
while n < 200:
    mg = func1(mg,T4)
    n += 1
x41,y41,z41,x42,y42,z42 = func2(mg)
xdata41 = np.array(x41)
ydata41 = np.array(y41)
zdata41 = np.array(z41)
xdata42 = np.array(x42)
ydata42 = np.array(y42)
zdata42 = np.array(z42)

plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(xdata11, ydata11, zdata11, c='r')
ax.scatter3D(xdata12, ydata12, zdata12, c='b')
plt.title('T=3.5')
plt.show()

plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(xdata21, ydata21, zdata21, c='r')
ax.scatter3D(xdata22, ydata22, zdata22, c='b')
plt.title('T=4.0')
plt.show()

plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(xdata31, ydata31, zdata31, c='r')
ax.scatter3D(xdata32, ydata32, zdata32, c='b')
plt.title('T=4.4')
plt.show()

plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(xdata41, ydata41, zdata41, c='r')
ax.scatter3D(xdata42, ydata42, zdata42, c='b')
plt.title('T=5.0')
plt.show()