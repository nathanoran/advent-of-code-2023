
cardPile = open('day4/scratch-cards.txt', 'r')
scratchCards: list[str] = cardPile.readlines()

def convertStringIntList (numberList: str, separator: str = ' '):
    finalList: list[int] = []
    numberList = numberList.strip().split(separator)
    for number in numberList:

        if not number == '' and number.isnumeric():
            finalList.append(int(number))
    return finalList

def calculateScore(winnersCount: int):
    score = 0
    if winnersCount < 1:
        return score
    for x in range(winnersCount):
        if x == 0:
            score = 1
        elif x == 1:
            score = 2
        else:
            score = score * 2
    return score

cumulativeScore = 0
for card in scratchCards:
    [cardLabel, cardData] = card.split(':')
    [winners, cardNumbers] = cardData.split('|')
    winners = convertStringIntList(winners)
    cardNumbers = convertStringIntList(cardNumbers)
    winnersCount = 0
    for number in cardNumbers:
        if number in winners:
            print(f'{number} appears in {winners}')
            winnersCount += 1
    cumulativeScore += calculateScore(winnersCount)

print(cumulativeScore)
    

