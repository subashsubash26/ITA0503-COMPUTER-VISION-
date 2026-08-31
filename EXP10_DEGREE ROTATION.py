import cv2

# Read the input image
image = cv2.imread("image.jpg")   # Replace with your image file name

# Check if image is loaded
if image is None:
    print("Error: Image not found.")
    exit()

# Rotate the image 90 degrees clockwise
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Display the original and rotated images
cv2.imshow("Original Image", image)
cv2.imshow("90 Degree Clockwise Rotated Image", rotated_image)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
