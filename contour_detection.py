import cv2 as cv
import numpy as np
path_img = "../Downloads/people_2.jpg"

img = cv.imread(path_img)

#next step - converting to the grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#blurring
blured_img = cv.GaussianBlur(img_gray, (3,3), cv.BORDER_DEFAULT)

#next is grabbing edge of the img
img_canny = cv.Canny(blured_img,125, 175)


#getting contours and hierarchies
contours, hierarchies = cv.findContours(img_canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

#creating img from zero
canvas = np.zeros((img.shape),  dtype='uint8')
cv.drawContours(canvas,contours, -1, (150, 255, 150), thickness=1)

cv.imshow("Original img", img)
cv.imshow("Canny img", img_canny)
cv.imshow("Drawed img", canvas)


cv.waitKey(0)