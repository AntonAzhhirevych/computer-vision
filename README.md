# Geometric Drawing & Signal Visualization in Python

This project explores basic graphical capabilities of Python using `matplotlib`, `numpy`, and simple math to create layered geometric figures, logo-like patterns, and signal plots.

## Overview

The script includes three independent tasks:

### Task 1: Layered Geometric Figures

Draws two overlapping sets of layered shapes:
- Concentric circles (left side)
- Nested equilateral triangles (right side)

Each layer is colored using a preset palette to create a visually appealing pattern.

### Task 2: Logo Construction with Triangles

Builds a symmetrical logo composed of 4 isosceles triangles rotated at 90° intervals.

- Supports both **outline-only** and **filled** rendering
- Can be rendered in **monochrome** or **color mode**

### Task 3: Signal Plotting

Visualizes mathematical functions:
- Three individual signals: `sin(x)`, `cos(x)` with varying amplitudes
- One combined plot for comparison

Useful for understanding waveform behavior and signal envelopes.

## Technologies Used

- Python 3.10+
- matplotlib
- numpy
- math

## Setup & Installation

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```


## Running the Script

Simply run the script to execute all tasks:

```bash
python main.py
```
