def convertStringIntList (numberList: str, separator: str = ' '):
    finalList: list[int] = []
    numberList = numberList.strip().split(separator)
    for number in numberList:

        if not number == '' and number.isnumeric():
            finalList.append(int(number))
    return finalList