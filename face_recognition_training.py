import cv2 as cv
import os
import numpy as np

players = ["havertz", "martinelli", "odegaard", "rice", "saka"]

DIR = "../faces"

# Creating a haarcascade variable for face detection
haar_cascade = cv.CascadeClassifier("haar_face.xml")

features = []    # Features of each img
labels = []      # labels of each player

def create_train() -> None:
    """Prepearing a data for face recognition.
    Goes inside each folder in the list , fetches faces features
    and aliases it with particular labels. """

    for player in players:
        path = os.path.join(DIR, player)  # Path to every folder
        label = players.index(player)     # Label

        for img in os.listdir(path):
            img_path = os.path.join(path, img)    # Path to every image in the folder

            # Reading img via cv2
            img_array = cv.imread(img_path)

            # Converting image to a grayscale
            gray_img = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # Creating a face rectangle (face detection)
            faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=4)

            # Looping over ever faces in rect
            for(x, y, w, h) in faces_rect:

                # Grabbing basis region of interest (bassically cropping out the face in the image)
                faces_roi = gray_img[y:y + h, x:x + w]

                # Appending cropped faces in features list
                features.append(faces_roi)

                # Appending label to labels folder
                labels.append(label)


create_train()

# print(f"Length of the features: {len(features)}")
# print(f"Length of the labels: {len(labels)}")

# Creating a faces recognizer
face_recognizer = cv.face.LBPHFaceRecognizer.create()

# Convertin feature and label lists into NumPy list
features = np.array(features, dtype="object")
labels = np.array(labels)

# Train the recognizer on the features and labels lists
face_recognizer.train(features, labels)

print("\nTrainig done!\n")

# Saving trained face recognizer
face_recognizer.save("face_trained_recognizer.yml")

# Saving features and labels list
np.save("features.npy", features)
np.save("labels.npy", labels)



