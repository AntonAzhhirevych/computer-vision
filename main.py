import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.colors as mcolors
# from matplotlib.animation import PillowWriter

# --- Color and Projection Config ---
EDGE_COLOR = "#000000"

# Generate smooth color transition (HSV color cycle)
def get_smooth_color(frame):
    hue = (frame % 360) / 360  # normalized to [0,1]
    rgb = mcolors.hsv_to_rgb((hue, 1, 1))
    return rgb

# Define cube vertices (unit cube with 8 corners)
cube_vertices = np.array([
    [0, 0, 0], [1, 0, 0],  # bottom face (z=0)
    [1, 1, 0], [0, 1, 0],
    [0, 0, 1], [1, 0, 1],  # top face (z=1)
    [1, 1, 1], [0, 1, 1]
])

# Define cube faces using vertex indices
faces = [
    [0, 1, 2, 3],  # bottom face
    [4, 5, 6, 7],  # top face
    [0, 1, 5, 4],  # side faces
    [2, 3, 7, 6],
    [1, 2, 6, 5],
    [3, 0, 4, 7]
]

# Convert points to homogeneous coordinates (adds 1 as 4th component)
def to_homogeneous(points):
    ones = np.ones((points.shape[0], 1))
    return np.hstack([points, ones]).T

# Convert back from homogeneous coordinates to 3D
def from_homogeneous(hpoints):
    return (hpoints[:3, :] / hpoints[3, :]).T

# Create axonometric (isometric) projection matrix using Rx and Ry
def axonometric_matrix():
    angle_x = np.radians(35.26)
    angle_y = np.radians(45)
    Rx = np.array([
        [1, 0, 0, 0],
        [0, np.cos(angle_x), -np.sin(angle_x), 0],
        [0, np.sin(angle_x),  np.cos(angle_x), 0],
        [0, 0, 0, 1]
    ])
    Ry = np.array([
        [np.cos(angle_y), 0, np.sin(angle_y), 0],
        [0, 1, 0, 0],
        [-np.sin(angle_y), 0, np.cos(angle_y), 0],
        [0, 0, 0, 1]
    ])
    return Ry @ Rx

# Build uniform scaling matrix centered around the middle of the cube
def scale_matrix(s):
    center = np.mean(cube_vertices, axis=0)
    translate_to_origin = np.array([
        [1, 0, 0, -center[0]],
        [0, 1, 0, -center[1]],
        [0, 0, 1, -center[2]],
        [0, 0, 0, 1]
    ])
    scale = np.array([
        [s, 0, 0, 0],
        [0, s, 0, 0],
        [0, 0, s, 0],
        [0, 0, 0, 1]
    ])
    translate_back = np.array([
        [1, 0, 0, center[0]],
        [0, 1, 0, center[1]],
        [0, 0, 1, center[2]],
        [0, 0, 0, 1]
    ])
    return translate_back @ scale @ translate_to_origin

# Initialize the plot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect("equal")
ax.axis("off")
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Animation frame update function
def update(frame):
    ax.cla()  # Clear previous frame
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.axis("off")

    # Calculate dynamic scale and smooth color
    scale = 0.5 + 0.5 * np.sin(np.radians(frame * 2))
    color = get_smooth_color(frame)

    # Apply transformation: scaling and axonometric projection
    homog = to_homogeneous(cube_vertices)
    transform = axonometric_matrix() @ scale_matrix(scale)
    projected = from_homogeneous(transform @ homog)

    # Draw filled polygon faces
    for face in faces:
        face_2d = projected[face][:, :2]  # Extract x, y only
        polygon = plt.Polygon(face_2d, facecolor=color, edgecolor=None, linewidth=0)
        ax.add_patch(polygon)

    # Draw edge lines (wireframe) for each face
    for face in faces:
        indices = face + [face[0]]  # Close the polygon
        for i in range(len(indices) - 1):
            p1 = projected[indices[i]][:2]
            p2 = projected[indices[i + 1]][:2]
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=EDGE_COLOR, linewidth=1)

# Run animation
ani = FuncAnimation(fig, update, frames=360, interval=50, repeat=True)
plt.title("3D Cube with Axonometric Projection and Smooth Fill", pad=20)
plt.show()


# writer = PillowWriter(fps=10)
# ani.save("сube.gif", writer=writer)