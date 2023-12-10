class Race:
    timeLimit: int = 0
    distanceRecord: int = 0

def defineRaces():
    races: list[Race] = []

    # Part 1 Problem Input
    race = Race()
    race.timeLimit = 50
    race.distanceRecord = 242
    races.append(race)
    
    race = Race()
    race.timeLimit = 74
    race.distanceRecord = 1017
    races.append(race)

    race = Race()
    race.timeLimit = 86
    race.distanceRecord = 1691
    races.append(race)

    race = Race()
    race.timeLimit = 85
    race.distanceRecord = 1252
    races.append(race)

    return races

def doesHoldTimeBeatRecord(race: Race, holdTime: int):
    print('holdTime:', holdTime)
    remainingTime = race.timeLimit - holdTime
    print('remaining time:', remainingTime)
    remainingTime = max(remainingTime, 0)
    print('remaining time:', remainingTime)
    mmPerS = holdTime
    distanceTravelled = remainingTime * mmPerS
    print('distance traveled:', distanceTravelled)
    print('record distance:', race.distanceRecord)
    print('result:',distanceTravelled > race.distanceRecord)
    return distanceTravelled > race.distanceRecord

races = defineRaces()

numberOfWinners = 1

for race in races:
    print(f'race: {race.timeLimit}ms, {race.distanceRecord}mm')
    shortestHoldTime = 0
    while (not doesHoldTimeBeatRecord(race, shortestHoldTime)):
        shortestHoldTime += 1

    print('shortestHoldTime', shortestHoldTime)
    
    longestHoldTime = race.timeLimit
    while (not doesHoldTimeBeatRecord(race, longestHoldTime)):
        longestHoldTime -= 1
    print('longestHoldTime', longestHoldTime)

    print('calculated number of winners:', longestHoldTime - shortestHoldTime + 1)

    numberOfWinners = numberOfWinners * (longestHoldTime - shortestHoldTime + 1)

    print('cummulative number of winners:',numberOfWinners)