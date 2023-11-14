import cv2 as cv
import numpy as np

img = cv.imread("../Downloads/barsik.jpeg")

cv.imshow("Cat", img)


# Creating a blank
blank = np.zeros(img.shape[:2], dtype="uint8")
blank2 = blank.copy()


# Creating masks.
# Draw circle on the blank.
mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2 - 160), 130, (255, 255, 255), -1)
# Draw rectangle on the blank.
mask_2 = cv.rectangle(blank2, (100, 100), (200, 200), 255, -1)


# Creating masked images
masked_img = cv.bitwise_and(img, img, mask=mask)
masked_img_2 = cv.bitwise_and(img, img, mask=mask_2)

# Displaying results
cv.imshow("Masked img", masked_img)
cv.imshow("Masked img 2", masked_img_2)

cv.waitKey(0)
