# Object Tracking in Video Using MobileNet SSD & CSRT

This project demonstrates a hybrid object detection and tracking pipeline to monitor a person across video frames. It uses MobileNet SSD for initial person detection and OpenCV's CSRT tracker for real-time tracking throughout the video stream.

## Overview

The pipeline performs the following steps:

1. **Load and initialize** a pre-trained MobileNet SSD model.
2. **Detect the first person** in the video using object detection.
3. **Initialize tracking** with OpenCV’s CSRT algorithm.
4. **Track the person** across video frames while skipping some frames for efficiency.
5. **Log tracking events** (position or loss of tracking).
6. **Save the annotated video** and log file.

## Technologies Used

- Python 3.10+
- OpenCV (`cv2`)
- NumPy
- MobileNet SSD (Caffe model)
- CSRT Tracker (OpenCV)

## Setup & Installation

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

