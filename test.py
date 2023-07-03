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
    #gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    #b,g,r = cv2.split(resized_frame)
    #green_frame = g

    blur_frame=cv2.medianBlur(resized_frame,11)
    canny_frame=cv2.Canny(blur_frame,95,100)
    #blue_frame=cv2.HoughLinesP(blue_frame, 2, np.pi/180,150, None,50,10)
    #kernel = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
    #total_frame = cv2.filter2D(canny_frame, -1, kernel)
    #thresh = cv2.inRange(resized_frame, (50, 10, 50), (0, 255 , 0))
    cv2.imshow('Frame', canny_frame)

    if cv2.waitKey(33) & 0xFF == ord('q'): 
        break 
  else: 
    break

capture.release()
 

cv2.destroyAllWindows()