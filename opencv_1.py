import cv2
import numpy as np

path = '../beerBot_DATA/pics/all_beers/001_edelburg_hefew.png'
video_path = "../Downloads/cars.mp4"

def load_img(path:str) -> None:
    """Загрузка и вывод на экран изображения
    с подписью"""

    #загрузка изображения
    my_img = cv2.imread(path)

    #показать изображение
    cv2.imshow("Edelburg Hefeweizen", my_img)

    #установим время отображения изображения в милисекундах
    cv2.waitKey(0)  # 0 в варгументе - бесконечный показ

def load_video(path:str) -> None:
    """Загрузка и вывод видео"""

    #открытие файла с видео
    video = cv2.VideoCapture(path)

    #создание бесконечного цикла для перебора кадров видео
    while True:
        success, img = video.read()  #success либо True лиюо False (успешно/неуспешно прочитано видео)
                                    #в img будет помещено текущее изображение
        cv2.imshow("My video", img)

        #условие выхода из цикла (в том числе нажатие клавишы q)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

#load_video(video_path)

def load_web_cam():
    '''Считывание видео с web-камеры'''

    #открытие файла
    web_video = cv2.VideoCapture(0)

    #задаем размер самого изображения
    web_video.set(3, 500)   #3 - это id ширирны(указывается любой id), 500 - размер ширины
    web_video.set(4, 350)  # 3 - это id высоты, 350 - размер высоты

    # создание бесконечного цикла для перебора кадров видео
    while True:
        success, img = web_video.read()  # success либо True лиюо False (успешно/неуспешно прочитано видео)
        # в img будет помещено текущее изображение
        cv2.imshow("My web-camera", img)

        # условие выхода из цикла (в том числе нажатие клавишы q)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break


#load_web_cam()


def correct_img(path:str, new_size:tuple) -> None:
    """Уменьшение изображения"""

    img = cv2.imread(path)

    #посмотрим на размер изображения
    print(f"Size : {img.shape[0]} x {img.shape[1]}")   #Size : 327 x 187

    #изменим размер изображения
    new_img = cv2.resize(img, new_size)

    #уменьшим оригинал пропорционально в 2 раза
    img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

    #покажем пропорционально уменьшенное изображение
    cv2.imshow("Small version",img)

    #покажем новое измененнное изображение
    cv2.imshow("Resized image",new_img)

    cv2.waitKey(0)

#correct_img(path, (500, 500))

def cut_img(path:str):
    """Обрезка изображения при выводе на экран с помощью срезов"""

    img = cv2.imread(path)

    #обрезка при выводе на экран
    cv2.imshow("Cutted image",img[0:50, 0:100])

    cv2.waitKey(0)

#cut_img(path)

def blur_img(path:str) -> None:
    """Размытие изображения"""


    img = cv2.imread(path)

    #(7,7) - на сколько сильным будет размытие
    blurred = cv2.GaussianBlur(img, (7,7), 0)

    cv2.imshow("blurred pic",blurred)

    cv2.waitKey(0)

#blur_img(path)

def img_to_gray(path:str) -> None:
    """Преобразование картинки в чб"""

    img = cv2.imread(path)

    #cv2.COLOR_BGR2GRAY - выбираем формат смены
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("in gray color", gray_img)
    cv2.waitKey(0)

#img_to_gray(path)

def find_corners(path:str) -> None:
    '''Нахождение углов изображения,
    то есть мы приводим изображение в
    бинарный формат(черно-белый)'''

    img = cv2.imread(path)

    #90 - пороги - это как точности определения всех обводок изображения
    res = cv2.Canny(img, 90 ,90)

    #попробуем другие пороги
    res2 = cv2.Canny(img, 30, 30)

    cv2.imshow("result",res)
    cv2.imshow("result 2", res2)  #тут точность обведения стала лучше (нужна большая точность - уменьшаем
                                            #значение порогов#)
    #создадим матрицу со значениями 1 типа uint8
    kernel = np.ones((5,5), np.uint8)

    #так же мы можем изменять ширину обводки(контура)
    #iterations - обоводка(количество обводок, чем больше, тем жирнее обводка)
    res3 = cv2.dilate(res, kernel, iterations= 1)

    cv2.imshow("With dilate", res3)

    #отменим обведение у предыдущего изображения
    res4 = cv2.erode(res3, kernel, iterations=1)

    cv2.imshow("without dilate", res4)
    cv2.waitKey(0)

find_corners(path)