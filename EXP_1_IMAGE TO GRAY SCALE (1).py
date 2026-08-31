import cv2

# Read the image
image = cv2.imread('image.jpg')

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found.")
else:
    # Display the original image
    cv2.imshow("Original Image", image)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the grayscale image
    cv2.imshow("Grayscale Image", gray_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
