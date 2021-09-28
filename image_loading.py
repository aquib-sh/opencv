import os 
import sys
import random
import cv2

path = 'sample.jpeg'

if not os.path.exists(path):
    print(f"{path} does not exist.")

img = cv2.imread(path)
img2 = img.copy()
img3 = img.copy()

# Shape of Image
rows, columns, channels = img.shape
print("Height:", rows)
print("Width:", columns)
print("Channels:", channels)


# Middle Pixel
mid_row = len(img)//2
mid_col = mid_row//2
mid_pixel = img[mid_row][mid_col]
print("Value of middle pixel:", end=" ")
print(mid_pixel)

# Change all pixels from middle row
# This will create a kind of line in middle
# with random color pixels
for i in range(0, columns):
    blue  = random.randint(0, 255)
    green = random.randint(0, 255)
    red   = random.randint(0, 255)
    img[mid_row][i] = [blue, green, red]

# Put black pixels randomly in the image
for i in range(0, rows):
    for j in range(0, columns):
        if random.randint(0, 1):
            img2[i][j] = [0,0,0]

# Put white pixels randomly in the image
for i in range(0, rows):
    for j in range(0, columns):
        if random.randint(0, 1):
            img3[i][j] = [255, 255, 255]


# Now display the images
cv2.imshow("Line in centre", img)
cv2.imshow("Black pixels randomly", img2)
cv2.imshow("White pixels randomly", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
