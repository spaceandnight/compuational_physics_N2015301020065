import matplotlib.pyplot as plt
import math
import random
import numpy as np

mg = []
T1 = 1.5
T2 = 2.0
T3 = 2.25
T4 = 3.0

for i in range(0,10):
    row_i = []
    for j in range(0,10):
        a = 1
        row_i.append(a)
    mg.append(row_i)
    
def func(mg,T):
    mgnew = mg
    for i in range(0,10):
        for j in range(0,10):
            con = mgnew[i][j]
            if i == 0:
                a = mgnew[9][j]
            else:
                a = mgnew[i-1][j]
            if i == 9:
                b = mgnew[0][j]
            else:
                b = mgnew[i+1][j]
            if j == 0:
                c = mgnew[i][9]
            else:
                c = mgnew[i][j-1]
            if j == 9:
                d = mgnew[i][0]
            else:
                d = mgnew[i][j+1]
            E = 2 * (a + b + c + d) * con
            if E <= 0:
                mgnew[i][j] = -1 * con
            if E > 0:
                r = random.random()
                e = - E / T
                f = math.exp(e)
                if r <= f:
                    mgnew[i][j] = -1 * con
                else:
                    mgnew[i][j] = con
    return mgnew;

def func1(mg):
    b = 0
    for i in range(0,10):
        for j in range(0,10):
            a = mg[i][j]
            b += a
    M = b / 100.0
    return M;

def func2(mg):
    xa = []
    ya = []
    xb = []
    yb = []
    for i in range(0,10):
        for j in range(0,10):
            a = mg[i][j]
            if a > 0:
                xa.append(i)
                ya.append(j)
            else:
                xb.append(i)
                yb.append(j)
    xc = np.array(xa)
    yc = np.array(ya)
    xd = np.array(xb)
    yd = np.array(yb)
    return xc,yc,xd,yd;

t = np.arange(0,800,1)

listM1 = []
n = 0
while n < 800:
    mg = func(mg,T1)
    a = func1(mg)
    listM1.append(a)
    n += 1
x11,y11,x12,y12 = func2(mg)

listM2 = []
n = 0
while n < 800:
    mg = func(mg,T2)
    a = func1(mg)
    listM2.append(a)
    n += 1
x21,y21,x22,y22 = func2(mg)

listM3 = []
n = 0
while n < 800:
    mg = func(mg,T3)
    a = func1(mg)
    listM3.append(a)
    n += 1
x31,y31,x32,y32 = func2(mg)

listM4 = []
n = 0
while n < 800:
    mg = func(mg,T4)
    a = func1(mg)
    listM4.append(a)
    n += 1
x41,y41,x42,y42 = func2(mg)

M1 = np.array(listM1)
M2 = np.array(listM2)
M3 = np.array(listM3)
M4 = np.array(listM4)

plt.figure()
plt.subplot(2,2,1)
plt.title('T=1.5')
plt.xlabel('Time')
plt.ylabel('Magnetization')
plt.ylim(-1.2,1.2)
plt.plot(t,M1)
plt.subplot(2,2,2)
plt.title('T=2.0')
plt.xlabel('Time')
plt.ylabel('Magnetization')
plt.ylim(-1.2,1.2)
plt.plot(t,M2)
plt.subplot(2,2,3)
plt.title('T=2.25')
plt.xlabel('Time')
plt.ylabel('Magnetization')
plt.ylim(-1.2,1.2)
plt.plot(t,M3)
plt.subplot(2,2,4)
plt.title('T=3.0')
plt.xlabel('Time')
plt.ylabel('Magnetization')
plt.ylim(-1.2,1.2)
plt.plot(t,M4)
plt.show()

plt.figure()
plt.subplot(2,2,1)
plt.title('T=1.5')
plt.scatter(x11,y11,s=400,c='r')
plt.scatter(x12,y12,s=400,c='b')
plt.subplot(2,2,2)
plt.title('T=2.0')
plt.scatter(x21,y21,s=400,c='r')
plt.scatter(x22,y22,s=400,c='b')
plt.subplot(2,2,3)
plt.title('T=2.25')
plt.scatter(x31,y31,s=400,c='r')
plt.scatter(x32,y32,s=400,c='b')
plt.subplot(2,2,4)
plt.title('T=3.0')
plt.scatter(x41,y41,s=400,c='r')
plt.scatter(x42,y42,s=400,c='b')
plt.show()