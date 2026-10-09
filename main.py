import requests

def weerUtrecht():
    dataMeteo = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.0907&longitude=5.1214&current=temperature_2m").json()
    temp = dataMeteo["current"]["temperature_2m"]
    return temp

print(weerUtrecht())

