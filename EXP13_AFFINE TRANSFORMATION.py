import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    rows, cols = image.shape[:2]

    # Three points in the original image
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])

    # Corresponding points in the transformed image
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    # Compute affine transformation matrix
    matrix = cv2.getAffineTransform(pts1, pts2)

    # Apply affine transformation
    transformed = cv2.warpAffine(image, matrix, (cols, rows))

    # Convert BGR to RGB for display
    original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    transformed_rgb = cv2.cvtColor(transformed, cv2.COLOR_BGR2RGB)

    # Display images
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.imshow(original_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.imshow(transformed_rgb)
    plt.title("Affine Transformed Image")
    plt.axis("off")

    plt.show()
