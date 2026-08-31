import cv2
import numpy as np

# Read the input image
image = cv2.imread("image.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary threshold
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Create a 5x5 structuring element
kernel = np.ones((5,5), np.uint8)

# Perform Opening operation
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary)
cv2.imshow("Opening Result", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
