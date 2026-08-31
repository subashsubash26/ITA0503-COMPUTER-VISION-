import cv2
import numpy as np

def subtract_foreground():

    # Read the input image
    image = cv2.imread("input.jpg")

    if image is None:
        print("Error: Image not found!")
        return

    # Convert BGR image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Set foreground color range
    # Example: red foreground
    lower = np.array([0, 100, 100])
    upper = np.array([10, 255, 255])

    # Create mask for the foreground color
    mask = cv2.inRange(hsv, lower, upper)

    # Extract the foreground
    foreground = cv2.bitwise_and(image, image, mask=mask)

    # Display original image
    cv2.imshow("Original Image", image)

    # Display foreground mask
    cv2.imshow("Foreground Mask", mask)

    # Display extracted foreground
    cv2.imshow("Foreground", foreground)

    # Save the result
    cv2.imwrite("foreground.jpg", foreground)

    # Wait for key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call the function
subtract_foreground()
