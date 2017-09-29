import matplotlib.pyplot as plt
import numpy as np
list1 = [0,0,0,0,0,0,0,0,0,0,0];
list2 = [0,0,0,0,0,0,0,0,0,0,0];
v = 40
h = 1
d = v * h
i = 0
j = 1
while j != 11:
    list1[j] = list1[i] + h
    list2[j] = list2[i] + d
    i += 1
    j += 1
T = np.array(list1)
X = np.array(list2)
plt.plot(T,X,marker='o',mec='b',mfc='w',color='r')
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.title('line of x-t')
plt.show()
