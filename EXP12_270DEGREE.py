import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Rotate image by 270° clockwise (90° counterclockwise)
    rotated = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Convert BGR to RGB for display
    original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)

    # Display images
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.imshow(original_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.imshow(rotated_rgb)
    plt.title("270° Clockwise Rotated Image")
    plt.axis("off")

    plt.show()
