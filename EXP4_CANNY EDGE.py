from google.colab import files
import cv2
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

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges using Canny function
    edges = cv2.Canny(blur, 100, 200)

    # Display Original Image
    plt.figure(figsize=(6,6))
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")
    plt.show()

    # Display Edge Detected Image
    plt.figure(figsize=(6,6))
    plt.imshow(edges, cmap='gray')
    plt.title("Canny Edge Detection")
    plt.axis("off")
    plt.show()
