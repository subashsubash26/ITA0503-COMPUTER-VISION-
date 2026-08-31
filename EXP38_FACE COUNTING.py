import cv2

def count_faces():

    # Read the input image
    image = cv2.imread("input.jpg")

    if image is None:
        print("Error: Image not found!")
        return

    # Load Haar Cascade face detector
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Count faces
    face_count = len(faces)

    # Draw rectangle around each detected face
    for (x, y, w, h) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    # Display number of faces on image
    cv2.putText(
        image,
        "Faces: " + str(face_count),
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    # Print result
    print("Number of faces detected:", face_count)

    # Display image
    cv2.imshow("Face Counting", image)

    # Save output
    cv2.imwrite("face_count.jpg", image)

    # Wait for key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call the function
count_faces()
