"""
    regular_polygons

    Draw regular polygons.

"""

from cmath import cos, pi, sin
from typing import List
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
from pandas import array

import numpy as np


def get_vertices(radius: float, sides: int) -> List:
    """
    Calculate vertices for a regular polygon inscribed in a circunference of
    given radius centered at the origin.
    """
    # initial point
    p_0 = (-radius, 0)
    # rotation angle
    theta = 2 * pi / sides
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
radius = 6.0
sides = 6
vertices = get_vertices(radius, sides)

fig, ax = plt.subplots(figsize=(10, 10))
polygon = Polygon(vertices, True, color="red", ec="black", lw=1.5)
# circle = Circle((0, 0), radius=radius, fill=False, color='gray', lw=.5)

ax.add_patch(polygon)

# Hide axis
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("none")
ax.spines["bottom"].set_color("none")

# Hide ticks
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])


ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
plt.show()
