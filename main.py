import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

# Task 1: Drawing two layered figures

EDGE = "#000000"  # black edge for all shapes
FILLS = ["#ff595e", "#ffca3a", "#8ac926", "#1982c4", "#f77f00", "#6a4c93"]  # fill colors
N = 6  # number of layers

def draw_circles(ax, r_max, shift, n_layers):
    radii = np.linspace(r_max, r_max / n_layers, n_layers)  # create decreasing radii
    for i, r in enumerate(radii):
        ax.add_patch(
            Circle(
                (-shift, 0), r,
                edgecolor=EDGE,
                facecolor=FILLS[i % len(FILLS)],
                lw=1.3
            )
        )

def draw_triangles(ax, s_max, shift, n_layers):
    def triangle(scale):
        α = math.pi / 2  # rotate starting angle
        return [
            (scale * math.cos(α + k * 2 * math.pi / 3),
             scale * math.sin(α + k * 2 * math.pi / 3))
            for k in range(3)
        ]

    scales = np.linspace(s_max, s_max / n_layers, n_layers)
    for i, s in enumerate(scales):
        pts = [(x + shift, y) for x, y in triangle(s)]  # shifted triangle
        x, y = zip(*(pts + [pts[0]]))  # close shape for outline
        ax.plot(x, y, color=EDGE, lw=1.3)
        ax.add_patch(
            Polygon(pts, closed=True, edgecolor="none", facecolor=FILLS[i % len(FILLS)])
        )

def task1():
    r_max = 2.5  # max radius for the circle set
    s_max = 4.5  # max side length for the triangle set
    shift = 4.5  # shift to place the second figure on the right

    # Set up the canvas
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.set_aspect("equal")
    ax.axis("off")  # hide axes

    # Draw shapes
    draw_circles(ax, r_max, shift, N)
    draw_triangles(ax, s_max, shift, N)

    # Adjust canvas limits so all shapes are visible
    x_max = shift + s_max + 0.5
    x_min = -shift - r_max - 0.5
    y_max = max(r_max, s_max) + 0.5
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(-y_max, y_max)

    plt.title("Task 1 – Geometric Layered Figures")
    plt.tight_layout()
    plt.show()


# Task 2: Drawing a logo with 4 isosceles triangles

EDGE_MONO = "#000000"
FACE_MONO = "white"
FACE_COLORS = ["#ff595e", "#ffca3a", "#8ac926", "#1982c4"]  #fill for coloured version
EDGE_COLORS = ["#d62828", "#f77f00", "#4d908e", "#6a4c93"]  #outlines for coloured version

def petal_vertices(base_len=2.0, height=3.0):
    # Create 4 isosceles triangles (petals) rotated at 0°, 90°, 180°, 270°
    petals = []
    for k in range(4):
        theta = math.radians(90 * k)
        d = np.array([math.cos(theta), math.sin(theta)])     # main direction
        p = np.array([-d[1], d[0]])                          # perpendicular
        apex = np.array([0.0, 0.0])                          # center of the shape
        base_center = d * height
        p1 = base_center + p * (base_len / 2)
        p2 = base_center - p * (base_len / 2)
        petals.append([apex, p1, p2])
    return petals

def draw_logo(*, mode, mono):
    # Draws the logo using 4 triangles.
    # mode: "lines" → outline using ax.plot, "poly"  → filled polygon
    # mono: True → black/whit , False → coloured
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.axis("off")
    petals = petal_vertices()

    for i, tri in enumerate(petals):
        if mode == "lines":
            x, y = zip(*(tri + [tri[0]]))  #outline the triangle
            ax.plot(x, y, color=EDGE_MONO if mono else EDGE_COLORS[i], lw=2)
            if not mono:
                ax.add_patch(
                    Polygon(tri, closed=True, facecolor=FACE_COLORS[i], edgecolor="none", alpha=0.35)
                )
        else:  #polygon
            ax.add_patch(
                Polygon(tri, closed=True,
                        edgecolor=EDGE_MONO if mono else EDGE_COLORS[i],
                        facecolor=FACE_MONO if mono else FACE_COLORS[i],
                        lw=2)
            )

    # rescale plot if only patches are used (poly mode)
    if mode == "poly":
        ax.relim()
        ax.autoscale_view()

    plt.title(f"Logo – {mode} – {'mono' if mono else 'colour'}")
    plt.show()

def task2():
    draw_logo(mode="lines", mono=True)
    draw_logo(mode="lines", mono=False)
    draw_logo(mode="poly", mono=True)
    draw_logo(mode="poly", mono=False)


# Task 3: Signal plots
# Draws 3 test signals and a combined plot.

def task3():
    a = 35  # student number
    x = np.linspace(-4 * math.pi, 4 * math.pi, 1000)

    # Define the signals
    y1 = 0.01 * a * np.sin(x)
    y2 = 0.01 * (a + 3) * np.sin(x)
    y3 = 0.01 * a * np.cos(x)

    # Create 2x2 subplot layout
    fig, axs = plt.subplots(2, 2, figsize=(10, 7))
    axs = axs.ravel()
    # Plot each signal individually
    axs[0].plot(x, y1, color='red')
    axs[0].set_title("Signal 1: y₁(x) = 0.35·sin(x)")

    axs[1].plot(x, y2, color='green')
    axs[1].set_title("Signal 2: y₂(x) = 0.38·sin(x)")

    axs[2].plot(x, y3, color='blue')
    axs[2].set_title("Signal 3: y₃(x) = 0.35·cos(x)")

    # Combine all signals in one graph
    axs[3].plot(x, y1, 'r', label='y₁ = 0.35·sin(x)')
    axs[3].plot(x, y2, 'g', label='y₂ = 0.38·sin(x)')
    axs[3].plot(x, y3, 'b', label='y₃ = 0.35·cos(x)')
    axs[3].set_title("Combined signals")
    axs[3].legend()

    # Grid, axis, styling for all subplots
    for ax in axs:
        ax.grid(True)
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    fig.suptitle("Task 3 – Signal envelopes (a = 35, variant 5)")
    plt.tight_layout()
    plt.show()


# Main entry point
def main():
    task1()
    task2()
    task3()

if __name__ == "__main__":
    main()

