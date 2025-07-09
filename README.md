# Animated 3D Cube with Axonometric Projection in Python

This project demonstrates animated rendering of a 3D cube using axonometric projection. The cube smoothly scales in size and transitions through a continuous color spectrum, creating a visually engaging effect using only 2D plotting tools.

## Overview

The animation features:

- A **3D cube** rendered in 2D using **axonometric (isometric) projection**
- **Smooth scaling** animation centered on the cube
- **Dynamic color transitions** using HSV interpolation
- **Wireframe edges** for geometric clarity

This implementation simulates 3D behavior within a 2D environment using transformation matrices and homogeneous coordinates — perfect for exploring foundational concepts in 3D graphics.

## Key Concepts

- 3D object definition via vertex and face lists
- Homogeneous transformations and matrix multiplication
- Axonometric projection using rotation matrices (`Rx`, `Ry`)
- Uniform scaling with respect to object center
- Real-time animation with `FuncAnimation`
- HSV-to-RGB color cycling for smooth transitions

## Technologies Used

- Python 3.10+
- `matplotlib`
- `numpy`

## Setup & Installation

To run this animation:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Script

```bash
python3 main.py
```