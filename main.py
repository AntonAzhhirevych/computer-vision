import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load stereo pair
imgL = cv2.imread('data/im0.png', cv2.IMREAD_GRAYSCALE)
imgR = cv2.imread('data/im1.png', cv2.IMREAD_GRAYSCALE)

# StereoSGBM parameters
stereo = cv2.StereoSGBM_create(
    minDisparity=0,
    numDisparities=16*5,
    blockSize=9,
    P1=8*3*9**2,
    P2=32*3*9**2,
    disp12MaxDiff=1,
    uniquenessRatio=10,
    speckleWindowSize=100,
    speckleRange=32
)

# Compute disparity map
disparity = stereo.compute(imgL, imgR).astype(np.float32) / 16.0

# Show disparity
plt.imshow(disparity, cmap='plasma')
plt.colorbar()
plt.title("Disparity Map")
plt.show()

# Q-matrix
Q = np.float32([
    [1, 0, 0, -imgL.shape[1]/2],
    [0, -1, 0, imgL.shape[0]/2],
    [0, 0, 0, -1000],  # focal length (approx.)
    [0, 0, 1, 0]
])

# Reconstruct 3D
points_3D = cv2.reprojectImageTo3D(disparity, Q)
mask = disparity > disparity.min()
output = points_3D[mask]

# Save
np.savetxt("results/point_cloud.xyz", output.reshape(-1, 3), fmt="%.2f")
plt.savefig("results/disparity_map.png")
print("✅ Point cloud saved.")
