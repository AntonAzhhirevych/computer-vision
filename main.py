import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Global config
FILL_COLORS = ["#f94144", "#f3722c", "#f8961e", "#90be6d"]
EDGE_COLOR = "#000000"

ANGLE_STEP = np.pi / 30
SCALE_STEP = 0.02
DX, DY = 0.5, 0.5

# Initial triangle vertices in homogeneous coordinates
BASE_TRIANGLE = np.array([
    [0, 1, 0.5],
    [0, 0, 1],
    [1, 1, 1]
])

# Frame state
frame = {
    "angle": 0,
    "scale": 1.0,
    "scale_dir": 1,
    "color_index": 0
}

# Transformation pipeline: Scale → Rotate → Translate
def transform(vertices, angle, scale):
    R = np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle),  np.cos(angle), 0],
        [0, 0, 1]
    ])
    S = np.array([
        [scale, 0, 0],
        [0, scale, 0],
        [0, 0, 1]
    ])
    T = np.array([
        [1, 0, DX],
        [0, 1, DY],
        [0, 0, 1]
    ])
    return T @ R @ S @ vertices

# Setup plot
fig, ax = plt.subplots()
transformed_triangle = transform(BASE_TRIANGLE, 0, 1)
polygon = plt.Polygon(
    transformed_triangle[:2].T,
    closed=True,
    facecolor=FILL_COLORS[0],
    edgecolor=EDGE_COLOR,
    linewidth=2
)
ax.add_patch(polygon)
ax.set_xlim(-2, 3)
ax.set_ylim(-2, 3)
ax.set_aspect("equal")
ax.axis("off")

# Update function for animation
def update(_):
    # Update rotation and scale
    frame["angle"] += ANGLE_STEP
    frame["scale"] += frame["scale_dir"] * SCALE_STEP

    # Reverse scale direction and switch fill color
    if frame["scale"] > 1.5 or frame["scale"] < 0.5:
        frame["scale_dir"] *= -1
        frame["color_index"] = (frame["color_index"] + 1) % len(FILL_COLORS)

    # Apply transformation
    transformed = transform(BASE_TRIANGLE, frame["angle"], frame["scale"])
    polygon.set_xy(transformed[:2].T)
    polygon.set_facecolor(FILL_COLORS[frame["color_index"]])
    return polygon,

# Run animation
ani = FuncAnimation(fig, update, frames=200, interval=100, blit=True)

# Save as GIF
# ani.save("animated_triangle.gif", writer="pillow", fps=10)

plt.title("Animated 2D Triangle – Transformations with Color Change", pad=20)
plt.show()
