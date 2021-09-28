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

    canvas = numpy.ones(frame.shape, dtype=numpy.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    canvas[:height//2, :width//2] = cv2.rotate(
            smaller_frame, cv2.cv2.ROTATE_180) # upper left

    canvas[height//2:, :width//2] = smaller_frame # lower left
    canvas[:height//2, width//2:] = smaller_frame # upper right
    canvas[height//2:, width//2:] = cv2.rotate(
            smaller_frame, cv2.cv2.ROTATE_180) # lower right

    #cv2.imshow("Video", canvas)
    cv2.imshow("Video", cv2.rotate(frame, cv2.cv2.ROTATE_180))

    if cv2.waitKey(1) == ord('q'): 
        break


cap.release()
cv2.destroyAllWindows()

