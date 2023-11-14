import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread("../Downloads/barsik.jpeg")

# Creating a mask
blank = np.zeros(img.shape[:2], dtype="uint8")
circle = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2 - 180), 150, (255, 255, 255), -1)


# Converting to Grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

mask = cv.bitwise_and(gray_img, gray_img, mask=circle)
cv.imshow("Mask", mask)

cv.imshow("Grayscale cat", gray_img)

# Computing grayscale histogram
gray_hist = cv.calcHist([gray_img], [0], mask, [256], [0, 256])

# Plotting
plt.figure()
plt.title("Grayscale histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()


# Colour histogram
img2 = cv.imread("../Downloads/people_1.jpg")
cv.imshow("People", img2)

blank2 = np.zeros(img2.shape[:2], dtype="uint8")
mask2 = cv.circle(blank2, (img2.shape[1] // 2, img2.shape[0] // 2), 150, (255, 255, 255), -1)
masked = cv.bitwise_and(img2, img2, mask = mask2)
cv.imshow("masked people", masked)

colors = ('b', 'g', 'r')
plt.figure()
plt.title("Colour histogram for people")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
for i, col in enumerate(colors):
    hist = cv.calcHist([img2], [i], mask2, [256], [0, 256])
    plt.plot(hist,color = col)
    plt.xlim([0, 256])
plt.show()


cv.waitKey(0)