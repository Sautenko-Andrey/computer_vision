import numpy as np
from PIL import Image
from pylab import *

path = '../beerBot_DATA/pics/all_beers/001_edelburg_hefew.png'

def img_to_array(path:str):
    '''Представление изображения в виде массива'''

    #откроем и посмотрим как цветное изображение int
    img_array = array(Image.open(path))
    print(f"Image shape: {img_array.shape}\nImage type: {img_array.dtype}\n\n")

    # откроем и посмотрим как черно-белое изображение float
    img_array_bw = array(Image.open(path).convert('L'), dtype='f')
    print(f"Image shape: {img_array_bw.shape}\nImage type: {img_array_bw.dtype}")


img_to_array(path)
