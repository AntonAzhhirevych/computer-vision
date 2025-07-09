# 3D Animated Pyramid with Color & Opacity Transitions

This project demonstrates 3D rendering and animation using Python's `matplotlib` and `numpy`. It visualizes a triangular-based pyramid that rotates smoothly around the Y-axis while dynamically transitioning its face color and transparency.

## Overview

The animation showcases:

- A **triangular-based 3D pyramid** rendered in axonometric projection.
- **Continuous rotation** around the Y-axis.
- **Smooth color interpolation** between predefined colors.
- **Dynamic alpha blending** for fade-in and fade-out effects during rotation.

Useful for understanding 3D object construction, transformation matrices, homogeneous coordinates, and real-time animation techniques in Python.

## Key Concepts

- Homogeneous coordinate transformation
- Rotation matrix around the Y-axis
- Color interpolation using linear blending
- 3D object rendering with `Poly3DCollection`
- Animation using `FuncAnimation`

## Technologies Used

- Python 3.10+
- matplotlib
- numpy
- mpl_toolkits.mplot3d
- matplotlib.animation

## Setup & Installation

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Script

```bash
python main.py
```

