import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Crop Region of Interest (ROI)
    roi = image[50:200, 50:200]

    # Copy the ROI
    roi_copy = roi.copy()

    # Paste the ROI into another location
    image[220:370, 220:370] = roi_copy

    # Convert BGR to RGB for display
    original_rgb = cv2.cvtColor(cv2.imread("image.jpg"), cv2.COLOR_BGR2RGB)
    roi_rgb = cv2.cvtColor(roi_copy, cv2.COLOR_BGR2RGB)
    modified_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display images
    plt.figure(figsize=(15,5))

    plt.subplot(1,3,1)
    plt.imshow(original_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1,3,2)
    plt.imshow(roi_rgb)
    plt.title("Cropped ROI")
    plt.axis("off")

    plt.subplot(1,3,3)
    plt.imshow(modified_rgb)
    plt.title("Image After Copy & Paste")
    plt.axis("off")

    plt.show()
