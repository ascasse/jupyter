import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def func(x):
    return 1 / x

x = np.linspace(0.5, 5)
y = func(x)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111,aspect='equal')

plt.plot(x, y, 'r', linewidth=2)
# plt.xlim(xmin=-1)
# plt.ylim(ymin=-1)
plt.axis('equal')
plt.show()