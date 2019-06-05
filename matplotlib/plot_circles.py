import matplotlib.pyplot as plt
import numpy as np


def xy(r, phi,  c_1=0, c_2=0):
    ''' Cartesian coordinates for point at polar coordinates r, phi with origin (c_1, c_2) '''
    return r*np.cos(phi) + c_1, r*np.sin(phi) + c_2

def circle(r, phi_0=0, phi_1=2*np.pi, c_1=0, c_2=0):
    ''' 
    Circle arc with center (c_1, c_2) and radius r between the given angle values.
    
    Args:

      - r (float) :     Circle radius
      - phi_0 (float):  Angle for origin point of the arc 
      - phi_1 (float):  Angle for end point of the arc
      - c_1 (float):    x coordinate of circle center
      - c_2 (float):    y coordinate of circle center

    '''
    phis = np.arange(phi_0, phi_1, 0.01)
    return xy(r, phis, c_1, c_2)


a = 1.0

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111,aspect='equal')

ax.plot(*circle(ax, 2., 0, np.pi/2))
ax.plot(*circle(ax, a, -np.pi/2, np.pi/2, 0, a))
ax.plot(*circle(ax, a/2, c_1=a*np.sqrt(2), c_2=a/2))

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
