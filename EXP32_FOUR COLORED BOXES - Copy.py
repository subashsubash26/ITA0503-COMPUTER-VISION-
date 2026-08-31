import cv2
import numpy as np

def create_image():

    # Get image size from user
    height = int(input("Enter image height: "))
    width = int(input("Enter image width: "))

    # Create a white image
    image = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Box size = 1/10th of image size
    box_height = height // 10
    box_width = width // 10

    # Black box - Top Left
    image[0:box_height, 0:box_width] = [0, 0, 0]

    # Blue box - Top Right
    image[0:box_height, width-box_width:width] = [255, 0, 0]

    # Green box - Bottom Left
    image[height-box_height:height, 0:box_width] = [0, 255, 0]

    # Red box - Bottom Right
    image[height-box_height:height, width-box_width:width] = [0, 0, 255]

    # Display the image
    cv2.imshow("Four Colored Boxes", image)

    # Save the image
    cv2.imwrite("colored_boxes.jpg", image)

    # Wait for key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call the function
create_image()
