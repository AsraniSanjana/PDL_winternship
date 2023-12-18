import torch
import cv2
import numpy as np

area=[]

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

cap=cv2.VideoCapture('traffic.mp4')   # pre recorded video
# cap = cv2.VideoCapture(0) # using real time camera



model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
count=0
while True:
    ret,frame=cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    
    frame=cv2.resize(frame,(1020,500))


    print("Current area array:", area)

    if len(area) >= 3:
        # Draw the polygon
        cv2.polylines(frame, [np.array(area, np.int32)], True, (0, 0, 255), 2)

    
    results = model(frame) # for full screen obj detection
    # results = model(roi)



    for index, row in results.pandas().xyxy[0].iterrows():
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])

        d=(row['name'])   #person class/label
        print(d)

        # below code is only for poly lines 53-
        cx=int(x1+x2)//2  #center pt of a obj: (cx,cy) if inside roi, get detected
        cy=int(y1+y2)//2
        results=cv2.pointPolygonTest(np.array(area, np.int32),((cx,cy)), False)
        print(results)
        # if results==-1: boundary , 1:inside
        if results>=0:
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2) # for full screen
            cv2.putText(frame, str(d), (x1,y1), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
            cv2.circle(frame,(cx,cy),5,(255,0,0),-1) # fill my circle w solid color: -1

    cv2.polylines(frame,[np.array(area, np.int32)], True, (0,0,255),2) # 2 is thickness

        # cv2.rectangle(roi,(x1,y1),(x2,y2),(0,255,0),2)  # for my selected roi
    cv2.imshow("ROI",frame)
    if cv2.waitKey(1)&0xFF==27:
#  u can see the coordinates as the mouse changes position
# waitkey 0 means pause at a certain frame


        break
cap.release()
cv2.destroyAllWindows()