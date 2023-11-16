import cv2 as cv
img = cv.imread("../Downloads/people_1.jpg")

# Converting image to the Grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# Simple tresholding
threshold, thresh = cv.threshold(gray_img, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple thresholding", thresh)

threshold_inv, thresh_inv = cv.threshold(gray_img, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple thresholding inverse", thresh_inv)


# Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                       cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive thresholding", adaptive_thresh)

adaptive_thresh_inv = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                       cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("Adaptive thresholding inverse", adaptive_thresh_inv)


adaptive_thresh_gaus = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive thresholding Gaussian", adaptive_thresh_gaus)



cv.waitKey(0)