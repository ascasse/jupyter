
# Draw axes for 1st quadrant

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, aspect="equal")

# Force that spines intersect at 0,0
ax.spines["left"].set_position("zero")  # type: ignore
ax.spines["bottom"].set_position("zero")  # type: ignore

# Eliminate upper and right spines
ax.spines[["top", "right"]].set_visible(False)

ax.set_xlim(-0.25, 3)
ax.set_ylim(-0.25, 2)

# Hide ticks
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([])

plt.show()
