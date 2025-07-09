import cv2
import torch
import numpy as np
import sys
import os

# YOLOv5 path
FILE = os.path.abspath(__file__)
YOLO_V5_PATH = os.path.join(os.path.dirname(FILE), "yolov5")
sys.path.append(YOLO_V5_PATH)

# Import YOLOv5 utilities
from models.common import DetectMultiBackend
from utils.torch_utils import select_device
from utils.augmentations import letterbox
from utils.general import non_max_suppression, scale_boxes

# Load YOLOv5 model
device = select_device('cpu')
model_path = 'model/best.pt'
model = DetectMultiBackend(model_path, device=device, dnn=False)
stride, names = model.stride, model.names
print("Loaded model with classes:", names)

# Open video file
cap = cv2.VideoCapture("data/helmet_test_1.mp4")
if not cap.isOpened():
    print("Cannot open video")
    exit()

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess frame
    img = letterbox(frame, 640, stride=stride, auto=True)[0]
    img = img.transpose((2, 0, 1))[::-1]
    img = np.ascontiguousarray(img)
    img_tensor = torch.from_numpy(img).to(device).float() / 255.0
    if img_tensor.ndimension() == 3:
        img_tensor = img_tensor.unsqueeze(0)

    # Inference
    with torch.no_grad():
        pred = model(img_tensor, augment=False, visualize=False)
        pred = non_max_suppression(pred, conf_thres=0.4, iou_thres=0.45)

    if pred[0] is not None and len(pred[0]):
        pred[0][:, :4] = scale_boxes(img_tensor.shape[2:], pred[0][:, :4], frame.shape).round()

        for *xyxy, conf, cls in pred[0]:
            label = names[int(cls)].lower().strip()
            if label == 'no helmet':
                x1, y1, x2, y2 = map(int, xyxy)
                color = (0, 0, 255)
                text = "No Helmet"
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, text, (x1, max(y1 - 10, 0)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Show result
    cv2.imshow("Helmet Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
