def smartAppControllerS3():
    def aantalDagen(inputFile):
        fileHandle = open(inputFile, "r")
        dagen = 0
        for lijnen in fileHandle.readlines():
            dagen += 1
        dagen = dagen - 1
        fileHandle.close()
        return dagen

    def autoberekeningActuatoren(inputFile, outputFile):
        fileHandle = open(inputFile, "r")
        outputFile = open(outputFile, "w")
        lijn = 0
        for lines in fileHandle.readlines():
            datum, people, setpoint, buitentemperatuur, neerslag = lines.split()
            if lijn != 0:
                tempVerschil = float(setpoint) - float(buitentemperatuur)
                if tempVerschil >= 20:
                    CVketel = 100
                elif 10 <= tempVerschil < 20:
                    CVketel = 50
                elif tempVerschil < 10:
                    CVketel = 0

                people = int(people)
                if people <= 3:
                    ventStand = people + 1
                else:
                    ventStand = 4

                neerslag = float(neerslag)
                if neerslag < 3:
                    bewatering = True
                elif neerslag >= 3:
                    bewatering = False

                outputFile.write(f"{datum};{CVketel};{ventStand};{bewatering} \n")

            lijn += 1

        fileHandle.close()
        outputFile.close()

    def overwriteSettings(outputFile):
        gekozenDatum = input("welke datum wilt u veranderen? ")
        try:
            systeem = int(input("voer 1 in om CV-ketel aan te passen, 2 voor ventilatie en 3 voor bewatering "))
            waarde = int(input("wat moet het worden? "))
        except:
            return -3

        if systeem != 1 and systeem != 2 and systeem != 3:
            return -2
        elif (systeem == 1 and (waarde < 0 or waarde > 100)) or (systeem == 2 and (waarde < 0 or waarde > 4)) or (
                systeem == 3 and (waarde != 0 and waarde != 1)):
            return -3

        readFile = open(outputFile, "r")
        datumGevonden = False
        nieuweRegels = []

        for lines in readFile.readlines():
            data = lines.split(";")
            if data[0] == gekozenDatum:
                datumGevonden = True
                if systeem == 1:
                    data[1] = str(waarde)
                elif systeem == 2:
                    data[2] = str(waarde)
                elif systeem == 3:
                    if waarde == 0:
                        data[3] = "False"
                    else:
                        data[3] = "True"
                lines = ";".join(data) + "\n"

            nieuweRegels.append(lines)

        if datumGevonden == False:
            return -1

        writeFile = open(outputFile, "w")
        writeFile.writelines(nieuweRegels)

        readFile.close()
        writeFile.close()

        return 0

    def smartAppController():
        while True:
            print("1: Aantal dagen weergeven")
            print("2: Automatisch alle actuatoren berekenen en naar uitvoerbestand schrijven")
            print("3: Waarde overschrijven in het uitvoerbestand")
            print("4: Stoppen")

            keuze = input()
            try:
                keuze = int(keuze)
            except:
                print("ongeldige keuze")
                continue

            if keuze == 1:
                print("dagen:", aantalDagen("weerenzo.txt"))
            elif keuze == 2:
                autoberekeningActuatoren("weerenzo.txt", "output.txt")
                print("actuatoren in output file opgeslagen")
            elif keuze == 3:
                overwriteResult = overwriteSettings("output.txt")
                if overwriteResult == 0:
                    print("succesvol aangepast")
                elif overwriteResult == -1:
                    print("Datum niet gevonden")
                elif overwriteResult == -2:
                    print("Ongeldig systeem gekozen")
                elif overwriteResult == -3:
                    print("Ongeldige waarde ingevoerd")
            elif keuze == 4:
                break
            else:
                print("dit is geen geldige keuze")
                continue

    smartAppController()