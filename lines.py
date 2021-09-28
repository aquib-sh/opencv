# Capture multi video from webcam
# Display the frame 4 times on canvas

import numpy
import cv2

# 0 means 1st webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, 
            (0, 0), 
            (width, height), 
            (0,255,0), 
            10
        )

    cv2.imshow("Video", img)

    if cv2.waitKey(1) == ord('q'): 
        break


cap.release()
cv2.destroyAllWindows()

