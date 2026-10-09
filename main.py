import requests
from projecten import weerstation
from projecten import smartAppController

def weerUtrecht():
    try:
        dataMeteo = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.0907&longitude=5.1214&current=temperature_2m").json()
        temp = dataMeteo["current"]["temperature_2m"]
        print(temp)
    except:
        print("er ging iets mis")

while True:
    print("1: laat het huidige temperatuur in utrecht zien")
    print("2: start weerstation")
    print("3: start smartAppController")
    print("4: stop het programma")

    keuze = input()
    try:
        keuze = int(keuze)
    except:
        print("ongeldige keuze")
        continue

    if keuze != 1 and keuze != 2 and keuze != 3 and keuze !=4:
        print("ongeldige keuze")
        continue

    elif keuze == 1:
        weerUtrecht()

    elif keuze == 2:
        weerstation.weerstation()

    elif keuze == 3:
        smartAppController.smartAppControllerS3()

    elif keuze == 4:
        break




