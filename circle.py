import numpy
import cv2


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    circle = cv2.circle(frame, 
            (width//2, height//2),      #centre coord
            100,             #radius
            (255, 0, 0), # circle
            -1               #thickness, -1 means fill entirely
        )

    cv2.imshow("Image with rect", circle)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

