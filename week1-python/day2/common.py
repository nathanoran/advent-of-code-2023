class CubeGroup:
    def __init__(self, maxRed: int, maxGreen: int, maxBlue: int):
        self.red = maxRed
        self.green = maxGreen
        self.blue = maxBlue

    def getPower(self):
        return self.red * self.blue * self.green

class Game:
    def __init__(self, id: int, pulls: list[CubeGroup]):
        self.id = id
        self.pulls = pulls

def parseIntoGames():
    gameResultsFile = open('game-results.txt', 'r')
    gameResults = gameResultsFile.readlines()

    games: list[Game] = []

    for game in gameResults:
        [gameLabel, AllCubePulls] = game.split(':')

        [gameString, gameId] = gameLabel.split(' ')
        gameId = int(gameId)

        cubePulls = AllCubePulls.strip().split(';')
        gamePulls: list[CubeGroup] = []

        for cubePull in cubePulls:
            cubeGroups = cubePull.strip().split(',')
            gamePull: CubeGroup = CubeGroup(0,0,0)

            for cubeColorGroup in cubeGroups:
                [count, color] = cubeColorGroup.strip().split(' ')
                count = int(count)
                if (color == 'red'):
                    gamePull.red = count
                elif (color == 'green'):
                    gamePull.green = count
                elif (color == 'blue'):
                    gamePull.blue = count
            
            gamePulls.append(gamePull)
        
        games.append(Game(gameId, gamePulls))

    return games
