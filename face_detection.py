import cv2 as cv

img = cv.imread("../Downloads/sheldon.jpeg")
img2 = cv.imread("../Downloads/group.jpeg")

# Converting to the grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# Creating a haarcascade variable
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# Detecting a face on the image
face_rectangle = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=3)
face_rectangle2 = haar_cascade.detectMultiScale(gray_img2, scaleFactor=1.1, minNeighbors=1)

print(f"Number of faces found = {len(face_rectangle)}")
print(f"Number of faces found  = {len(face_rectangle2)}")

# Drawing a rectangle on that face(s)
for(x,y,w,h) in face_rectangle:
    cv.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0),thickness=3)

for(x,y,w,h) in face_rectangle2:
    cv.rectangle(img2, (x,y), (x + w, y + h), (0, 255, 0),thickness=2)



cv.imshow("Detected face", img)
cv.imshow("Detected faces", img2)
# cv.imshow("Grayscale Sheldon", gray_img)
cv.waitKey(0)