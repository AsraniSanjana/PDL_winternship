# Copyright 2021 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Utility functions to display the pose detection results."""

import cv2
import numpy as np
from tracker import*
import cvzone

_MARGIN = 10  # pixels
_ROW_SIZE = 10  # pixels
_FONT_SIZE = 1
_FONT_THICKNESS = 2
_TEXT_COLOR = (255, 0, 0)  # red
tracker=Tracker()
area=[(236,164),(251,183),(275,178), (258,165)]
# area=[(22, 200) , (1270, 200)]   # for upside
area1_c=set()   # area1: first: bottom to up walking people, lhs polygon
# area=[(250, 298), (401, 299), (402, 328), (257, 334)]
area2=[(303,221),(315,248),(340,234),(325,209)]
# area2=[(790, 43), (876, 42), (880, 80), (799, 82)]   
# area2=[(22, 200) , (1270, 200)]  # for downside
area2_c=set()   # area2: second: up to down walking people, rhs polygon
def visualize(
    image: np.ndarray,
    detection_result,
) -> np.ndarray:
  """Draws bounding boxes on the input image and return it.

  Args:
    image: The input RGB image.
    detection_result: The list of all "Detection" entities to be visualize.

  Returns:
    Image with bounding boxes.
  """
  list=[]
  for detection in detection_result.detections:
    # Draw bounding_box
    bbox = detection.bounding_box
    start_point = bbox.origin_x, bbox.origin_y
    end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
    x,y=start_point
    x1,y1=end_point
    list.append([x,y,x1,y1])
    
  
    # Draw label and score
    category = detection.categories[0]
    category_name = category.category_name

    # if 'person' in category_name: 
    #   list.append([x,y,x1,y1])
    #   cv2.rectangle(image, (x,y),(x1,y1), (0,0,255), 3) 
    # print(category_name) #class label objname
    probability = round(category.score, 2)
    result_text = category_name + ' (' + str(probability) + ')'
    text_location = (_MARGIN + bbox.origin_x, _MARGIN + _ROW_SIZE + bbox.origin_y)
  bbox_idx=tracker.update(list)
  for bbox in bbox_idx:
      x2,y2,x3,y3,id=bbox
      cx=int(x2+x3)//2
      cy=int(y2+y3)//2
      results1=cv2.pointPolygonTest(np.array(area,np.int32),((cx,cy)),False)   #centroid for lhs area
      if results1>=0:
         cv2.circle(image,(cx,cy),4,(255,0,255),-1)
         cv2.rectangle(image,(x2,y2),(x3,y3),(0,255,0),2)
         cv2.putText(image, str(id), (x2,y2), cv2.FONT_HERSHEY_PLAIN,
                _FONT_SIZE, _TEXT_COLOR, _FONT_THICKNESS),area1_c.add(id)
      results=cv2.pointPolygonTest(np.array(area2,np.int32),((x3,y3)),False)   #bottom right for rhs
      if results>=0:
         cv2.circle(image,(x3,y3),4,(255,0,255),-1)
         cv2.rectangle(image,(x2,y2),(x3,y3),(0,255,0),2)
         cv2.putText(image, str(id), (x2,y2), cv2.FONT_HERSHEY_PLAIN, _FONT_SIZE, _TEXT_COLOR, _FONT_THICKNESS)
         area2_c.add(id)
  a=(len(area2_c))
  b=(len(area1_c))
  # print("#people moving down: "+str(a))
  # print("#people moving up: "+str(b))
  # cv2.rectangle(image, (x,y),(x1,y1), (0,0,255), 3) 
  cvzone.putTextRect(image, f'moving Up: {b}', (20, 174), 1, 3, (255, 255, 255), 2, cv2.LINE_AA)  # White text
  cvzone.putTextRect(image, f'moving Down: {a}', (20, 250), 1, 3, (255, 255, 255), 2, cv2.LINE_AA)  # White text


  cv2.polylines(image,[np.array(area,np.int32)],True,(255,0,0),2)

  cv2.polylines(image,[np.array(area2,np.int32)],True,(255,0,0),2)
  return image
