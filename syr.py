import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image

def selection_of_scale(json):
    toponym = json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split()
    toponym_l_c = toponym['boundedBy']['Envelope']['lowerCorner']
    toponym_r_c = toponym['boundedBy']['Envelope']['upperCorner']
    l_toponym_longitude, l_toponym_lattitude = map(float, toponym_l_c.split(" "))
    r_toponym_longitude, r_toponym_lattitude = map(float, toponym_r_c.split(" "))
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": f"{r_toponym_longitude - l_toponym_longitude},{r_toponym_lattitude - l_toponym_lattitude}",
        "l": "map",
        "pt": ",".join([toponym_longitude, toponym_lattitude]) + ",pm2rdm"}
    return map_params


# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    # обработка ошибочной ситуации
    pass

# Преобразуем ответ в json-объект
json_response = response.json()
# Получаем первый топоним из ответа геокодера.
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
# Координаты центра топонима:
toponym_coodrinates = toponym["Point"]["pos"]
# Долгота и широта:
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

delta = input()

map_params = selection_of_scale(json_response)

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
# Создадим картинку
# и тут же ее покажем встроенным просмотрщиком операционной системы