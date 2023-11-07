'''Распознование лиц на изображениях'''

import cv2

pic_path = "../Downloads/people_3.jpg"

def execute(path:str = pic_path) ->None:


    img = cv2.imread(path)

    #преобразуем изображение к серому формату
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #вытянем файл как натренированную модель НС
    nn_faces = cv2.CascadeClassifier("./nn_models/faces.xml")

    #заведем перменную, которая будет содержать координаты найденных лиц
    #засчет метода detectMultiScale() мы находим координаты всех найденных объектов(лиц)
    #scaleFactor - если модель натренирована на маленьких лицах, то мі через
    #этот параметр указываем во сколько раз может быть увеличены лица на нашем изображении
    #по сравнению с натренированными(подставновка методом проб)
    #minNeighbors - как много может быть соседей рядом с найденным объектом(сколько лиц на фото)
    results = nn_faces.detectMultiScale(img_gray,scaleFactor=1.4, minNeighbors=3)

    #далее сделаем так, что все найденные лица будут выделены в квадратики
    #чтобы обвести лица в квадратики, создадим цикл

    # coord_x,coord_y - координаты, где было найдено лицо
    # width, height - ширина и высота найденного лица
    #работаем с серым изображением, но обводим лица на цветном изображении
    for (coord_x,coord_y, width, height) in results:
        #далее чертим квадратик вокруг лица
        cv2.rectangle(img, (coord_x, coord_y), (coord_x + width, coord_y + height), (0,0,255), thickness=3)



    cv2.imshow("Result", img)
    cv2.waitKey(0)

execute()