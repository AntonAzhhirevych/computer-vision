# Animated 2D Triangle with Transformation Pipeline in Python

This project visualizes a 2D triangle undergoing a sequence of geometric transformations—scaling, rotation, and translation—while cyclically changing its fill color. The animation is implemented using homogeneous coordinates and rendered with `matplotlib`.

## Overview

The animation demonstrates:

- **Scaling**: Uniform size change with bouncing effect between limits
- **Rotation**: Continuous angular rotation around the triangle center
- **Translation**: Constant shift applied on each frame
- **Color transition**: Smooth cyclical switch through a predefined color palette

The transformations follow this pipeline:

Scale → Rotate → Translate

## Key Concepts

- Homogeneous coordinates for affine transformations
- Matrix multiplication order and composition
- Dynamic animation using `FuncAnimation`
- Color control and polygon manipulation with `matplotlib`

## Technologies Used

- Python 3.10+
- `matplotlib`
- `numpy`

## Setup & Installation

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

