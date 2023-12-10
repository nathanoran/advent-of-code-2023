import math

class Race:
    timeLimit: int = 0
    distanceRecord: int = 0

def defineRaces():
    races: list[Race] = []

    # # Part 1 Problem Input
    # race = Race()
    # race.timeLimit = 50
    # race.distanceRecord = 242
    # races.append(race)
    
    # race = Race()
    # race.timeLimit = 74
    # race.distanceRecord = 1017
    # races.append(race)

    # race = Race()
    # race.timeLimit = 86
    # race.distanceRecord = 1691
    # races.append(race)

    # race = Race()
    # race.timeLimit = 85
    # race.distanceRecord = 1252
    # races.append(race)

    # Part 2 Problem Input
    race = Race()
    race.timeLimit = 50748685
    race.distanceRecord = 242101716911252
    races.append(race)

    return races

def calculateDistanceTravelledForHoldTime(race: Race, holdTime:int):
    print('holdTime:', holdTime)
    remainingTime = race.timeLimit - holdTime
    print('remaining time:', remainingTime)
    remainingTime = max(remainingTime, 0)
    print('remaining time:', remainingTime)
    mmPerS = holdTime
    distanceTravelled = remainingTime * mmPerS
    print('distance traveled:', distanceTravelled)
    return distanceTravelled

def doesHoldTimeBeatRecord(race: Race, holdTime: int):
    print('record distance:', race.distanceRecord)
    distanceTravelled = calculateDistanceTravelledForHoldTime(race, holdTime)
    print('result:',distanceTravelled > race.distanceRecord)
    return distanceTravelled > race.distanceRecord

def findShortestWinningHoldTime (race: Race, min: int, max: int):
    """Because we're specifically looking for the shortest Winning hold time, if we find a winner, we always go smaller"""
    while max - min > 1: # this check is a bit sloppy for the binary search algorithm, but it works for my test input.
        print(f'min: {min}, max:{max}')
        mid = int(((max - min) / 2) + min)
        if (doesHoldTimeBeatRecord(race, mid)):
            max = mid
        else:
            min = mid

    return max

races = defineRaces()

numberOfWinners = 1

for race in races:
    print(f'race: {race.timeLimit}ms, {race.distanceRecord}mm')
    # this approach will take advantage of the symmetry of the calculations.
    # Ex: a race that lasts 50ms, holding for 1ms and 49ms result in the same distance,
    #     holding for 2ms and 48ms result in the same distance, and so on.
    # So if we start with a holdTime = 1/2 the available time, we maximize the distance travelled per ms,
    # and their for maximize the distance traveled. From there, we only need to look at distances less than
    # or greater than the most optimal option. Because for every hold time longer than the most optimal
    # holdTime, there is an equally effective holdTime that is shorter than the most optimal hold time.

    shortestWinningHoldTime = findShortestWinningHoldTime(race, 0, race.timeLimit)

    totalNumberOfHoldTimes = race.timeLimit + 1 # 1 accounts for the zero case

    numberOfWinners = numberOfWinners * (totalNumberOfHoldTimes - (2 * shortestWinningHoldTime))
        
    print('cummulative number of winners:', numberOfWinners)