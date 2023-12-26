# run this code to get the coords of area/roi u want to do objdet in 
import torch
import cv2
import numpy as np

area = []  # Initialize empty list for storing polygon points

def POINTS(event, x, y, flags, param):
    global area

    if event == cv2.EVENT_LBUTTONDOWN:
        # Left mouse button click - add the clicked point to the area array
        area.append((x, y))
        print("Selected point:", (x, y))
        
        # Print the current area array
        print("Current area array:", area)

        if len(area) > 1:
            # Draw a line connecting the last two points
            cv2.line(frame, area[-2], area[-1], (0, 0, 255), 2)

        # If the polygon is closed (at least 3 points), draw the last line connecting the first and last points
        if len(area) >= 3:
            cv2.line(frame, area[-1], area[0], (0, 0, 255), 2)

cv2.namedWindow('ROI')
cv2.setMouseCallback('ROI', POINTS)

cap = cv2.VideoCapture('people.mp4')  # pre-recorded video
# cap = cv2.VideoCapture(0) # using real-time camera

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue

    frame = cv2.resize(frame, (1020, 500))

    print("Current area array:", area)

    if len(area) >= 1:
        # Draw the polygon
        cv2.polylines(frame, [np.array(area, np.int32)], True, (0, 0, 255), 2)

    cv2.imshow("ROI", frame)
    key = cv2.waitKey(int(1000 / 30))  # Set the delay for 30 frames per second


    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
