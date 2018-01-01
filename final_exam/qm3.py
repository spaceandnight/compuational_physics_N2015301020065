import matplotlib.pyplot as plt
import math
import random
import numpy as np
mg = []
T = 0.2
for i in range(0,10):
    row_i = []
    for j in range(0,10):
        a = 1
        row_i.append(a)
    mg.append(row_i)

def func(mg0,T):
    mgnew = mg0
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

def func1(mg,T):
    mg3 = mg
    n = 0
    d = 0
    while n < 1000:
        c = 0
        mg3 = func(mg3,T)
        for i in range(0,10):
            for j in range(0,10):
                if i == 9:
                    a = mg3[i][j] * mg3[0][j]
                    c += a
                else:
                    a = mg3[i][j] * mg3[i+1][j]
                    c += a
                if j == 9:
                    b = mg3[i][j] * mg3[i][0]
                    c += b
                else:
                    b = mg3[i][j] * mg3[i][j+1]
                    c += b
        d -= c
        n += 1
    e = d / 100000.0
    return e;

listE = []
listT = []
while T <= 6:
    E = func1(mg,T)
    listT.append(T)
    listE.append(E)
    T += 0.2

listc1 = []
listt1 = []
for i in range(0,27):
    a = listE[i+1] - listE[i]
    c = a / 0.2
    t = listT[i] + 0.1
    listc1.append(c)
    listt1.append(t)

Tx = np.array(listT)
Ex = np.array(listE)
C1 = np.array(listc1)
T1 = np.array(listt1)
plt.figure()
plt.xlabel('Temperature')
plt.ylabel('Energy per spin')
plt.scatter(Tx,Ex,s=30)
plt.show()
plt.figure()
plt.xlabel('Temperature')
plt.ylabel('Specific heat per spin')
plt.scatter(T1,C1,s=30)
plt.show()