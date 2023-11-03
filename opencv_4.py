"""Функции трансформации изображений"""
import cv2
import numpy as np

pic_path = "../Downloads/mbappe.jpeg"

def reflect_pic(path:str = pic_path) -> None:
    '''Отражение изображения по горизонтали,
    вертикали и одновременно по вертикали и горизонтали'''

    img = cv2.imread(path)

    # уменьшим оригинал пропорционально в 2 раза
    img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))


    #отзеркалим по горизонтали
    img_2 = cv2.flip(img, 1)

    #отразим по вертикали
    img_3 = cv2.flip(img, 0)

    #отразим и по вертикали и по горизонтали
    img_4 = cv2.flip(img, -1)


    cv2.imshow("Original",img)
    # cv2.imshow("horizont reflect", img_2)
    # cv2.imshow("vertical reflect", img_3)
    # cv2.imshow("all reflects", img_4)
    cv2.waitKey(0)

# reflect_pic()

def rotate_pic(angle, path: str = pic_path):
    '''Вращение изображения'''

    img = cv2.imread(path)

    # уменьшим оригинал пропорционально в 2 раза
    img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

    #получим размеры изображения
    height, width = img.shape[:2]

    #создадим точку вращения нашего изображения в середине самого изображения
    #будущее вращение будет происходить относительно центра изображения
    point = (width // 2, height // 2)

    #создадим матрицу, засчет которой мы будем делать вращение
    #1 - изображение никак не увеличивается при вращении
    #чтобы изображение увеличивалось в 2 раза при вращенни, то выбираем 2
    matrix = cv2.getRotationMatrix2D(point, angle, 1)

    return cv2.warpAffine(img, matrix, (width, height))

# img = rotate_pic(90, pic_path)
# cv2.imshow("Rotated img", img)
# cv2.waitKey(0)

def biasing_pic(x,y,path:str = pic_path):
    """Смещение изображения
    По бокам будут черные полосы"""

    img = cv2.imread(path)

    #создадим матрицу через numpy
    #каждый элемент матрицы будет вещественным числом
    matrix = np.float32([ [1, 0, x], [0, 1 , y] ])

    return cv2.warpAffine(img, matrix, (img.shape[1], img.shape[0]))

# img = biasing_pic(30, 45, pic_path)
# cv2.imshow("biased pic", img)
# cv2.waitKey(0)

def search_contours(path:str = pic_path):
    """Нахождение контуров изображения"""

    img = cv2.imread(path)

    # уменьшим оригинал пропорционально в 2 раза
    img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

    # нарисуем с помощью полученных контуров картинку
    new_img = np.zeros(img.shape, dtype="uint8")

    #задаем серый цвет
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #немного размоем изображение, чтобы сгладить углы(уменьшить кол-во контуров)
    img = cv2.GaussianBlur(img, (5,5), 0)

    #далее найдем края
    #после нахождения краев мы уже сможем найти контуры
    #находим края
    #второй аргумент означает, к примеру если 100 - то
    #все цвета, что ниже 100 , они будут проигнорированы и их значение будет
    #установлено как 0, то есть черное
    #а третий аргументы 140 - все цвета, которые больше 140 будут проигнорированы
    #и приведены к 255, то есть белые точки
    img = cv2.Canny(img,100, 140)

    #далее находим контуры в этом изображении
    #в переменную contours вернется список со всеми контурами
    #в переменную hierarchies вернется иерархия самих объектов
    #RETR_LIST - означает, что мы будм получать полностью все доступные контуры
    #CHAIN_APPROX_NONE - будут найдены абсолютно все координаты всех контуров
    contours, hierarchies = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    print(contours)

    #продолжим рисование картинку по полученным контурам
    cv2.drawContours(new_img, contours, -1, (275, 111, 34), thickness=1)

    cv2.imshow("New image", new_img)


    cv2.waitKey(0)

search_contours()