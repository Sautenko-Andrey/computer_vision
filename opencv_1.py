import cv2

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

    #покажем новое измененнное изображение
    cv2.imshow("Resized image",new_img)

    cv2.waitKey(0)

correct_img(path, (500, 500))