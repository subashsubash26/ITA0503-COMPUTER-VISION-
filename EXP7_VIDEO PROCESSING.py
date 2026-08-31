import cv2
import time

# Load the captured video
cap = cv2.VideoCapture("captured_video.mp4")  # Replace with your video file name

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

print("Press:")
print("n - Normal Speed")
print("s - Slow Motion")
print("f - Fast Motion")
print("q - Quit")

speed = "normal"

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video Playback", frame)

    # Set playback speed
    if speed == "normal":
        delay = 30          # Normal speed
    elif speed == "slow":
        delay = 100         # Slow motion
    elif speed == "fast":
        delay = 10          # Fast motion

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('n'):
        speed = "normal"
    elif key == ord('s'):
        speed = "slow"
    elif key == ord('f'):
        speed = "fast"
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
