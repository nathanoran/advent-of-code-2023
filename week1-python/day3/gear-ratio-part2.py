from common import findAdjacentValues


engineFile = open('day3/engine-schematic.txt', 'r')
engineSchematic: list[str] = engineFile.readlines()

def isGearSymbol (x: int, y: int):
    return engineSchematic[y][x] == '*'

gearRatioHashValue = 0
for y in range(len(engineSchematic)):
    # -1 below removes the new line character
    for x in range(len(engineSchematic[y]) - 1):
        # print(f'evaluating special character at ({x}, {y}). Character is: "{engineSchematic[y][x]}" Result: {isSpecialSymbol(x, y)}')
        if (isGearSymbol(x, y)):
            values = findAdjacentValues(engineSchematic, x, y)
            # it's only a gear if it has exactly 2 values
            if (len(values) == 2):
                gearRatio = values[0] * values[1]
                gearRatioHashValue += gearRatio

print(gearRatioHashValue)