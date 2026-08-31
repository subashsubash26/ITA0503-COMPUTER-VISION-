import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Sobel filter in X direction
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

    # Apply Sobel filter in Y direction
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # Compute Sobel magnitude
    sobel = cv2.magnitude(sobel_x, sobel_y)

    # Convert to uint8
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)
    sobel = cv2.convertScaleAbs(sobel)

    # Display images
    plt.figure(figsize=(12,8))

    plt.subplot(2,2,1)
    plt.imshow(gray, cmap='gray')
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(2,2,2)
    plt.imshow(sobel_x, cmap='gray')
    plt.title("Sobel X")
    plt.axis("off")

    plt.subplot(2,2,3)
    plt.imshow(sobel_y, cmap='gray')
    plt.title("Sobel Y")
    plt.axis("off")

    plt.subplot(2,2,4)
    plt.imshow(sobel, cmap='gray')
    plt.title("Sobel Edge Detection")
    plt.axis("off")

    plt.show()
