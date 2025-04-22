from random import shuffle


class Card:
    """
    Class representing a card.
    ----------------------------------
    Attributes:
        suit (str): The suit of the card. Must be one of "S", "H", "D", "C"
        value (int): The value of the card. Must be between 1 and 13. Aces have the value 1

    """
    def __init__(self, suit, value, hidden=False):
        self.suit = suit
        self.value = value
        self.index = self._get_index()
        self.hidden = hidden

    def _get_index(self) -> int:
        if self.suit == "S":
            off_set = 0
        elif self.suit == "H":
            off_set = 13
        elif self.suit == "D":
            off_set = 26
        else:
            off_set = 39
        return off_set + self.value - 1

    def __str__(self):
        if self.hidden:
            return "??"
        suit_symbols = {
            "H": "♥", "D": "♦", "C": "♣", "S": "♠"
        }
        symbol = suit_symbols[self.suit]
        if self.value == 1:
            return f"A{symbol}"
        if self.value == 11:
            return f"J{symbol}"
        if self.value == 12:
            return f"Q{symbol}"
        if self.value == 13:
            return f"K{symbol}"

        return f"{self.value}{symbol}"


class Deck:
    """
    Class representing a deck of cards.
    """
    def __init__(self):
        self.cards = [Card(suit, value) for suit in "SHDC" for value in range(1, 14)]
        shuffle(self.cards)

    def deal(self, num_cards: int = 1) -> list[Card]:
        """
        Deals cards and discards them from the deck.
        -----------------------
        Parameters:
            num_cards (int): The number of cards to deal.

        Returns:
            list[Card]: The sequence of cards dealt.
        """

        if num_cards > len(self.cards):
            raise ValueError
        return [self.cards.pop() for _ in range(num_cards)]


if __name__ == "__main__":
    card1 = Card("S", 2)
    card2 = Card("H", 1)
    print(card1.index, card2.index)

    deck = Deck()
    print(*deck.deal(3))
