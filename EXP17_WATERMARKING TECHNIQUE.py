import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Create a copy of the image
    watermark = image.copy()

    # Add text watermark
    text = "WATERMARK"
    cv2.putText(watermark, text, (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                2, (255, 255, 255), 3)

    # Blend original image and watermark
    output = cv2.addWeighted(image, 0.8, watermark, 0.2, 0)

    # Convert BGR to RGB for display
    original_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

    # Display images
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.imshow(original_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.imshow(output_rgb)
    plt.title("Watermarked Image")
    plt.axis("off")

    plt.show()
