import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from scipy.stats import multivariate_normal



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.plot_surface(x,y,z)
#ax.plot_wireframe(x,y,z)

plt.show()