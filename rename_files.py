import os
import random

'''Для переименования фотографий продуктов папках, которые используются для обучения НС'''

item_name='saka'
file_extension = "jpeg"

path = '../faces/saka'
for file in os.listdir(path):
    if file.endswith(file_extension):
        i = random.randint(1, 999999)
        os.rename(f'{path}/{file}', f'{path}/{item_name}_{i}.{file_extension}')
        i+=1