from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Read image
image = cv2.imread("watch.jpg")

# Perform object detection
results = model(image)

# Draw detections
output = results[0].plot()

# Display result
cv2.imshow("Watch Detection", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
