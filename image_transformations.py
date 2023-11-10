import cv2 as cv
import numpy as np

path_img = "../Downloads/people_1.jpg"

img = cv.imread(path_img)

# 1. Translation

def translateIMG(img: np.ndarray, x: int | float, y: int | float) -> np.ndarray:

    '''
    -x --> left
    -y --> Up
    x --> Right
    y --> Down
    '''

    #translation matrix
    trans_matrix = np.float32( [ [1, 0, x], [0, 1, y] ] )

    #getting dimensions of image
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, trans_matrix, dimensions)

translated_img = translateIMG(img, 300, 300)


# 2. Rotation

def rotate(img: np.ndarray, angle: int | float, rotation_point: tuple = None) -> np.ndarray:

    #getting size
    (height, width) = img.shape[:2]

    #default coordinats of rotation point
    if rotation_point is None:
        rotation_point = (width // 2, height // 2)

    #rotation matrix
    rotation_matrix = cv.getRotationMatrix2D(rotation_point,angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img,rotation_matrix,dimensions)

rotated_img = rotate(img,45)


# 3. Resizing
resized_img = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)


# 4. Flipping

flipped_img = cv.flip(img,0)  #vertically
flipped_img2 = cv.flip(img,1)  #horizontally
flipped_img3 = cv.flip(img,-1)  #both


# 5. Cropping

cropped_img = img[0:150, 0:img.shape[0]]



cv.imshow("Original img", img)
cv.imshow("Translated img", translated_img)
cv.imshow("Rotated img", rotated_img)
cv.imshow("Resized img", resized_img)
cv.imshow("Vertically flipped img", flipped_img)
cv.imshow("Horizontally flipped img", flipped_img2)
cv.imshow("Both way flipped img", flipped_img3)
cv.imshow("Cropped img", cropped_img)

cv.waitKey(0)