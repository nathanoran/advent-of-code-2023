from common import CubeGroup, parseIntoGames

games = parseIntoGames()

powerSum = 0
for game in games:
    smallestCubeGroup = CubeGroup(0,0,0)

    for pull in game.pulls:
        smallestCubeGroup.red = max(smallestCubeGroup.red, pull.red)
        smallestCubeGroup.green = max(smallestCubeGroup.green, pull.green)
        smallestCubeGroup.blue = max(smallestCubeGroup.blue, pull.blue)

    powerSum += smallestCubeGroup.getPower()


print(powerSum)
