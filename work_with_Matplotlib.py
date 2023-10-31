from PIL import Image
from pylab import *
path = '../beerBot_DATA/pics/all_beers/001_edelburg_hefew.png'

def check_path(path:str):
    if type(path) != str:
        raise TypeError("Error: type of path must be string.")
    if path[-4:] not in ['.jpg', '.png'] and path[-5:] != '.jpeg':
        raise ValueError("Error: unsupported extension")

def drawing_on_image(path:str) -> None:
    '''Нанесение на изображение нескольких
    точек и отрезка прямой'''

    check_path(path)

    #прочитаем изображение в массив
    img_array = array(Image.open(path))

    #поместим на график изображение
    imshow(img_array)

    #зададим несколько точек
    x_coord = [100, 100, 150, 150]
    y_coord = [150, 200, 150, 200]

    #нанесем эти точки в виде красных звездочек
    plot(x_coord, y_coord, 'r*')

    #нарисуем отрезок, соединяющий первые две точки
    plot(x_coord[:2], y_coord[:2])

    #добавить заголовок и показать график
    title("Plotting: beer")

    #отключим координаты
    axis('off')

    show()

#drawing_on_image(path)



def draw_isolines_histohrams(path:str) -> None:
    '''Изолинии и гистограммы изображений'''

    check_path(path)

    #прочитаем изображение в массив и сделаем полутоновым
    img_array = array(Image.open(path).convert('L'))

    #создадим новый рисунок
    figure()

    #не использовать цвета
    gray()

    #показать изолинии относительно верхнего левого угла
    contour(img_array, origin = 'image')
    axis('equal')
    axis('off')

    #далее нарисуем гистограмму
    # создадим новый рисунок
    figure()

    #создаем гистограмму
    #flatten() преобразовывает любой массив в одномерный
    hist(img_array.flatten(), 128)

    show()

#draw_isolines_histohrams(path)

def mark_dots(path:str):
    '''Интерактивное аннотирование.
    После вывода графика программа будет ждать пока
    пользователь три раза щелкнет мышью вобласти
    окна рисунка. Координаты отмеченных пользователем
    точек сохраняются в переменной x'''
    check_path(path)

    #сохраним изображение в массив
    img_arr = array(Image.open(path))

    # поместим на график изображение
    imshow(img_arr)

    print("Щелкните в 3-ч точках")
    x = ginput(3)

    print(f"Вы щелкнули: {x}")

    show()

mark_dots(path)