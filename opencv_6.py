"""Побитовые операции и маски"""

import cv2
import numpy as np

pic_path = "../Downloads/barsik.jpeg"
def execute(path:str = pic_path) -> None:

    #подгрузим изображение кота
    cat = cv2.imread(path)

    #создадим пустое полотно точно такого же размера как и изображение кота
    canvas = np.zeros((cat.shape[:2]), dtype='uint8')

    #создадим черное полотно
    img = np.zeros((500, 500), dtype='uint8')

    #создадим круг и прямоугольник
    #белый цвет круга
    #-1 - залит полностью внутри
    circle = cv2.circle(img.copy(), (0,0), 75, (255,0,0), -1)
    rectangle = cv2.rectangle(img.copy(), (25,25), (225, 225), (255, 0, 0), -1)

    #ПОБИТОВЫЕ ОПЕРАЦИИ (операции по объединению)
    #нахождение частей объектов, которые перескаются (общие пиксели)
    img_circle_rect = cv2.bitwise_and(circle, rectangle)

    #получение полного объединения объектов
    img_full_join = cv2.bitwise_or(circle, rectangle)

    #объединения объектов, но все , что совпадает, не выводится
    imgXOR = cv2.bitwise_xor(circle, rectangle)

    #метод инверсии (черное станет белым, и наоборот)
    img_inver = cv2.bitwise_not(circle)

    #работа с масками(выделение определенного фрагмента на изображении)
    #создадим новый круг
    new_circle = cv2.circle(canvas.copy(), (210, 280), 150, (255, 0,0), -1)
    #объединим одно и тоже фото само с собой
    res_1 = cv2.bitwise_and(cat, cat, mask=new_circle)

    #выведем на экран
    # cv2.imshow("circle", circle)
    # cv2.imshow("rectangle", rectangle)
    # cv2.imshow("img_circle_rect", img_circle_rect)
    # cv2.imshow("img_full_join", img_full_join)
    # cv2.imshow("imgXOR", imgXOR)
    # cv2.imshow("img_inver", img_inver)
    cv2.imshow("cat&cat", res_1)

    cv2.waitKey(0)

execute()