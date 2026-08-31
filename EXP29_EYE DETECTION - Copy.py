import cv2

# Read the image
image = cv2.imread("eyes.jpg")

# Load Haar Cascade classifiers
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5
)

# Detect eyes inside each face
for (x, y, w, h) in faces:

    # Draw rectangle around face
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (255, 0, 0),
        2
    )

    # Region of interest for eyes
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

    # Detect eyes
    eyes = eye_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    # Draw rectangles around eyes
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(
            roi_color,
            (ex, ey),
            (ex + ew, ey + eh),
            (0, 255, 0),
            2
        )

# Display result
cv2.imshow("Eye Detection", image)

print("Number of eyes detected:", len(eyes) if len(faces) > 0 else 0)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()
