import cv2
import numpy as np

def create_rectangle():

    # Get image size from user
    height = int(input("Enter image height: "))
    width = int(input("Enter image width: "))

    # Create a white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Rectangle coordinates
    x1 = width // 4
    y1 = height // 4
    x2 = 3 * width // 4
    y2 = 3 * height // 4

    # Draw a blue rectangle
    cv2.rectangle(
        image,
        (x1, y1),
        (x2, y2),
        (255, 0, 0),
        3
    )

    # Display the image
    cv2.imshow("Rectangle", image)

    # Save the image
    cv2.imwrite("rectangle.jpg", image)

    # Wait for a key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call the function
create_rectangle()
