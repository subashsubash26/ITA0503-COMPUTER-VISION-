import cv2

def add_text_to_image():

    # Read the image
    image = cv2.imread("input.jpg")

    # Check whether image was loaded
    if image is None:
        print("Error: Image not found!")
        return

    # Get text from user
    text = input("Enter the text to display on the image: ")

    # Set text position
    position = (50, 100)

    # Set font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Set font size
    font_scale = 1

    # Set text color - Blue (BGR)
    color = (255, 0, 0)

    # Set thickness
    thickness = 2

    # Add text to image
    cv2.putText(
        image,
        text,
        position,
        font,
        font_scale,
        color,
        thickness,
        cv2.LINE_AA
    )

    # Display the image
    cv2.imshow("Image with Text", image)

    # Save the output image
    cv2.imwrite("output.jpg", image)

    # Wait for key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call the function
add_text_to_image()
