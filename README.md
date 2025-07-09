### Computer Vision & Object Detection Projects

A collection of practical projects focused on computer vision, real-time object detection, 2D/3D graphics transformations, and image processing using Python and deep learning frameworks.


Technologies & Tools (Python 3.10+ ,OpenCV, NumPy, Matplotlib, YOLOv5 (PyTorch), scikit-image, Ultralytics tools)

## Branches

Each branch in this repository represents a standalone project focused on a specific topic within computer vision, object detection, or graphical rendering.

### `01-basic-graphics-python`

**Exploring the Basic Graphical Capabilities of Python**

This branch demonstrates how to create layered 2D shapes, render symmetrical logo-like figures using triangles, and visualize mathematical signals. The project is built entirely with native Python libraries like `matplotlib`, `numpy`, and `math`, making it ideal for understanding fundamental graphical operations without using external engines.

### `02-coordinate-transformations-2d-3d`

**Study of Coordinate Construction and Transformations for 2D and 3D Objects**

This branch focuses on the creation and transformation of 2D and 3D geometric objects using homogeneous coordinates and transformation matrices. It includes an animated 3D triangular-based pyramid with real-time rotation, color interpolation, and opacity blending—providing insight into practical 3D graphics implementation with `matplotlib` and `numpy`.

### `03-raster-image-processing`

**Exploring Algorithms for Raster Image Formation and Processing**

This branch investigates foundational techniques for working with raster-based digital images. It includes pixel-level operations, filtering, histogram-based adjustments, and basic enhancement methods using OpenCV, NumPy, and matplotlib. Ideal for learning how raw image data can be manipulated, analyzed, and visualized programmatically.

### `04-image-enhancement-cv`

**Image Enhancement Techniques for Computer Vision Tasks**

This branch focuses on improving the quality of digital images to optimize them for computer vision workflows. It demonstrates a complete pipeline including color correction (HSV equalization), contrast enhancement (global and local histograms), noise reduction, automatic thresholding, morphological filtering, and contour detection. Suitable for preprocessing satellite, aerial, or general-purpose images in segmentation and recognition tasks.

### `05-image-segmentation-clustering`

**Segmentation and Clustering Techniques for Object Detection in Imagery**

This branch explores techniques for segmenting and isolating objects—specifically lakes—from satellite and map imagery. It combines K-means clustering with adaptive preprocessing pipelines for both low-resolution (Sentinel) and high-resolution (Google Maps) images. The pipeline uses color space transformations, CLAHE, contour filtering, and morphological operations to produce clean segmentation masks and visual overlays.

### `06-object-tracking-video`

**Object Tracking in Video Using Image Comparison and Detection**

This branch presents a practical pipeline that integrates object detection and visual tracking to monitor a person across video frames. It uses MobileNet SSD to detect the initial person in the frame and OpenCV’s CSRT tracker to follow their motion throughout the video. The pipeline logs tracking events, highlights position changes, and outputs a processed video, making it suitable for surveillance demos or foundational research in video-based tracking.

### `07-object-identification-cv`

**Object Identification on Digital Images Using YOLOv5**

This branch demonstrates real-time object identification using a custom-trained YOLOv5 model. The pipeline is optimized to detect safety violations—specifically the absence of helmets—in both webcam streams and video files. It uses a local clone of the YOLOv5 repository, processes each frame with high accuracy, and visually highlights the detections. Ideal for safety compliance, industrial monitoring, and edge-device deployment scenarios.