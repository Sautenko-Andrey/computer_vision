import cv2 as cv

path_img = "../Downloads/people_1.jpg"
path_video = "../Downloads/dance.mp4"

def read_img() -> None:
    '''Reading and displaying image'''

    #open
    img = cv.imread(path_img)

    #display
    cv.imshow("People", img)

    #infinitive display
    cv.waitKey(0)

#read_img()

def read_video() -> None:
    '''Read and display video'''

    video = cv.VideoCapture(path_video)

    #reading video frame by frame using infinitive loop
    while True:
        isTrue, frame = video.read()

        #displaying every single frame
        cv.imshow("Video", frame)

        #for stopping playing video
        if cv.waitKey(20) & 0xFF == ord("d"):
            break

        #release the video device
        #video.release()

        #destroy all windows since we don't need them anymore
        #cv.destroyAllWindows()

read_video()