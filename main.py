import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import colors as mcolors
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
# from matplotlib.animation import PillowWriter

# Global config
FILL_COLORS = ["#f94144", "#f3722c", "#f8961e", "#90be6d", "#43aa8b", "#577590"]
EDGE_COLOR = "#000000"

# Define pyramid vertices (triangular base)
vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0.5, 0, np.sqrt(3) / 2],
    [0.5, 1, np.sqrt(3) / 6]
])

# Faces of the pyramid
faces = [
    [0, 1, 2],
    [0, 1, 3],
    [1, 2, 3],
    [2, 0, 3]
]

# Homogeneous transformation helpers
def to_homogeneous(pts):
    ones = np.ones((pts.shape[0], 1))
    return np.hstack([pts, ones]).T

def from_homogeneous(h_pts):
    return (h_pts[:3, :] / h_pts[3, :]).T

# Rotation matrix around Y axis
def rotate_y(angle_deg):
    theta = np.radians(angle_deg)
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [ c, 0, s, 0],
        [ 0, 1, 0, 0],
        [-s, 0, c, 0],
        [ 0, 0, 0, 1]
    ])

# Linear interpolation between two RGB tuples
def lerp_color(c1, c2, t):
    return tuple((1 - t) * np.array(c1) + t * np.array(c2))

# Setup figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1, 1, 1])
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 2)
ax.set_zlim(-1, 2)
ax.axis('off')

def update(frame):
    # Clear previous drawings
    while ax.collections:
        ax.collections[0].remove()

    # Rotation and transparency
    angle = (frame * 3) % 360
    alpha = (np.sin(np.radians(frame * 4)) + 1) / 2

    if alpha < 0.01:
        return

    # Transform vertices
    homog = to_homogeneous(vertices)
    rotated = from_homogeneous(rotate_y(angle) @ homog)
    poly3d = [rotated[face] for face in faces]

    # Interpolate between two colors
    t = (frame % 60) / 60
    idx1 = (frame // 60) % len(FILL_COLORS)
    idx2 = (idx1 + 1) % len(FILL_COLORS)
    color1 = mcolors.to_rgb(FILL_COLORS[idx1])
    color2 = mcolors.to_rgb(FILL_COLORS[idx2])
    interpolated_color = lerp_color(color1, color2, t)

    # Apply alpha to edge color
    edge_rgba = (*mcolors.to_rgb(EDGE_COLOR), alpha)

    # Draw frame
    collection = Poly3DCollection(
        poly3d,
        facecolors=[(*interpolated_color, alpha)],
        edgecolors=[edge_rgba],
        linewidths=1
    )
    ax.add_collection3d(collection)

ani = FuncAnimation(fig, update, frames=360, interval=50, repeat=True)
plt.title("3D Triangle Pyramid – Smooth Color and Opacity Transition", pad=20)
plt.show()

# writer = PillowWriter(fps=10)
# ani.save("pyramid.gif", writer=writer)
