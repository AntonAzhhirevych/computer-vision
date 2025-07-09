import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure
import os

# Create folder for results
os.makedirs("results", exist_ok=True)

# 1. Load image
image_path = "data/image.png"
img = cv2.imread(image_path)

# 2. Color correction (convert to HSV and enhance saturation)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv[:, :, 1] = cv2.equalizeHist(hsv[:, :, 1])  # enhance saturation
color_corrected = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# 3. Convert to grayscale
gray = cv2.cvtColor(color_corrected, cv2.COLOR_BGR2GRAY)

# 4. Global histogram (intensity rescaling)
gray_global = exposure.rescale_intensity(gray)

# 5. Local histogram correction (CLAHE)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
gray_clahe = clahe.apply(gray_global)

# 6. Build brightness histogram
plt.figure()
plt.hist(gray.ravel(), bins=256, range=[0, 256], color='gray')
plt.title("Histogram of grayscale image")
plt.xlabel("Pixel value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("results/histogram.png")
plt.show()

# 7. Filtering (median)
filtered = cv2.medianBlur(gray_clahe, 5)

# 8. Thresholding
_, mask = cv2.threshold(filtered, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 9. Morphology (opening + closing)
kernel = np.ones((5, 5), np.uint8)
opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)

# 10. Contour detection
contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 11. Area-based filtering
min_area = 5000
field_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

# Contour statistics output
areas = [cv2.contourArea(cnt) for cnt in field_contours]
print("Fields detected:", len(field_contours))
print("Average area:", np.mean(areas) if areas else "None")

# 13. Visualization
contour_img = img.copy()
cv2.drawContours(contour_img, field_contours, -1, (0, 255, 0), 2)

# 14. Save results
cv2.imwrite("results/enhanced.png", gray_clahe)
cv2.imwrite("results/mask.png", closed)
cv2.imwrite("results/contours.png", contour_img)

# Show results
titles = ['Original', 'Contrast Enhancement', 'Mask', 'Contours']
images = [img, gray_clahe, closed, contour_img]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()