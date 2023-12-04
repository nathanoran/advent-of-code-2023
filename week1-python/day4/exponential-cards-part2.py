from common import convertStringIntList

cardPile = open('day4/scratch-cards.txt', 'r')
scratchCards: list[str] = cardPile.readlines()

cardCounts: list[int] = []

for i in range(len(scratchCards)):
    cardCounts.append(1)

for i in range(len(scratchCards)):
    card = scratchCards[i]
    [cardLabel, cardData] = card.split(':')
    [winners, cardNumbers] = cardData.split('|')
    winners = convertStringIntList(winners)
    cardNumbers = convertStringIntList(cardNumbers)
    winnersCount = 0
    for number in cardNumbers:
        if number in winners:
            print(f'{number} appears in {winners}')
            winnersCount += 1

    for j in range(winnersCount):
        cardCounts[i + j + 1] += cardCounts[i]

cumulativeCards = 0
for count in cardCounts:
    cumulativeCards += count
print(cumulativeCards)
    

