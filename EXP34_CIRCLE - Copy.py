import cv2
import numpy as np

def create_circle():

    # Get image size from user
    height = int(input("Enter image height: "))
    width = int(input("Enter image width: "))

    # Create a white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Find the center of the image
    center_x = width // 2
    center_y = height // 2

    # Set radius
    radius = min(height, width) // 4

    # Draw a blue circle
    cv2.circle(
        image,
        (center_x, center_y),
        radius,
        (255, 0, 0),
        3
    )

    # Display the image
    cv2.imshow("Circle", image)

    # Save the image
    cv2.imwrite("circle.jpg", image)

    # Wait for a key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call the function
create_circle()
