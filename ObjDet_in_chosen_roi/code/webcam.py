import cv2

# Function to display webcam feed
def display_webcam():
    cap = cv2.VideoCapture(0)  # Use '0' for the default webcam device

    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Webcam not available")
            break

        cv2.imshow("Webcam Feed", frame)  # Display the frame in a local environment

        # Press 'q' to exit the webcam display
        key = cv2.waitKey(1)
        if key == ord('q') or key == 27:  # 'q' or Esc key
            break
    
    cap.release()
    cv2.destroyAllWindows()

display_webcam()
