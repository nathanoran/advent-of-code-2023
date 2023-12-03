"""
parses an integer based on the position given
if the position given has no digit, returns -1
"""
def getValue (engineSchematic: list[str], x: int, y: int):
    print(f'Parsing value at ({x}, {y}): {engineSchematic[y][x]}')
    if (not engineSchematic[y][x].isdigit()):
        print ('No digits -- returning -1')
        return -1
    valueString = engineSchematic[y][x]

    rightBound = x
    while (engineSchematic[y][rightBound+1].isdigit()):
        rightBound += 1
        valueString += engineSchematic[y][rightBound]

    leftBound = x
    while (engineSchematic[y][leftBound-1].isdigit()):
        leftBound -= 1
        valueString = engineSchematic[y][leftBound] + valueString
    
    print(f'ParsedValue: {valueString}')
    return int(valueString)


"""
Above and below a special have positions to check for adjacent values:
x..  .x.  ..x
 * ,  * ,  * , 
That said, there are a few edge cases for values with multiple digits:
xx.  xxx  .xx
 * ,  * ,  * 
And posibly two values:
x.x
 *
We don't want to include values more than once, so it's important to detect these edge cases when they occur.
For this method, x and y are the middle position to find one to two values above or below a special character
"""
def findInLineValues(engineSchematic: list[str], x: int, y: int):
    # Check the middle position first
    if(engineSchematic[y][x].isdigit()):
        # Four possible states: .x., xx., .xx, xxx
        # In any of the above states, there is only one value
        return [getValue(engineSchematic, x,y)]

    values: list[int] = []

    # Check Left and Right next
    leftValue = getValue(engineSchematic, x-1, y)
    if (leftValue > -1):
        values.append(leftValue)

    rightValue = getValue(engineSchematic, x+1, y)
    if (rightValue > -1):
        values.append(rightValue)

    return values


def findAdjacentValues(engineSchematic: list[str], x: int, y: int):
    # Assume (x, y) is the possition of a special character
    allValues: list[int] = []

    # Above values
    for value in findInLineValues(engineSchematic, x, y-1): 
        allValues.append(value)

    # Middle values
    for value in findInLineValues(engineSchematic, x, y):
        allValues.append(value)

    # Below values
    for value in findInLineValues(engineSchematic, x, y+1):
        allValues.append(value)
    
    return allValues