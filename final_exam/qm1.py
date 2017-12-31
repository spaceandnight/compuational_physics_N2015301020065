import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(-4,4,0.1)
T = np.arange(0.1,8.1,0.1)
t = 0.1
t1 = 0.1
list1 = []
list2 = []
y1 = x
a = input('a = ')
b = a * x
y2 = np.tanh(b)
def func(T):
    m = 4 / T
    a = 0
    b = np.tanh(m * a)
    c = 0.1
    if T >= 4:
        M = 0
    else:
        while c > 0.0002:
            if a <= b:
                a += c
                b = np.tanh(m * a)
            else:
                a -= c
                b = np.tanh(m * a)
                c = c / 10
        M = a + c/2
    return M;
while t <= 8:
    ad = func(t)
    list1.append(ad)
    t += 0.1
d = 0.047
while t1 <= 8:
    if t1 >= 4:
        ad = 0
    else:
        e = 4 - t1
        f = e * d
        g = math.sqrt( f )
        ad = t1 * g
    list2.append(ad)
    t1 += 0.1
M = np.array(list1)
M1 = np.array(list2)
plt.figure(1)
plt.plot(x,y1,label='<s>')
plt.plot(x,y2,label='tanh')
plt.xlabel('<s>')
plt.ylabel('y')
plt.legend()
plt.show()
plt.figure(2)
plt.plot(T,M,label='8.11')
plt.plot(T,M1,label='8.14')
plt.title('The line of M-T')
plt.xlabel('Temperature')
plt.ylabel('Magnetization')
plt.legend()
plt.show()
