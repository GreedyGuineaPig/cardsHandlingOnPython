from typing import List
import random as rand

rankOfTrump = ("A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
suitOfTrump = ("C", "D", "H", "S")
ranking = {"A": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
           "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}


def createNewDeck() -> List:
    return [(rank, suit) for rank in rankOfTrump for suit in suitOfTrump]


def dealHands(deck, handSize) -> List:
    rand.shuffle(deck)
    hand = []
    for i in range(handSize):
        hand.append(deck.pop())
    return hand


def dealTwoHands(deck, handSize) -> List:
    rand.shuffle(deck)
    hands = [[], []]
    for i in range(handSize):
        hands[0].append(deck.pop())
        hands[1].append(deck.pop())
    return hands


def printTwoHands(hands) -> None:
    for i in range(len(hands)):
        print(hands[i])
        sortedHand = sortHandByRank(hands[i])
        print(sortedHand)
        printHands(sortedHand)


def sortHandByRank(hand) -> List:
    return sorted(hand, key=lambda x: ranking[x[0]])


def printHands(hands) -> None:
    for card in hands:
        print(cardPrintFormatWithOF(card), end=" ")
    print()


def cardPrintFormatWithOF(card) -> str:
    formattedCard = formatCardColor(card)
    return formattedCard[0] + " of " + formattedCard[1]


def isRedCard(card) -> bool:
    return card[1] == "H" or card[1] == "D"


def makeItRedString(str) -> str:
    return "\033[31m" + str + "\033[0m"


def convertSuitToSymbol(suit) -> str:
    if suit == "C":
        return "\u2663"
    elif suit == "S":
        return "\u2660"
    elif suit == "H":
        return "\u2665"
    else:
        return "\u2666"


def getSuitFreqs(hand) -> dict:
    D = {}
    for card in hand:
        if card[1] in D.keys():
            D[card[1]] += 1
        else:
            D[card[1]] = 1
    return D


def getRankFreqs(hand) -> dict:
    D = {}
    for card in hand:
        if card[0] in D.keys():
            D[card[0]] += 1
        else:
            D[card[0]] = 1
    return D


def printCardImage(card, back) -> None:
    printCardsImageTopAndBottom([card])
    printCardsImageSecondRow([card], back)
    printCardsImageThirdRow([card])
    printCardsImageTopAndBottom([card])


def printHandImageHorizontally(hand, back) -> None:
    printCardsImageTopAndBottom(hand)
    printCardsImageSecondRow(hand, back)
    printCardsImageThirdRow(hand)
    printCardsImageTopAndBottom(hand)


def printCardsImageThirdRow(hand) -> None:
    for _ in hand:
        print("|   |", end=" ")
    print()


def formatCardColor(card) -> tuple:
    if isRedCard(card):
        return makeItRedString(card[0]), makeItRedString(convertSuitToSymbol(card[1]))
    return card


def printCardsImageSecondRow(hand, back) -> None:
    sortedHand = sortHandByRank(hand)
    for card in sortedHand:
        if back:
            mark = "   "
        else:
            formattedCard = formatCardColor(card)
            if card[0] == "10":
                mark = "|" + formattedCard[0] + formattedCard[1] + "|"
            else:
                mark = "|" + formattedCard[0] + " " + formattedCard[1] + "|"
        print(mark, end=" ")
    print()


def printCardsImageTopAndBottom(hand) -> None:
    for _ in hand:
        print("+---+ ", end="")
    print()


def redCardBingoGame(i) -> None:
    print("---------------Red Card Bingo!----------------------")
    newDeck = createNewDeck()
    for _ in range(i):
        hand = dealHands(newDeck, i)
        printHandImageHorizontally(hand, False)


def main():
    deck = createNewDeck()
    hand = dealHands(deck, 5)
    hands = dealTwoHands(deck, 5)
    printTwoHands(hands)
    getRankFreqs(hand)
    getSuitFreqs(hand)
    printHandImageHorizontally(hand, False)
    redCardBingoGame(5)


main()
