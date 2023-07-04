import cv2
import numpy as np
 
def open_file(file_path):
  capture = cv2.VideoCapture(file_path)
  return capture
 

def video_processing(frame):
    resized_frame = cv2.resize(frame, (1000, 600))
    blur_frame=cv2.medianBlur(resized_frame, 15)
    thresh_frame = cv2.inRange(blur_frame, (100, 50, 0), (180, 180 , 100))

    #cv2.HoughLinesP(image, rho, theta, threshold, lines, minLineLength, maxLineGap) 
    lines=cv2.HoughLinesP(thresh_frame, 2, np.pi/180, 175, None, 10, 20)

    try:
      for line in lines:
          line = line[0]
          cv2.line(resized_frame, (line[0],line[1]), (line[2],line[3]), (0,0,255), 3)  
    except: pass

    return resized_frame, thresh_frame
