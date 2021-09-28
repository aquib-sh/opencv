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
    line_color = (0, 0, 0)
    line_width = 5

    for i in range(0, width, 30):
        frame = cv2.line(frame, 
                (i, 0), 
                (i, height), 
                line_color, 
                line_width
            )
    
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) == ord('q'): 
        break


cap.release()
cv2.destroyAllWindows()

