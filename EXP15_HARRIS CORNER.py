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

    # Convert to float32
    gray = np.float32(gray)

    # Apply Harris Corner Detection
    corners = cv2.cornerHarris(gray, 2, 3, 0.04)

    # Dilate corner points
    corners = cv2.dilate(corners, None)

    # Mark detected corners in red
    image[corners > 0.01 * corners.max()] = [0, 0, 255]

    # Convert BGR to RGB for display
    result = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the result
    plt.figure(figsize=(6,6))
    plt.imshow(result)
    plt.title("Harris Corner Detection")
    plt.axis("off")
    plt.show()
