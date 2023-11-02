import cv2
import numpy as np

def create_pic():
    """Создание объектов разной формы и вывод информации"""

    #создадим черное полотно

    #для этого создадим матрицу с нулями 300 х 300 (изображение будет 300 х 300 пикселей)
    #3 - это цветовой канал(указываем, что используется 3 слоя rgb. Мы сможем окрашивать
    # изображение в другие цвета)
    my_img = np.zeros((300,300, 3), dtype="uint8")

    #далее окрасим изображение полностью в синий цвет
    #формат в opencv BGR (blue, green, red)
    my_img[:] = 255, 0, 0  #значение для B устанавливаем на максимум

    #красное
    #my_img[:] = 0, 0, 255

    #зеленое
    #my_img[:] = 0, 255, 0

    #выберем цвет из google picker и создадим копию нашего изображения
    custom_img = np.copy(my_img)
    custom_img[:] = 133, 86, 123

    #окраска небольшой части изображения
    small_overlap_img = np.copy(my_img)
    small_overlap_img[100:150,200:280] = 11, 44, 227

    #встроенные методы для рисования фигур
    #нарисуем прямоугольник
    #создадим новый холст
    pic = np.copy(my_img)

    #(0, 0) - точка с которой будет происходить рисование прямоугольника (верхний левый угол)
    # (150, 150) - точки до которых мы будем рисовать прямоугольник (правый нижний угол прямоугольника)
    # (11, 44, 227) - цвет обводки
    #thickness - жирность обводки
    cv2.rectangle(pic, (125,150), (250, 250), (11, 44, 227), thickness=2)

    #со значением обводки Filled мы заливаем полностью прямоугольник
    #cv2.rectangle(pic, (125, 150), (250, 250), (11, 44, 227), thickness=cv2.FILLED)

    #Создадим линию
    line_img = np.copy(my_img)
    cv2.line(line_img, (0,0), (150, 0), (11, 44, 227), thickness=3)
    #проведем линию по центру через все изображение
    cv2.line(line_img, (0, line_img.shape[0] //2),
             (line_img.shape[1],line_img.shape[0] //2 ), (11, 44, 227), thickness=2 )

    #создание круга (нарисуем по центру изображения)
    circle_image = np.copy(my_img)
    cv2.circle(circle_image,(circle_image.shape[1]//2, circle_image.shape[0]//2),
               75,(11, 44, 227),thickness=4)

    #создание текстовых надписей на изображении
    text_img = np.copy(my_img)

    cv2.putText(text_img,"some text", (100, 125),
                cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0), thickness=1)


    #выведем на экран
    # cv2.imshow("My image", my_img)
    # cv2.imshow("Custom image", custom_img)
    # cv2.imshow("Small overlap", small_overlap_img)
    # cv2.imshow("Rectangle", pic)
    #cv2.imshow("Line", line_img)
    #cv2.imshow("Circle", circle_image)
    cv2.imshow("With text", text_img)


    cv2.waitKey(0)

create_pic()
