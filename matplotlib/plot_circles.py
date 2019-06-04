import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle


def xy(r,phi):
  return r*np.cos(phi), r*np.sin(phi)

# Circle at center (c_1, c_2) with radius r
def xy_2(r,phi, c_1, c_2):
    return r*np.cos(phi) + c_1, r*np.sin(phi) + c_2

a = 1.0

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111,aspect='equal')  

phis = np.arange(0,3.14/2,0.01)
r =2.
ax.plot( *xy(r,phis), c='r',ls='-' )

phis = np.arange(-3.14/2, 3.14/2, 0.01)
r = 1.
c_1 = 0.0
c_2 = 1.
ax.plot( *xy_2(r, phis, c_1, c_2), ls='-' )

phis = np.arange(0.,6.28,0.01)
r = 0.5
c_1 = np.sqrt(2)
c_2 = 0.5
ax.plot( *xy_2(r,phis, c_1, c_2), ls='-' )

# Horizontal line
ax.plot([0,0,0], zorder = 1)

# Vertical line
ax.plot([0,0,0], [0,1,2], zorder = 1)

# Hide axis
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')

ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# Set ticks
ax.get_xaxis().set_ticks([a, 2*a])
ax.get_yaxis().set_ticks([a, 2*a])
ax.set_xticklabels(('$a$', '$2a$'))
ax.set_yticklabels(('$a$', '$2a$'))

plt.show()