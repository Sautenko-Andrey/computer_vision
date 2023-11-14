import cv2 as cv
import numpy as np

# Creating a blank
blank = np.zeros((400, 400), dtype="uint8")

# Drawing a rectangle
rectangle = cv.rectangle(blank.copy(), (30, 30),(370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, (255, 255, 255), -1)


cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)



# 1. Bitwise AND  ----> finds intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("AND", bitwise_and)


# 2. Bitwise OR -----> finds non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("OR", bitwise_or)

# 3. Bitwise XOR    ----> finds non-intersecting regions
bitwise_XOR = cv.bitwise_xor(rectangle, circle)
cv.imshow("XOR", bitwise_XOR)

# 4. Bitwise NOT   ----> inverts binary colour
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("NOT", bitwise_not)

cv.waitKey(0)
