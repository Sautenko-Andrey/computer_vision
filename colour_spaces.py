import cv2 as cv
import matplotlib.pyplot as plt
path_img = "../Downloads/people_2.jpg"



img = cv.imread(path_img)
img = cv.resize(img, (650, 500))


# 1. BGR convert to Grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 2. BGR to HSV
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# 3. BGR to LAB
lab_img = cv.cvtColor(img, cv.COLOR_BGR2LAB)

# 4. BGR to RGB
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

#we can convert vice versa, except  Grayscale to HSV directly, we can do it
# in the following way: Grayscale --> BGR --> HSV

#HSV to BGR
hsv_to_bgr = cv.cvtColor(hsv_img, cv.COLOR_HSV2BGR)



# cv.imshow("Img", img)
# cv.imshow("Gray Img", gray_img)
# cv.imshow("HSV Img", hsv_img)
# cv.imshow("LAB Img", lab_img)
# plt.imshow(rgb_img)
# plt.show()
cv.imshow("HSV to BGR Img", hsv_to_bgr)

cv.waitKey(0)

