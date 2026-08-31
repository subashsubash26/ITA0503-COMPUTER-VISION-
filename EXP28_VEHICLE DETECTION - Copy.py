import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open the video
cap = cv2.VideoCapture("vehicles.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect objects in the current frame
    results = model(frame)

    # Process detected objects
    for result in results:
        boxes = result.boxes

        for box in boxes:
            # Get class ID
            class_id = int(box.cls[0])

            # Get confidence
            confidence = float(box.conf[0])

            # Vehicle classes in COCO dataset
            vehicle_classes = {
                2: "Car",
                3: "Motorcycle",
                5: "Bus",
                7: "Truck"
            }

            if class_id in vehicle_classes and confidence > 0.5:

                # Get bounding box coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Vehicle name
                name = vehicle_classes[class_id]

                # Draw rectangle
                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                # Display vehicle name and confidence
                label = f"{name}: {confidence:.2f}"

                cv2.putText(
                    frame,
                    label,
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

    # Display the frame
    cv2.imshow("Vehicle Detection", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
