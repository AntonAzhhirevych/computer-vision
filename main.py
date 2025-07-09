import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os

# Create folder for results
os.makedirs("results", exist_ok=True)

# Define image paths
image_paths = {
    "low": "data/low.png",     # Sentinel image
    "high": "data/high.png"    # Google Maps image
}

# Load image from file
def load_image(path):
    return cv2.imread(path)

# Apply K-means clustering to enhance color separation
def apply_kmeans_clustering(image, k=3):
    reshaped = image.reshape((-1, 3)).astype(np.float32)
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
    labels = kmeans.fit_predict(reshaped)
    clustered = kmeans.cluster_centers_[labels].reshape(image.shape).astype(np.uint8)
    return clustered

# Generate mask for Sentinel images using HSV color distance
def generate_low_res_mask(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, w = hsv.shape[:2]
    center_region = hsv[h // 2 - 20:h // 2 + 20, w // 2 - 20:w // 2 + 20]
    ref_color = np.mean(center_region.reshape(-1, 3), axis=0)
    distance = np.linalg.norm(hsv.astype(np.float32) - ref_color.astype(np.float32), axis=2)
    mask = (distance < 30).astype(np.uint8) * 255
    return mask

# Generate mask for Google Maps images using CLAHE and thresholding
def generate_high_res_mask(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    v_channel = hsv[:, :, 2]
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(v_channel)
    blurred = cv2.medianBlur(enhanced, 5)
    _, binary_mask = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return binary_mask

# Apply morphological operations to refine mask
def refine_mask(binary_mask):
    kernel = np.ones((5, 5), np.uint8)
    opened = cv2.morphologyEx(binary_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel, iterations=2)
    return closed

# Filter contours and keep only the one nearest to center with largest area for low-res images
def filter_contours(mask_img, image_type, original_image=None):
    contours, _ = cv2.findContours(mask_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return []

    h, w = mask_img.shape[:2]
    cx, cy = w // 2, h // 2

    if image_type == "low":
        closest_contour = None
        min_dist = float('inf')
        for cnt in contours:
            M = cv2.moments(cnt)
            if M['m00'] == 0:
                continue
            x = int(M['m10'] / M['m00'])
            y = int(M['m01'] / M['m00'])
            dist = np.sqrt((x - cx)**2 + (y - cy)**2)
            if dist < min_dist:
                min_dist = dist
                closest_contour = cnt
        return [closest_contour] if closest_contour is not None else []

    else:
        valid_contours = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 6000:
                continue
            perimeter = cv2.arcLength(cnt, True)
            circularity = 4 * np.pi * (area / (perimeter ** 2 + 1e-6))
            if circularity < 0.8:
                valid_contours.append(cnt)
        if not valid_contours:
            return []
        return [max(valid_contours, key=cv2.contourArea)]

# Draw contours on image
def draw_contours(image, contours):
    result_image = image.copy()
    cv2.drawContours(result_image, contours, -1, (255, 0, 255), 2)
    return result_image

# Complete image processing pipeline
def process_image(image_path, image_type):
    original = load_image(image_path)
    clustered = apply_kmeans_clustering(original, k=3)
    cv2.imwrite(f"results/{image_type}_kmeans.png", clustered)

    if image_type == "low":
        mask = generate_low_res_mask(clustered)
    else:
        mask = generate_high_res_mask(clustered)

    cleaned_mask = refine_mask(mask)
    contours = filter_contours(cleaned_mask, image_type, original)
    result_image = draw_contours(original, contours)

    cv2.imwrite(f"results/{image_type}_mask.png", cleaned_mask)
    cv2.imwrite(f"results/{image_type}_result.png", result_image)

    return original, clustered, cleaned_mask, result_image

# Run processing on both images
low_image, low_clustered, low_mask, low_result = process_image(image_paths["low"], "low")
high_image, high_clustered, high_mask, high_result = process_image(image_paths["high"], "high")

# Visualization
fig, axs = plt.subplots(2, 4, figsize=(16, 8))
for i, (orig, cluster, mask, result, label) in enumerate([
    (low_image, low_clustered, low_mask, low_result, "Sentinel"),
    (high_image, high_clustered, high_mask, high_result, "Google")
]):
    axs[i][0].imshow(cv2.cvtColor(orig, cv2.COLOR_BGR2RGB))
    axs[i][0].set_title(f"{label} – Original")
    axs[i][1].imshow(cv2.cvtColor(cluster, cv2.COLOR_BGR2RGB))
    axs[i][1].set_title(f"{label} – K-Means")
    axs[i][2].imshow(mask, cmap='gray')
    axs[i][2].set_title(f"{label} – Mask")
    axs[i][3].imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    axs[i][3].set_title(f"{label} – Detected Lake")
    for ax in axs[i]:
        ax.axis("off")

plt.tight_layout()
plt.savefig("results/lake_detection_with_clustering.png")
plt.show()
