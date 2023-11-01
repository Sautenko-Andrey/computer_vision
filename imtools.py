import os
from PIL import Image
from pylab import *

def get_imlist(path:str) -> list:
    '''Returns names list of all jpg-files
    within catalog'''

    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(".jpg")]

def change_size(image:ndarray, size:tuple | list) -> array:
    '''Изменение размера изображения'''

    if not isinstance(image, ndarray) or not isinstance(size,(tuple, list)):
        raise TypeError("Error: type of argument is unsupported.")

    if len(size) != 2:
        raise AttributeError("Error: size has 2 elements.")

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