import cv2

ip = "192.168.0.1" 
port = 9060           
stream_url = f"http://{ip}:{port}/video"

# Open the video stream
cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("Error: Unable to open video stream.")
    exit()

# Display the video frames
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Show the frame in a window
    cv2.imshow("MJPEG Stream", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
