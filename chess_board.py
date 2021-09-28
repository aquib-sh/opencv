import numpy
import cv2


# Create an empty white canvas
img = numpy.full((800,800,3), 255, dtype=numpy.uint8)
rows, columns, channels = img.shape
print(rows, columns, channels)

# Intervals for patching
hinterval = 100 # height
winterval = 100 # width

# Switching for changing from black patch to white patch
alternate = False

# Create a black box to apply
patch = numpy.full((hinterval, winterval, 3), 
    0, dtype=numpy.uint8)

# Apply the patches
for i in range(0, rows, hinterval):
    hend = i+hinterval
    if (hend > rows): break

    for j in range(0, columns, winterval):
        wend = j+winterval
        if (wend > columns): break
       
        # If not alternate then add black patch
        # or else keep the existing white board color
        if not (alternate):
            img[i:i+hinterval, j:j+winterval] = patch

        # Flip alternate
        alternate = not alternate

    # Again flip alternate for next row
    # if 1st row has black on 1st column 
    # then 2nd row will have white on 1st column
    alternate = not alternate


# Display image
cv2.imshow("Chess board", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
