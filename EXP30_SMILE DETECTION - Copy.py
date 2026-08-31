import cv2

# Read the image
image = cv2.imread("smile.jpg")

# Load Haar Cascade classifiers
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

smile_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.3,
    minNeighbors=5
)

smile_count = 0

# Process each detected face
for (x, y, w, h) in faces:

    # Draw rectangle around face
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (255, 0, 0),
        2
    )

    # Select lower part of face where mouth/smile is located
    roi_gray = gray[y + int(h * 0.5):y + h, x:x + w]
    roi_color = image[y + int(h * 0.5):y + h, x:x + w]

    # Detect smile
    smiles = smile_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.7,
        minNeighbors=20
    )

    # Draw rectangle around detected smile
    for (sx, sy, sw, sh) in smiles:

        cv2.rectangle(
            roi_color,
            (sx, sy),
            (sx + sw, sy + sh),
            (0, 255, 0),
            2
        )

        smile_count += 1

# Display result
cv2.imshow("Smile Detection", image)

print("Number of smiles detected:", smile_count)

# Wait for key press
cv2.waitKey(0)
cv2.destroyAllWindows()
