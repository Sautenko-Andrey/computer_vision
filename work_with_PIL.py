from PIL import Image
import os

path = '../beerBot_DATA/pics/all_beers/001_edelburg_hefew.png'

#открытие изображения и преобразование в градации серого
my_img = Image.open(path).convert('L')
#my_img.show()

def to_jpg(img_list:str):

    '''Reads images from img_list and coverts
     them into jpeg format'''

    for image in img_list:
        out_img = os.path.splitext(image)[0] + ".jpg"
        if image != out_img:
            try:
                Image.open(image).save(out_img)
            except IOError:
                print("Error: I can't convert file")

#to_jpg('../pics')

#создание миниатюр 128 х 128 пикселей
my_img.thumbnail((128, 128))
#my_img.show()



def cut_canvas(path:str, coordinats:tuple) -> None:
    '''Копирование и вставка областей'''
    if not isinstance(path, str):
        raise TypeError("Error: Path must be string.")
    if len(coordinats) != 4:
        raise AttributeError("Error: tuple coordinats expects 4 values.")

    #opening image
    img = Image.open(path)
    #img.show()

    #cutting region by coordinats
    region = img.crop(coordinats)
    #region.show()

    #rotate 180 and put back to original image
    region = region.transpose(Image.ROTATE_180)
    img.paste(region, coordinats)
    img.show()


cords = (100,100,150,150)
#cut_canvas(path, cords)


def change_or_rotate(path:str, mode:str, new_size:tuple = None, angle = None) -> None:
    '''Изменение размера или поворот'''

    if mode == 'c':
        if len(new_size) != 2:
            raise AttributeError("Error: new_size attribute should contains 2 elements.")
        img = Image.open(path)
        out_img = img.resize((new_size))
        out_img.show()

    elif mode == 'r':
        if not  isinstance(angle, (int, float)):
            raise TypeError("Error: angle should be a digital")

        img = Image.open(path)
        out_image = img.rotate(angle)
        out_image.show()

    else:
        raise IOError("Error: Unsupported mode.")

# change_or_rotate(path, 'c', new_size= (100, 50))
# change_or_rotate(path, 'r', angle=45)
