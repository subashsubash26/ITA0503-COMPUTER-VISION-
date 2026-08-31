import cv2
import pytesseract

def extract_text_from_video(video_path):

    # Open the video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open video!")
        return

    # Create a text file to store extracted text
    output_file = open("extracted_text.txt", "w")

    frame_number = 0

    while True:

        # Read a frame
        ret, frame = cap.read()

        if not ret:
            break

        frame_number += 1

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to improve OCR
        _, threshold = cv2.threshold(
            gray, 150, 255, cv2.THRESH_BINARY
        )

        # Extract text using Tesseract
        text = pytesseract.image_to_string(threshold)

        # Store detected text
        if text.strip():
            output_file.write(
                "Frame " + str(frame_number) + ":\n"
            )
            output_file.write(text)
            output_file.write("\n")

            print("Frame", frame_number, ":", text.strip())

        # Display video frame
        cv2.imshow("Video", frame)

        # Press Q to stop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Close everything
    cap.release()
    output_file.close()
    cv2.destroyAllWindows()

    print("Text extraction completed.")
    print("Text saved in extracted_text.txt")


# Call the function
extract_text_from_video("input.mp4")
