import cv2
import numpy as np

def subtract_background():

    # Read the input image
    image = cv2.imread("input.jpg")

    if image is None:
        print("Error: Image not found!")
        return

    # Convert BGR image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Set background color range
    # Example: green background
    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])

    # Create mask for the background color
    mask = cv2.inRange(hsv, lower, upper)

    # Remove the background
    result = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))

    # Display original image
    cv2.imshow("Original Image", image)

    # Display background mask
    cv2.imshow("Background Mask", mask)

    # Display image after background subtraction
    cv2.imshow("Background Subtracted", result)

    # Save result
    cv2.imwrite("background_subtracted.jpg", result)

    # Wait for key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call the function
subtract_background()
