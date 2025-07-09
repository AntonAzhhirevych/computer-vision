# Helmet Detection Using YOLOv5 and OpenCV

This project demonstrates real-time object identification on digital images using YOLOv5. It focuses on detecting workers without helmets from a webcam or video footage. The model is optimized to identify "no helmet" violations and provide visual feedback, making it suitable for safety compliance applications in industrial or construction environments.

## Overview

Two modes are available:

1. **Webcam mode** – real-time detection from a live camera stream
2. **Video file mode** – offline processing of recorded footage (e.g. `.mp4`)

In both cases, the script performs the following:
- Loads a custom-trained YOLOv5 model
- Runs detection on each frame
- Draws bounding boxes around "no helmet" cases
- Displays the annotated video stream in real-time

## Key Features

- Uses **YOLOv5** for fast and accurate object detection
- Compatible with both **webcam** and **video file** input
- Highlights detected "no helmet" instances in **red**
- Fully customizable and lightweight

## Technologies Used

- Python 3.10+
- OpenCV
- PyTorch
- YOLOv5 (local clone)
- NumPy



## Setup & Installation

```bash
# Clone YOLOv5 repo (if not already present)
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt

# Go back to project root
cd ..

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

