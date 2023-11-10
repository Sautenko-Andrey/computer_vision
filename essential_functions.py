import cv2 as cv

path_img = "../Downloads/people_1.jpg"

img = cv.imread(path_img)
img = cv.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

# 1. Converting to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 2. Bluring image
blur_img = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)

# 3. Edge cascade
canny_img = cv.Canny(blur_img, 125, 175)

# 4. Dilating image
dilated_img = cv.dilate(canny_img, (3,3), iterations=3)

# 5. Eroding
eroded_img = cv.erode(dilated_img, (3,3), iterations=1)

# 6. Resize
resized_img = cv.resize(img, (550, 400), interpolation=cv.INTER_CUBIC)


# 7. Cropping
cropped_img = img[50:200, 200:400]


# cv.imshow("Original img", img)
# cv.imshow("Gray img", gray_img)
# cv.imshow("Blur img", blur_img)
# cv.imshow("Canny img", canny_img)
# cv.imshow("Dilated img", dilated_img)
# cv.imshow("Eroded img", eroded_img)
# cv.imshow("Resized img", resized_img)
cv.imshow("Cropped img", cropped_img)

cv.waitKey(0)