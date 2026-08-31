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

    # Display Original Image
    plt.figure(figsize=(6,6))
    plt.imshow(image_rgb)
    plt.title("Original Image")
    plt.axis("off")
    plt.show()

    # Plot Histogram for Blue, Green, and Red channels
    colors = ('b', 'g', 'r')

    plt.figure(figsize=(8,5))
    for i, color in enumerate(colors):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.grid()
    plt.show()
