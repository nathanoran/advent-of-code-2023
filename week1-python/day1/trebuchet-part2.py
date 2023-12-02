
calibrationsFile = open('calibrations.txt', 'r')
calibrations = calibrationsFile.readlines()

digitStrings = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def determineFirstValidIndex (calibrationString, indexA, indexB):
    if (indexA >= 0 and indexB >= 0):
        firstIndex = min(indexA, indexB)
    elif (indexA >= 0 and indexB < 0):
        firstIndex = indexA
    elif (indexA < 0 and indexB >= 0):
        firstIndex = indexB
    else:
        firstIndex = len(calibrationString)
    return firstIndex

def findTensPlace (calibrationString):
    tensValue = '-1'
    tensIndex = len(calibrationString)
    for x in range(10):
        numberIndex = calibrationString.find(str(x))
        stringIndex = calibrationString.find(digitStrings[x])

        firstIndex = determineFirstValidIndex(calibrationString, numberIndex, stringIndex)

        if (firstIndex < tensIndex):
            tensValue = str(x)
            tensIndex = firstIndex

    if (tensValue == '-1'):
        print('This calibration string does not parse properly:', calibrationString)

    return tensValue

def findOnesPlace (calibrationString):
    reversedCalibration = calibrationString[::-1]

    onesValue = '-1'
    onesIndex = len(reversedCalibration)
    for x in range(10):
        numberIndex = reversedCalibration.find(str(x))
        stringIndex = reversedCalibration.find(digitStrings[x][::-1])

        firstIndex = determineFirstValidIndex(calibrationString, numberIndex, stringIndex)

        if (firstIndex < onesIndex):
            onesValue = str(x)
            onesIndex = firstIndex
    
    if (onesValue == '-1'):
        print('This calibration string does not parse properly:', calibrationString)

    return onesValue

calibrationSum = 0
for calibrationString in calibrations:
    calibrationShort = findTensPlace(calibrationString) + findOnesPlace(calibrationString)
    calibrationSum += int(calibrationShort)

print(calibrationSum)
