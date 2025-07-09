# Image Segmentation & Clustering for Lake Detection

This project explores segmentation and clustering techniques to identify and isolate lakes from satellite imagery. It uses different strategies for low-resolution (Sentinel) and high-resolution (Google Maps) images to build a flexible and automated detection pipeline suitable for computer vision applications.

## Overview

The script performs the following steps for both image types:

1. **Load input image** (Sentinel or Google Maps)
2. **Color clustering** using K-means (k=3) to reduce noise and enhance class separation
3. **Mask generation** using HSV color distance (for Sentinel) or CLAHE + thresholding (for Google Maps)
4. **Morphological processing** (opening and closing) to clean up masks
5. **Contour filtering** based on geometry and context
6. **Contour visualization** over the original image
7. **Side-by-side visualization** of all processing steps

## Techniques Used

- K-Means clustering with `sklearn`
- HSV-based color masking
- CLAHE (Contrast Limited Adaptive Histogram Equalization)
- Median filtering and Otsu thresholding
- Morphological operations (`cv2.morphologyEx`)
- Contour filtering by position, area, and circularity
- Visualization with `matplotlib`

## Technologies Used

- Python 3.10+
- OpenCV
- NumPy
- Matplotlib
- scikit-learn

## Setup & Installation

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```