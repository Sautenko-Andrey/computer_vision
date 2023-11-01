from numpy import *
from PIL import Image
from pylab import *

path = '../beerBot_DATA/pics/all_beers/001_edelburg_hefew.png'
original = Image.open(path)
original.show()

def img_to_array(path:str):
    '''Представление изображения в виде массива'''

    #откроем и посмотрим как цветное изображение int
    img_array = array(Image.open(path))
    print(f"Image shape: {img_array.shape}\nImage type: {img_array.dtype}\n\n")

    # откроем и посмотрим как черно-белое изображение float
    img_array_bw = array(Image.open(path).convert('L'), dtype='f')
    print(f"Image shape: {img_array_bw.shape}\nImage type: {img_array_bw.dtype}")


#img_to_array(path)

def light_up(path:str) -> None:
    '''Преобразование уровня яркости'''
    img_arr = array(Image.open(path).convert('L'))


    #инвертируем изображение
    img2 = 255 - img_arr
    pic2 = Image.fromarray(img2)
    pic2.show()

    #приведем цвета к интервалу 100 - 200
    img3 = (100.0 / 255) + img_arr + 100
    pic3 = Image.fromarray(uint8(img3))
    pic3.show()

    #применим квадратичную функцию
    img4 = 255.0 * (img_arr / 255.0) **2
    pic4 = Image.fromarray(uint8(img4))
    pic4.show()

#light_up(path)

def change_size(image:ndarray, size:tuple) -> array:
    '''Изменение размера изображения'''

    new_image = Image.fromarray(uint8(image))
    return array(new_image.resize(size))

def histeq(image:ndarray, number_bins = 256) -> tuple:
    """Выравнивание гистограммы полутонового изображения"""

    #получим гистограмму изображения
    imhist, bins = histogram(image.flatten(), number_bins)
    #функция распределения
    cdf = imhist.cumsum()
    #нормировка
    cdf = 255 * cdf / cdf[-1]

    #используем линейную интерполяцию  cdf для нахождения значения
    #новых пикселей
    new_img = interp(image.flatten(), bins[-1], cdf)
    return new_img.reshape(image.shape), cdf














