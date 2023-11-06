'''Цветовые форматы'''
import cv2

pic_path = "../Downloads/barsik.jpeg"

def change_ColorFormat(path:str = pic_path) -> None:
    """Привидение изображения к
    формату HSV, LAB (оптимизация, потмоу что
    хоть изображение и будет цветным, оно состоит из
    одного слоя,а не 3-х.)"""

    img = cv2.imread(path)

    #меняем формат на HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #меняем формат на LAB
    imgLAB = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    #можно кнвертировать в обратном направлении
    imgOrig = cv2.cvtColor(imgLAB, cv2.COLOR_LAB2BGR)

    #также можно конвертировать в RGB для последующей работы
    #в matplotlib или Pillow
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



    cv2.imshow('HSV', imgHSV)
    cv2.imshow("LAB", imgLAB)
    cv2.imshow("Orig", imgOrig)
    cv2.imshow("RGB", imgRGB)
    cv2.waitKey(0)


#change_ColorFormat()

def color_layers_decompose(path:str = pic_path) -> None:
    '''Разбиение слоев. Цветное изображение
    мы можем разбить на 3 слоя : красный, зеленый
    и синий, соответствено на 3 изображения.'''

    img = cv2.imread(path)

    #разобьем на синий, зеленый и красный
    blue, green, red = cv2.split(img)

    #объединить обратно все слои
    img_orig = cv2.merge([blue, green, red])

    #или поменяем местами
    img_rgb = cv2.merge([red, green, blue])

    # выведем отдельно три цвета
    #при выводе все цвета, которое приближенные к красному,зеленому и синему,
    #они становятся белыми
    cv2.imshow("Blue", blue)
    cv2.imshow("Green", green)
    cv2.imshow("Red", red)
    cv2.imshow("Orig", img_orig)
    cv2.imshow("RGB", img_rgb)

    cv2.waitKey(0)

color_layers_decompose()