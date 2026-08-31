import cv2
import time

def reverse_slow_motion(input_video):

    # Open the video
    cap = cv2.VideoCapture(input_video)

    if not cap.isOpened():
        print("Error: Cannot open video!")
        return

    # Store all frames
    frames = []

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    print("Total frames:", len(frames))

    # Play frames in reverse order
    for frame in reversed(frames):

        cv2.imshow("Reverse Slow Motion", frame)

        # Delay between frames
        # Increase this value for slower playback
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


# Call the function
reverse_slow_motion("input.mp4")
