camelCards = open('day7/camel-cards.txt', 'r')
allHands: list[str] = camelCards.readlines()

class Hand:
    cards: str
    bid: int
    cardCounts: dict
    type: int

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        self.cardCounts = dict.fromkeys(self.cards, 0)
        for cardChar in self.cards:
            if (not self.cardCounts[cardChar]):
                self.cardCounts[cardChar] = 1
            else:
                self.cardCounts[cardChar] += 1
        self.type = self.getType()
        print('New Hand:',self.cards)
        print('Determined Type:',self.type)
        print('Bid:',self.bid)
    
    def isFiveOfAKind(self):
        return len(self.cardCounts) == 1

    def isFourOfAKind(self):
        if len(self.cardCounts) != 2:
            return False
        counts = list(self.cardCounts.values())
        return counts[0] == 4 or counts[1] == 4
    
    def isFullHouse(self):
        if len(self.cardCounts) != 2:
            return False
        counts = list(self.cardCounts.values())
        return counts[0] == 3 or counts[1] == 3
    
    def isThreeOfAKind(self):
        if len(self.cardCounts) != 3:
            return False
        counts = list(self.cardCounts.values())
        return counts[0] == 3 or counts[1] == 3 or counts[2] == 3
    
    def isTwoPair(self):
        if len(self.cardCounts) != 3:
            return False
        counts = list(self.cardCounts.values())
        return counts[0] == 2 or counts[1] == 2 or counts[1] == 2

    def isOnePair(self):
        return len(self.cardCounts) == 4
    
    def getType(self):
        if self.isFiveOfAKind():
            return 6
        elif self.isFourOfAKind():
            return 5
        elif self.isFullHouse():
            return 4
        elif self.isThreeOfAKind():
            return 3
        elif self.isTwoPair():
            return 2
        elif self.isOnePair():
            return 1
        else:
            return 0
    
    def __str__(self):
        return f'({self.cards} | type: {self.type})'

def getCardValue(card: str):
    if card == 'T':
        return 10
    elif card == 'J':
        return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    elif card == 'A':
        return 14
    else:
        return int(card)

def compareHands(handA: Hand, handB: Hand):
    print(f'comparing hands: A={handA}, B={handB}')
    if (handA.type > handB.type):
        print('Determined hand A should be after hand B')
        return 1
    if (handA.type < handB.type):
        print('Determined hand A should be before hand B')
        return -1
    for i in range(5):
        if (getCardValue(handA.cards[i]) > getCardValue(handB.cards[i])):
            print('Determined hand A should be after hand B')
            return 1
        if (getCardValue(handA.cards[i]) < getCardValue(handB.cards[i])):
            print('Determined hand A should be before hand B')
            return -1
    print('hand A and hand B are equivalent')
    return 0

# 2-dimensional array first index is the hand type, second is the sorted order
hands: list[list[Hand]] = [[],[],[],[],[],[],[]]

for line in allHands:
    line = line[:-1:] # remove new line char
    [cards, bid] = line.split(' ')

    hand = Hand(cards, int(bid))
    handType = hand.type

    if len(hands[handType]) == 0:
        hands[handType].append(hand)
        print(f'new hand going into position 0\n')
    else:
        # insertion sort
        i = 0
        while i < len(hands[handType]) and compareHands(hand, hands[handType][i]) >= 0:
            i += 1
            print(f'i updated: {i}')

        print(f'new hand going into position {i}\n')
        
        hands[handType].insert(i, hand)

cumulativeWinnings = 0

rank = 1

for i in range(len(hands)):
    for j in range(len(hands[i])):
        print(f'Hand: {hands[i][j]} gets rank: {rank}. Bid: {hands[i][j].bid}')
        cumulativeWinnings += rank * hands[i][j].bid
        rank += 1
        print(f'cumulationWinnings: {cumulativeWinnings}\n')
