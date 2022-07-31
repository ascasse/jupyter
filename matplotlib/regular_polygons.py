'''
    regular_polygons

    Draw regular polygons.

'''

from cmath import cos, pi, sin

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
from pandas import array

import numpy as np


def get_vertices(radius: float, sides: int) -> array:
    '''
        Calculate vertices for a regular polygon inscribed in a circunference of
        given radius centered at the origin.
    '''
    # initial point
    p_0 = (-radius, 0)
    # rotation angle
    theta = 2*pi/sides
    # transformation
    r_theta = ([cos(theta), -sin(theta)], [sin(theta), cos(theta)])

    vertices = [p_0]
    p = p_0
    for i in range(sides - 1):
        p = np.dot(p, r_theta)
        p_real = p.real
        vertices.append((p_real[0], p_real[1]))

    return vertices


# Build an hexagon inscribed in a circle with radius 4
radius = 4.0
sides = 6
vertices = get_vertices(radius, sides)

fig, ax = plt.subplots(figsize=(8, 8))
polygon = Polygon(vertices, True, color='red', ec='black', lw=1.5)
circle = Circle((0, 0), radius=radius, fill=False, color='gray', lw=.5)

ax.add_patch(polygon)
ax.add_patch(circle)

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
plt.show()
