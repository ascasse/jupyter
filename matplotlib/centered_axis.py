import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, aspect="equal")

# forces that spines intersect at 0,0
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")

# set arbitrary axes dimensions
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Eliminate upper and right spines
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

# Hide ticks
ax.get_xaxis().set_ticks([-1, -0.5, 0.5, 1])
ax.get_yaxis().set_ticks([-1, -0.5, 0.5, 1])

plt.show()
