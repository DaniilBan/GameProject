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



search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

address_ll = "39.233785,51.634796"

search_params = {
    "apikey": api_key,
    "text": "подготовка к огэ",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)
if not response:
    pass

# Преобразуем ответ в json-объект
json_response = response.json()

# Получаем первую найденную организацию.
organization = json_response["features"][0]
# Название организации.
org_name = organization["properties"]["CompanyMetaData"]["name"]
# Адрес организации.
org_address = organization["properties"]["CompanyMetaData"]["address"]


geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": org_address,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

json_response = response.json()

# Получаем координаты ответа.
point = organization["geometry"]["coordinates"]
print(point)
org_point = "{0},{1}".format(point[0], point[1])
delta = "0.005"

map_params = selection_of_scale(json_response)

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
# Создадим картинку
# и тут же ее покажем встроенным просмотрщиком операционной системы