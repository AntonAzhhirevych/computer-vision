# Image Enhancement & Contour Detection for Computer Vision

This project demonstrates a full pipeline for enhancing the quality of digital images and detecting significant contours, which can be useful for segmentation and feature extraction in computer vision tasks.

## Overview

The script processes a raster image through the following steps:

1. **Color correction** using HSV equalization
2. **Grayscale conversion**
3. **Global and local histogram enhancements** (contrast stretching & CLAHE)
4. **Noise reduction** via median filtering
5. **Automatic thresholding** using Otsu's method
6. **Morphological operations** (opening and closing)
7. **Contour detection** and **area filtering**
8. **Visualization and result saving**

The workflow is especially useful for improving input image quality before analysis or machine learning-based classification.

## Output Files

All outputs are saved in the `results/` folder:

- `enhanced.png` – CLAHE-enhanced grayscale image
- `mask.png` – Thresholded and morphologically processed binary mask
- `contours.png` – Original image with detected contours overlaid
- `histogram.png` – Histogram of grayscale intensity values

## Technologies Used

- Python 3.10+
- OpenCV (`cv2`)
- NumPy
- Matplotlib
- scikit-image (`exposure`)

## Setup & Installation

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
