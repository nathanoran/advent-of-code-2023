from common import findAdjacentValues


engineFile = open('day3/engine-schematic.txt', 'r')
engineSchematic: list[str] = engineFile.readlines()

def isSpecialSymbol (x: int, y: int):
    return not engineSchematic[y][x].isdigit() and not engineSchematic[y][x] == '.'


def findAdjacentSum (x: int, y: int):
    values = findAdjacentValues(engineSchematic, x, y)
    adjacentSum = 0
    for value in values:
        adjacentSum += value

    return adjacentSum

schematicHashValue = 0
for y in range(len(engineSchematic)):
    # -1 below removes the new line character
    for x in range(len(engineSchematic[y]) - 1):
        # print(f'evaluating special character at ({x}, {y}). Character is: "{engineSchematic[y][x]}" Result: {isSpecialSymbol(x, y)}')
        if (isSpecialSymbol(x, y)):
            schematicHashValue += findAdjacentSum(x, y)

print(schematicHashValue)
