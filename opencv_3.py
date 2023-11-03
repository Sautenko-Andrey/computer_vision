
import cv2
import numpy as np

path = "../Downloads/chaus.mp4"
#path2 = "/home/andrey/Downloads/my_video.mp4"


def video_process(path:str):
    """Обработка видео по примеру обработки изображения"""

    video = cv2.VideoCapture(path)

    #делаем бесконечный цикл отображения видео на экране
    while True:
        #читаем видео по кадрам
        success, img = video.read()

        #к каждому кадру добавим эффект размытия
        img = cv2.GaussianBlur(img, (9,9), 0)

        #преобразуем каждый кадр в серый
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #далее получаем углы каждого кадра
        img = cv2.Canny(img, 30, 30)

        # создадим матрицу со значениями 1 типа uint8
        kernel = np.ones((5, 5), np.uint8)

        #уменьшаем углы
        img = cv2.dilate(img, kernel, iterations=1)

        #увеличиваем углы
        img = cv2.erode(img, kernel, iterations=1)


        cv2.imshow("My video", img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

video_process(path)

