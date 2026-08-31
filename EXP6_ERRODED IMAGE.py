from google.colab import files
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Upload Image
uploaded = files.upload()

# Step 2: Get uploaded file name
filename = list(uploaded.keys())[0]

# Step 3: Read the image
image = cv2.imread(filename)

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert BGR to RGB for display
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Step 4: Create a kernel
    kernel = np.ones((5,5), np.uint8)

    # Step 5: Apply Erosion
    eroded_image = cv2.erode(image_rgb, kernel, iterations=1)

    # Step 6: Display Original Image
    plt.figure(figsize=(6,6))
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")
    plt.show()

    # Step 7: Display Eroded Image
    plt.figure(figsize=(6,6))
    plt.imshow(eroded_image)
    plt.title("Eroded Image")
    plt.axis("off")
    plt.show()
