import torch
import cv2
import numpy as np

def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

cv2.namedWindow('ROI')
cv2.setMouseCallback('ROI', POINTS)

cap = cv2.VideoCapture('vids/people.mp4')  # pre-recorded video

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    count = 0  # Reset count for each frame
    frame = cv2.resize(frame, (1020, 500))

    # ROI: RECTANGLE: 2PTS
    roi = frame[64:273, 297:690]

    results = model(frame)

    area = [(164, 180), (311, 213), (282, 323), (150, 293)]  # Our ROI

    for index, row in results.pandas().xyxy[0].iterrows():
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])

        cx = int((x1 + x2) / 2)  # center pt of an object
        cy = int((y1 + y2) / 2)

        results = cv2.pointPolygonTest(np.array(area, np.int32), ((cx, cy)), False)
        if results >= 0 and row['name'] == 'person':
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, str(row['name']), (x1, y1), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)
            cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)
            count += 1  # Increment the count for each person in the ROI

    cv2.polylines(frame, [np.array(area, np.int32)], True, (0, 0, 255), 2)

    # Display count above the red box
    count_text = f'People in ROI: {count}'
    cv2.putText(frame, count_text, (area[0][0], area[0][1] - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow("ROI", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

print("Object count in ROI:", count)
cap.release()
cv2.destroyAllWindows()
