# ref: https://www.youtube.com/watch?v=KxdKcmarZjs&t=11s&pp=ygUkbGluZSBpbiBvdXIgPT10IGNvdW50ZXIgZnJlZWRvbSB0ZWNo
import torch
import cv2
import pandas as pd
from ultralytics import YOLO
from tracker import*
import cvzone

model = YOLO('yolov8s.pt')  # my pretrained model
# model = YOLO("yolov8x.pt")


def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        point = [x, y]
        print(point)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)
cap = cv2.VideoCapture('people.mp4')
# cap = cv2.VideoCapture(0)

# cap = cv2.VideoCapture(0)

my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")

count = 0
persondown = {}
tracker = Tracker()
counter1 = []

personup = {}
counter2 = []
# cy1 = 194   # line1 end y coord
# cy2 = 220
cy1=250
cy2=310
offset = 6

while True:
    ret, frame = cap.read()
    if not ret:
        break

    count += 1
    if count % 3 != 0:
        continue
    frame = cv2.resize(frame, (1250, 900))

    results = model.predict(frame)
    print(results)
    
    a = results[0].boxes.data
    print(a)
    px = pd.DataFrame(a).astype("float")
    print("\n")
    print("px"+str(px))

    list = []
    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        d = int(row[5])
        
        c = class_list[d]
        if 'person' in c:
            list.append([x1, y1, x2, y2])

    bbox_id = tracker.update(list)
    for bbox in bbox_id:
        x3, y3, x4, y4, id = bbox
        cx = int(x3 + x4) // 2  # center of the rectangle
        cy = int(y3 + y4) // 2
        cv2.circle(frame, (cx, cy), 4, (255, 0, 255), -1)

        if cy1 < (cy + offset) and cy1 > (cy - offset):
            cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 2)  # Red rectangle
            cvzone.putTextRect(frame, f'{id}', (x3, y3), 1, 2, (0, 0, 255))  # Red text
            # this only draws a rectangle only if the person has crossed the first green line 
            # if u want the objs to be detected only when, people from top are touching green line: if cy1<(cy+offset) and cy1>(cy-offset): up to down momement
            # if u want the objs to be detected (red boundary) only when, people from bottom are touching green line: if cy1>(cy+offset) and cy1>(cy-offset):  down to up movement 
            persondown[id] = (cx, cy)

        if id in persondown:
            if cy2 < (cy + offset) and cy2 > (cy - offset):
                cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 255, 255), 2)  # Yellow rectangle
                cvzone.putTextRect(frame, f'{id}', (x3, y3), 1, 2, (0, 255, 255))  # Yellow text
                    # so now when person crosses first line: red box
                    # when he crosses 2nd line: yellow box
                if counter1.count(id) == 0:
                    counter1.append(id)

        if cy2 < (cy + offset) and cy2 > (cy - offset):
            cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 2)  # Red rectangle
            cvzone.putTextRect(frame, f'{id}', (x3, y3), 1, 2, (0, 0, 255))  # Red text

            personup[id] = (cx, cy)

        if id in personup:
            if cy1 < (cy + offset) and cy1 > (cy - offset):
                cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 255, 255), 2)  # Yellow rectangle
                cvzone.putTextRect(frame, f'{id}', (x3, y3), 1, 2, (0, 255, 255))  # Yellow text
                    # so now when person crosses first line: red box
                    # when he crosses 2nd line: yellow box
                if counter2.count(id) == 0:
                    counter2.append(id)

    cv2.line(frame, (22, cy1), (1270, cy1), (0, 255, 0), 2)  # Upper green line
    cv2.line(frame, (30, cy2), (1370, cy2), (0, 255, 255), 2)  # Lower yellow line

    down = len(counter1)
    up = len(counter2)
    print(counter1)
    print(counter2)
    cvzone.putTextRect(frame, f'moving Up: {up}', (20, 174), 1, 3, (255, 255, 255), 2, cv2.LINE_AA)  # White text
    cvzone.putTextRect(frame, f'moving Down: {down}', (20, 250), 1, 3, (255, 255, 255), 2, cv2.LINE_AA)  # White text

    # how to tell dirn of a person?... only when a person has crossed the first line, the obj is counted
    cv2.imshow("Line_People Det_In Out Count", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
