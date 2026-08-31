import cv2

# Read the input image
image = cv2.imread("input.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Set threshold values
lower_threshold = 100
upper_threshold = 200

# Segment the image based on threshold values
segmented = cv2.inRange(
    gray,
    lower_threshold,
    upper_threshold
)

# Display original image
cv2.imshow("Original Image", image)

# Display segmented image
cv2.imshow("Segmented Image", segmented)

# Save the segmented image
cv2.imwrite("segmented.jpg", segmented)

# Wait for a key press
cv2.waitKey(0)
cv2.destroyAllWindows()
