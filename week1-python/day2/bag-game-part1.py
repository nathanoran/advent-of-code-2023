from common import CubeGroup

gameResultsFile = open('game-results.txt', 'r')
gameResults = gameResultsFile.readlines()

bag = CubeGroup(12, 13,14)

possibleGameSum = 0
for game in gameResults:
    [gameLabel, AllCubePulls] = game.split(':')

    [gameString, gameId] = gameLabel.split(' ')
    gameId = int(gameId)

    cubePulls = AllCubePulls.strip().split(';')

    isGamePossible = True
    for cubePull in cubePulls:
        cubeGroups = cubePull.strip().split(',')
        for cubeColorGroup in cubeGroups:
            [count, color] = cubeColorGroup.strip().split(' ')
            count = int(count)
            if (color == 'red' and count > bag.red):
                isGamePossible = False
            elif (color == 'green' and count > bag.green):
                isGamePossible = False
            elif (color == 'blue' and count > bag.blue):
                isGamePossible = False
    
    if (isGamePossible):
        possibleGameSum += gameId

print(possibleGameSum)
