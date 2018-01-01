import matplotlib.pyplot as plt
import math
import random
import numpy as np

mg1 = []
mg2 = []
mg3 = []

for i in range(0,10):
    row_i = []
    for j in range(0,10):
        a = 1
        row_i.append(a)
    mg1.append(row_i)
    
for i in range(0,10):
    row_i = []
    for j in range(0,10):
        a = 1
        row_i.append(a)
    mg3.append(row_i)

for i in range(0,10):
    we1_i = []
    for j in range(0,10):
        we2_j = []
        for k in range(0,10):
            a = 1
            we2_j.append(a)
        we1_i.append(we2_j)
    mg2.append(we1_i)

def func1(mg0,T):
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

def func2(mg0,T):
    mgnew = mg0
    for i in range(0,10):
        for j in range(0,10):
            con = mgnew[i][j]
            if i == 0:
                a = 0
            else:
                a = mgnew[i-1][j]
            if i == 9:
                b = 0
            else:
                b = mgnew[i+1][j]
            if j == 0:
                c = 0
            else:
                c = mgnew[i][j-1]
            if j == 9:
                d = 0
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

def func3(mg0,T):
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

def func4(mg0):
    mgnew = mg0
    a = 0
    for i in range(0,10):
        for j in range(0,10):
            a += mgnew[i][j]
    b = a / 100.0
    return b;

def func5(mg0):
    mgnew = mg0
    a = 0
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                a += mgnew[i][j][k]
    b = a / 1000.0
    return b;

list1 = []
list2 = []
T = 0.2
while T <= 6:
    n = 0
    b = 0
    mga = mg1
    while n <= 800:
        mga = func1(mga,T)
        a = func4(mga)
        b += a
        n += 1
    c = b / 800.0
    list1.append(T)
    list2.append(c)
    if T <= 1.0 or T >= 3.0:
        T += 0.4
    else:
        T += 0.1

list3 = []
list4 = []
T = 0.2
while T <= 6:
    n = 0
    b = 0
    mgb = mg3
    while n <= 800:
        mgb = func2(mgb,T)
        a = func4(mgb)
        b += a
        n += 1
    c = b / 800.0
    list3.append(T)
    list4.append(c)
    if T <= 1.0 or T >= 3.0:
        T += 0.4
    else:
        T += 0.1
'''        
list5 = []
list6 = []
T = 0.2
while T <= 6:
    n = 0
    b = 0
    mgc = mg2
    while n <= 800:
        mgb = func3(mgc,T)
        a = func5(mgc)
        b += a
        n += 1
    c = b / 800.0
    list5.append(T)
    list6.append(c)
    if T <= 3.5 or T >= 5.5:
        T += 0.4
    else:
        T += 0.1
'''
X1 = np.array(list1)
X2 = np.array(list2)
X3 = np.array(list3)
X4 = np.array(list4)
'''
X5 = np.array(list5)
X6 = np.array(list6)
'''
plt.figure()
plt.title('10*10 periodic boundary')
plt.xlabel('Temperatuer')
plt.ylabel('Magnetization')
plt.scatter(X1,X2)
plt.show()
plt.figure()
plt.title('10*10 free boundary')
plt.xlabel('Temperatuer')
plt.ylabel('Magnetization')
plt.scatter(X3,X4)
plt.show()
'''
plt.figure()
plt.title('10*10*10 periodic boundary')
plt.xlabel('Temperatuer')
plt.ylabel('Magnetization')
plt.scatter(X5,X6)
plt.show()
'''