import math
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

a = 1.0

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, aspect='equal')

# Hide axis
ax.spines[['top', 'right', 'bottom', 'left']].set_visible(False)

# Hide ticks
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])

# Draw circles
ax.add_patch(Wedge((0, 0), 2*a, 0, 90, edgecolor='black', facecolor='lightgray'))
ax.add_patch(Wedge((0, a), a, -90, 90, edgecolor='black', facecolor='white'))
ax.add_patch(Wedge((a * math.sqrt(2.0), a/2), a/2, 0, 360, edgecolor='black', facecolor='white'))

# Draw something to prevent clipping of the figure.
ax.plot([0, 0, 0], zorder=1)

plt.show()
