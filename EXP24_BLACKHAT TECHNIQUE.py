import cv2
import numpy as np

# Read image
image = cv2.imread("image.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Perform Black Hat operation
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Black Hat Result", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
