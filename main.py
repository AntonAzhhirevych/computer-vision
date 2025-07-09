import cv2
import numpy as np
import datetime

# Load the pre-trained MobileNet SSD model
prototxt_path = "mobilenet_ssd/MobileNetSSD_deploy.prototxt"
model_path = "mobilenet_ssd/MobileNetSSD_deploy.caffemodel"
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# Class labels
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

# Open video file
video_path = "data/camera.mov"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video file.")
    exit()

# Initialize video writer to save output
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter('results/tracking_output.mp4', fourcc, fps, (width, height))

# Prepare logging
log_file = open("results/tracking_log.txt", "w")

# Read the first frame
ret, frame = cap.read()
if not ret:
    print("Error: Cannot read the first frame.")
    cap.release()
    exit()

(h, w) = frame.shape[:2]
blob = cv2.dnn.blobFromImage(frame, 0.007843, (300, 300), 127.5)
net.setInput(blob)
detections = net.forward()

# Select the first detected person
target_box = None
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.3:
        idx = int(detections[0, 0, i, 1])
        if CLASSES[idx] == "person":
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            target_box = (startX, startY, endX - startX, endY - startY)
            break

if target_box is None:
    print("Error: No person found to track.")
    cap.release()
    exit()

tracker = cv2.TrackerCSRT_create()
tracker.init(frame, target_box)

frame_counter = 0
skip_rate = 3  # Skip some frames to reduce lag

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_counter += 1
    if frame_counter % skip_rate != 0:
        continue

    success, box = tracker.update(frame)
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    if success:
        x, y, w, h = map(int, box)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(frame, "Tracking", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        log_file.write(f"[{timestamp}] ✅ Tracking at [{x},{y},{w},{h}]\n")
    else:
        cv2.putText(frame, "Lost", (20, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        log_file.write(f"[{timestamp}] ❌ Lost tracking\n")

    out.write(frame)
    cv2.imshow("Person Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
log_file.close()
cv2.destroyAllWindows()
