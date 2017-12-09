from __future__ import division
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from copy import deepcopy

k = 0
grid = []
for i in range(48):    
    row_i = []
    for j in range(48):
        if i == 0 or i == 47 or j == 0 or j == 47:
            voltage = 0
        elif i >= 16 and i <= 31 and j >= 16 and j <= 31:
            voltage = 1
        else:
            voltage = 0
        row_i.append(voltage)
    grid.append(row_i)
while k <= 800:
    k += 1
    for i in range(48):    
        for j in range(48):
            if i == 0 or i == 47 or j == 0 or j == 47:
                pass
            elif i >= 16 and i <= 31 and j >= 16 and j <= 31:
                pass
            else:
                voltage_new = (grid[i+1][j] + grid[i-1][j] + grid[i][j+1] + grid[i][j-1])/4
                grid[i][j] = voltage_new


matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'



x = np.linspace(-1,1,48)
y = np.linspace(-1,1,48)
X, Y = np.meshgrid(x, y)
Z = grid

 

CS = plt.contour(X,Y,Z,12)
plt.clabel(CS, inline=1, fontsize=12)
plt.title('voltage near capacitor')
plt.xlabel('x(m)')
plt.ylabel('y(m)')

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap = cm.jet,linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_ylabel('y(m)')
ax.set_zlabel('voltage(V)')
ax.set_title('voltage distribution')

plt.show()