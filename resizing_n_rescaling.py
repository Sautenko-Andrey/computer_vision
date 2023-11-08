import cv2 as cv

path_video = "../Downloads/dance.mp4"
path_img = "../Downloads/people_1.jpg"

def rescaleFrame(frame, scale = 0.75):
    '''Scales frame'''

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def read_N_scale_video() -> None:
    '''Read , scale and display video'''

    video = cv.VideoCapture(path_video)

    #reading video frame by frame using infinitive loop
    while True:
        isTrue, frame = video.read()

        resized_frame = rescaleFrame(frame, scale=.20)

        #displaying every single frame
        cv.imshow("Original Video", frame)

        #displaying resized frame
        cv.imshow("Resized video", resized_frame)

        #for stopping playing video
        if cv.waitKey(20) & 0xFF == ord("d"):
            break

        #release the video device
        #video.release()

        #destroy all windows since we don't need them anymore
        #cv.destroyAllWindows()

#read_N_scale_video()


def read_N_scale_img() -> None:
    '''Reed, scale and display image'''

    #open
    img = cv.imread(path_img)

    #resized img
    resizes_img = rescaleFrame(img, scale=.5)

    #display
    cv.imshow("Original People", img)
    cv.imshow("Resized People", resizes_img)

    #infinitive display
    cv.waitKey(0)

# read_N_scale_img()

#method for live-video
def changeRes(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)
    capture.set()
