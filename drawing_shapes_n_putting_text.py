import cv2 as cv
import numpy as np

#creating a blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("Blank", blank)

# 1. Paint the image certain colour
green_canvas = blank.copy()
green_canvas[:] = 0, 255, 0 #green
cv.imshow("Green Blank", green_canvas)

red_canvas = blank.copy()
red_canvas[:] = 0, 0, 255 #red
cv.imshow("Red Blank", red_canvas)

red_square = blank.copy()
red_square[125:275, 135:420] = 0, 0, 255  #red squere on the black canvas
cv.imshow("Red ob Black", red_square)


# 2. Draw a rectangle
rectangle = blank.copy()
cv.rectangle(rectangle, (125, 125), (255, 255), (255, 0, 0), thickness=2)
cv.imshow("Rectangle", rectangle)

# 3. Draw a circle
circle = blank.copy()
cv.circle(circle,(255, 255), 150, (125, 111, 228), thickness=-1)
cv.imshow("Circle", circle)

# 4. Draw a line
line = blank.copy()
cv.line(line,(10,10), (490,490), (51,115,115), thickness=4)
cv.imshow("Line", line)

# 5. Write text on image
text = blank.copy()
cv.putText(text, "Python", (255, 255), cv.FONT_HERSHEY_COMPLEX,
           1.0,(43, 34, 56), thickness=3)
cv.imshow("Text",text)

cv.waitKey(0)

