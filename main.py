import cv2
import os
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt

# Create results directory if it doesn't exist ===
os.makedirs("results", exist_ok=True)

# Load input images ===
img1 = cv2.imread("data/test_image_1.jpg")
img2 = cv2.imread("data/test_image_2.jpg")

if img1 is None or img2 is None:
    raise FileNotFoundError("❌ One or both input images not found.")

# Resize second image to match the first
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Convert to grayscale ===
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Compute SSIM and difference image
score, diff = ssim(gray1, gray2, full=True)
print(f"🔍 Structural Similarity Index (SSIM): {score:.4f}")

# Highlight differences
diff = (diff * 255).astype("uint8")
thresh = cv2.threshold(diff, 230, 255, cv2.THRESH_BINARY_INV)[1]
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Copy images for drawing differences
img1_marked = img1.copy()
img2_marked = img2.copy()

for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(img1_marked, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(img2_marked, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Save result images
cv2.imwrite("results/image1_marked.jpg", img1_marked)
cv2.imwrite("results/image2_marked.jpg", img2_marked)
cv2.imwrite("results/diff_map.jpg", diff)
cv2.imwrite("results/thresh_map.jpg", thresh)

# Display results
plt.figure(figsize=(10, 6))
plt.subplot(1, 3, 1)
plt.title("Image 1 (Marked)")
plt.imshow(cv2.cvtColor(img1_marked, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Image 2 (Marked)")
plt.imshow(cv2.cvtColor(img2_marked, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Difference Map")
plt.imshow(thresh, cmap='gray')
plt.axis("off")

plt.tight_layout()
plt.savefig("results/comparison_summary.png")
plt.show()
