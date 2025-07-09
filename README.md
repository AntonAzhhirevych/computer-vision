# Image Comparison Using SSIM and Visual Difference Detection

This project demonstrates how to compare two digital images using the **Structural Similarity Index (SSIM)** and visualize the differences. It highlights areas of variation between two images and generates annotated results for analysis and reporting.

## Overview

The script performs the following steps:

1. Loads two images from the `data/` folder.
2. Converts both images to grayscale.
3. Computes the **SSIM score** and **difference map**.
4. Applies thresholding and contour detection to highlight differing regions.
5. Draws bounding boxes on the original images to mark changes.
6. Saves and visualizes the results.

## Key Concepts

- **SSIM (Structural Similarity Index):** A perceptual metric that quantifies image quality and similarity.
- **Difference Map Visualization:** Highlights pixel-wise differences.
- **Bounding Box Localization:** Uses contour detection to show exact regions where images differ.

## Technologies Used

- Python 3.10+
- OpenCV
- scikit-image
- Matplotlib

## ⚙Setup & Installation

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
