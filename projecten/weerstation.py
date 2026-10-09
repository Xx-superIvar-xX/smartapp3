def weerstation():
    def vraagUserInput(dag):
        while True:
            tempCelcius = input(f"wat is de temperatuur op dag {dag}[C]: ")
            if tempCelcius == "":
                exit()
            else:
                try:
                    tempCelcius = float(tempCelcius)
                    break
                except:
                    print("probeer opnieuw")
                    continue
        while True:
            windsnelheid = input(f"wat is de windsnelheid op dag {dag}[m/s]: ")
            if windsnelheid == "":
                exit()
            else:
                try:
                    windsnelheid = float(windsnelheid)
                    break
                except:
                    print("probeer opnieuw")
                    continue
        while True:
            luchtvochtigheid = input(f"wat is de luchtvochtigheid op dag {dag}[%]: ")
            if luchtvochtigheid == "":
                exit()
            else:
                try:
                    luchtvochtigheid = float(luchtvochtigheid)
                except:
                    print("probeer opnieuw")
                    continue
            if luchtvochtigheid < 0 or luchtvochtigheid > 100:
                print("probeer opnieuw")
                continue
            else:
                break
        return tempCelcius, windsnelheid, luchtvochtigheid

    def gevoelstemperatuur(tempCelcius, windsnelheid, luchtvochtigheid):
        gevoelsTemp = float(tempCelcius) - luchtvochtigheid / 100 * windsnelheid
        return gevoelsTemp

    def fahrenheit(tempCelcius):
        tempFahrenheit = 32 + 1.8 * tempCelcius
        return tempFahrenheit

    def gemTemp(tempLijst):
        return sum(tempLijst) / len(tempLijst)

    def weerrapport(tempCelcius, windsnelheid, luchtvochtigheid):
        if gevoelstemperatuur(tempCelcius, windsnelheid, luchtvochtigheid) < 0 and windsnelheid > 10:
            return "Het is heel koud en het stormt! Verwarming helemaal aan!"
        elif gevoelstemperatuur(tempCelcius, windsnelheid, luchtvochtigheid) < 0 and windsnelheid <= 10:
            return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
        elif 0 <= gevoelstemperatuur(tempCelcius, windsnelheid, luchtvochtigheid) < 10 and windsnelheid > 12:
            return "Het is best koud en het waait; verwarming aan en roosters dicht!"
        elif 0 <= gevoelstemperatuur(tempCelcius, windsnelheid, luchtvochtigheid) < 10 and windsnelheid <= 12:
            return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
        elif 10 <= gevoelstemperatuur(tempCelcius, windsnelheid, luchtvochtigheid) < 22:
            return "Heerlijk weer, niet te koud of te warm."
        else:
            return "Warm! Airco aan!"

    tempLijst = []
    for dag in range(1, 8):
        tempCelcius, windsnelheid, luchtvochtigheid = vraagUserInput(dag)
        tempLijst.append(tempCelcius)
        print("het is", tempCelcius, "°C", "(" + str(fahrenheit(tempCelcius)), "°F)")
        print("de gevoelstemperatuur is", gevoelstemperatuur(tempCelcius, windsnelheid, luchtvochtigheid), "°C")
        print(weerrapport(tempCelcius, windsnelheid, luchtvochtigheid))
        print("de gemiddelde temperatuur tot nu toe is", gemTemp(tempLijst), "°C")
        print("=========================================================")