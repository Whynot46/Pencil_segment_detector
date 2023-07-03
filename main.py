import cv2
import numpy as np
 

file_path = './pencil.mp4'
capture = cv2.VideoCapture(file_path)
 
if (capture.isOpened()== False): 
  print("Error opening video stream or file")
 

while(capture.isOpened()):

  ret, frame = capture.read()
  if ret == True:

    resized_frame = cv2.resize(frame, (1000, 600))

    blur_frame=cv2.medianBlur(resized_frame,11)
    thresh = cv2.inRange(blur_frame, (65, 0, 0), (180, 200 , 80))

    LSD = cv2.createLineSegmentDetector(0)
    lines = LSD.detect(thresh)[0]
    drawn_img = LSD.drawSegments(resized_frame, lines)

    cv2.imshow('Original', resized_frame)
    cv2.imshow('Tresh', thresh)

    if cv2.waitKey(33) & 0xFF == ord('q'): 
        break 
  else: 
    break

capture.release()
cv2.destroyAllWindows()