import requests
api_server = "http://static-maps.yandex.ru/1.x/"
st = input()
port = int(input())
lon = int(input())
lat = int(input())
delta = "0.002"

params = {
    "st": st,
    "port": port,
    "lon": lon,
    "lat": lat,
    "spn": ",".join([delta, delta]),
    "l": "map"
}
response = requests.get(api_server, params=params)
json_response = response.json()
print(json_response)
