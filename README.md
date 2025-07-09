# 3D Reconstruction from Stereo Images Using OpenCV

This project demonstrates the generation of a 3D point cloud from a stereo image pair using disparity mapping techniques. It utilizes OpenCV’s `StereoSGBM` algorithm to compute depth information and reprojects it into 3D space for visualization and export.

## Overview

The pipeline performs the following steps:

1. Loads a **grayscale stereo image pair** (`left` and `right`)
2. Computes the **disparity map** using `StereoSGBM`
3. Converts disparity to **3D point cloud** using a Q-matrix
4. Saves the point cloud in `.xyz` format
5. Displays the disparity map as a color-coded heatmap

## Technologies Used

- Python 3.10+
- OpenCV
- NumPy
- Matplotlib


## Setup & Installation

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```


