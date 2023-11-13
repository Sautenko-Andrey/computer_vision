import cv2 as cv
import numpy as np
path_img = "../Downloads/people_3.jpg"

img = cv.imread(path_img)
img = cv.resize(img, (int(img.shape[1] * .75), int(img.shape[0] * .75)))

# Creating a blank image
blank = np.zeros(img.shape[:2], dtype="uint8")

# Splitting image in blue, green and red
b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

merged = cv.merge([b,g,r])

# cv.imshow("Blue", b)
# cv.imshow("Green", g)
# cv.imshow("Red", r)
# cv.imshow("Merged", merged)
# cv.imshow("Custom img", blank)
cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)


cv.waitKey(0)