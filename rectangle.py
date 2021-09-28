import numpy
import cv2


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    rect = cv2.rectangle(frame, 
            (10, 10),       #coord of upper left
            (100,100),      #coord of lower right 
            (255, 0, 255),  #color
            -1              #thickness, -1 means fill entirely
        )

    cv2.imshow("Image with rect", rect)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

