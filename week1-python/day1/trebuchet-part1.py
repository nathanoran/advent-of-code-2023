
calibrationsFile = open('calibrations.txt', 'r')
calibrations = calibrationsFile.readlines()

calibrationSum = 0
for calibrationString in calibrations:
    tensPlaceIndex = ''
    onesPlaceIndex = ''
    for i in range(len(calibrationString)):
        if (tensPlaceIndex == '' and calibrationString[i].isdigit()):
            tensPlaceIndex = i
        if (calibrationString[i].isdigit()):
            onesPlaceIndex = i
    calibrationShort = calibrationString[tensPlaceIndex]+calibrationString[onesPlaceIndex]
    calibrationSum += int(calibrationShort)

print(calibrationSum)
