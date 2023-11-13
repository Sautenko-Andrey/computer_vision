import cv2 as cv

img = cv.imread('../Downloads/barsik.jpeg')

# 1. Averaging
average = cv.blur(img, (3,3))

# 2. Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)

# 3. Median Blur
median = cv.medianBlur(img, 3)

# 4. Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)

cv.imshow("A Cat", img)
cv.imshow("Average Blur", average)
cv.imshow("Gaussian Blur", gauss)
cv.imshow("Median Blur", median)
cv.imshow("Bilateral Blur", bilateral)
cv.waitKey(0)