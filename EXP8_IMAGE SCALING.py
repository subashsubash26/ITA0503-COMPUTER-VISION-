import cv2
import numpy as np

# Read the input image
image = cv2.imread("image.jpg")   # Replace with your image file name

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Create a kernel (3x3)
kernel = np.ones((3, 3), np.uint8)

# Perform dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Display original and dilated images
cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated_image)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
