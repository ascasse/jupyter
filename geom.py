"""
Simple elements
"""
from typing import Sequence
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def circle_dot(center):
    """Draw a circle to represent a point"""
    return Circle(center, 0.05, ec="black", color="w", zorder=100)


def triangle(
    v_a: Sequence[float], v_b: Sequence[float], v_c: Sequence[float], axt: plt.Axes
):
    """Draw a triangle with given vertices"""
    plt.axline(v_a, v_b, linewidth=0.5, color="r")
    plt.axline(v_b, v_c, linewidth=0.5, color="r")
    plt.axline(v_c, v_a, linewidth=0.5, color="r")

    axt.add_patch(circle_dot(A))
    axt.add_patch(circle_dot(B))
    axt.add_patch(circle_dot(C))


fig, ax = plt.subplots(figsize=(8, 8))

A = [-5.0, -2.0]
B = [-3.0, 2.0]
C = [4.0, -1.0]

triangle(A, B, C, ax)

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
plt.show()
