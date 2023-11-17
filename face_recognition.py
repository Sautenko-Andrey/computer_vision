import cv2 as cv
import numpy as np

# Creating a haarcascade variable for face detection
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# Our list of folders with images
players = ["havertz", "martinelli", "odegaard", "rice", "saka"]

# Loading features amd labels files
# features = np.load("features.npy", allow_pickle= True)
# labels = np.load("labels.npy", allow_pickle= True)

# Creating a faces recognizer
face_recognizer = cv.face.LBPHFaceRecognizer.create()

# Reading trained file
face_recognizer.read("face_trained_recognizer.yml")

# Trying to recognize player
img = cv.imread("../Downloads/rice.jpeg")

# Converting image to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Player", gray_img)

# Detect the face in image
faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=4)

# Looping over faces in the image
for (x, y, w, h) in faces_rect:
    faces_roi = gray_img[y : y + h, x : x + h]

    # Prediction
    label, confidence = face_recognizer.predict(faces_roi)
    print(f"Label = {players[label]} with a confidence of {confidence}")

    # Putting text
    cv.putText(img, str(players[label]), (20,20), cv.FONT_HERSHEY_COMPLEX,
               1.0, (0, 255, 0), thickness=2)

    # Drawing a rectangle over the face
    cv.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), thickness=2)

# Displaying a result
cv.imshow("Detected face",img)

cv.waitKey(0)