
# this code will only detect the objs in the specified area which is our roi. ref vid: https://youtu.be/xTH4g-W946Q?si=xCw3HSP0kHPPVeYU
import torch
import cv2
import numpy as np

def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('ROI')
cv2.setMouseCallback('ROI', POINTS)

cap=cv2.VideoCapture('vids/rampwalk.mp4')   # pre recorded video
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


#                                                                               ROI: RECTANGLE: 2PTS

    roi=frame[64:273,297:690]   # (297,64) (690,273) are the coords.. top left & bottom right
    results = model(frame) # for full screen obj detection
    # results = model(roi)  #for objs that fall in roi

#                                                                               ROI: POLY LINES

    # area=[(776,299),(713,353),(867,381),(985,355),(980,317),(776,299)]  #polygon
    area=[(164, 180), (311, 213), (282, 323), (150, 293)]     # our roi


    for index, row in results.pandas().xyxy[0].iterrows():
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])

        d=(row['name'])   #person class/label
        print(d)

        cx=int(x1+x2)//2  #center pt of a obj: (cx,cy) if inside roi, get detected
        cy=int(y1+y2)//2
        results=cv2.pointPolygonTest(np.array(area, np.int32),((cx,cy)), False)
        print(results)
        # if results==-1: boundary , 1:inside
        if results>=0:  #and d=='person'
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2) # for full screen, for roi replace 'frame' w roi.
            cv2.putText(frame, str(d), (x1,y1), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
            cv2.circle(frame,(cx,cy),5,(255,0,0),-1) # fill my circle w solid color: -1

    cv2.polylines(frame,[np.array(area, np.int32)], True, (0,0,255),2) # 2 is thickness

    cv2.imshow("ROI",frame)
    if cv2.waitKey(1)&0xFF==27:   # waitkey 0 means pause at a certain frame
#  u can see the coordinates as the mouse changes position
        break
cap.release()
cv2.destroyAllWindows()

# press esc to exit the pgm

'''

# this code will detect objs in the whole frame. ref vid: https://youtu.be/wsSNz1R3ej8?si=c_gfdYS7YvXvXCNw

import torch
import cv2
import numpy as np

def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        

cv2.namedWindow('ROI')
cv2.setMouseCallback('ROI', POINTS)

cap=cv2.VideoCapture('people.mp4')

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

    roi=frame[64:273,297:690]   # (297,64) (690,273) are the coords.. top left & bottom right
    results = model(frame) # for full screen obj detection
    # results = model(roi)  #for objs that fall in roi
                                            
    for index, row in results.pandas().xyxy[0].iterrows():
        x1 = int(row['xmin'])
        y1 = int(row['ymin'])
        x2 = int(row['xmax'])
        y2 = int(row['ymax'])

        d=(row['name'])   #person class/label
        print(d)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)



    cv2.imshow("ROI",frame)
    if cv2.waitKey(1)&0xFF==27: 
        break
cap.release()
cv2.destroyAllWindows()

# github repo link for boilerplate: https://github.com/freedomwebtech/roiinyolo
'''
