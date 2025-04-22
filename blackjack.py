from deck import Card, Deck


class Game:
    """
    Creates the blackjack game environment. Each game starts with a fresh deck of cards.
    """
    def __init__(self, five_card_charlie=False):
        self.deck = Deck()
        self.player_hand = self.deck.deal(num_cards=2)
        self.dealer_hand = self.deck.deal(num_cards=2)
        self.is_over = False
        self.score = 0
        self.five_card_charlie = five_card_charlie

    def take_action(self, action: str) -> None:
        """
        Takes an action and updates the environment.

        Parameters:
            action (str): The action to take. "S" for stay and "H" for hit
        Returns:
            None
        """
        if action == "S":
            self._dealer_hit()
            player_hand_value = self.evaluate_hand(self.player_hand)
            dealer_hand_value = self.evaluate_hand(self.dealer_hand)

            if dealer_hand_value > 21:  # dealer busts
                self.score = 1
            elif player_hand_value > dealer_hand_value:  # player has a better hand
                self.score = 1
            elif player_hand_value == dealer_hand_value:  # tie
                self.score = 0
            else:  # dealer has a better hand
                self.score = -1

            self.is_over = True

        else:
            self._hit()
            player_hand_value = self.evaluate_hand(self.player_hand)
            if player_hand_value > 21:
                self.score = -1
                self.is_over = True
            elif player_hand_value == 21:
                self.score = 1
                self.is_over = True
            else:
                if self.five_card_charlie and len(self.player_hand) == 5:
                    self.score = 1
                    self.is_over = True

    def _hit(self) -> None:
        self.player_hand.extend(self.deck.deal())

    def _dealer_hit(self) -> None:
        while self.evaluate_hand(self.dealer_hand) < 17:
            self.dealer_hand.extend(self.deck.deal())

    @staticmethod
    def evaluate_hand(hand: list[Card]) -> int:
        """
        Evaluates the hand. The value of ace is taken 1 or 11 depending on which one gives the best value.
        """
        score = 0
        num_aces = 0
        for card in hand:
            if card.value == 1:
                num_aces += 1
                score += 11
            elif 10 <= card.value:
                score += 10
            else:
                score += card.value

        best_hand = score
        while num_aces > 0 and best_hand > 21:  # if busting, take aces as 1
            best_hand -= 10
            num_aces -= 1

        return best_hand


if __name__ == '__main__':
    hand = [Card("S", 1), Card("H", 7), Card("C", 2)]
    print(*hand)
    print(Game.evaluate_hand(hand))
    for _ in range(5):
        game = Game()
        print(*game.player_hand)
        print(*game.dealer_hand)

        while not game.is_over:
            action = input("ACTION: ")
            game.take_action(action)
            print(*game.player_hand)

        print(f"Dealer hand:", *game.dealer_hand)
        print(game.score)
