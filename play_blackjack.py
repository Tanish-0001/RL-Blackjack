from blackjack import Game

while True:
    print("====================================")
    new = input("Would you like to start a new game? (y/n): ")

    if new == "y":
        game = Game(five_card_charlie=True)
        game.dealer_hand[1].hidden = True  # hide dealer's second card
        while not game.is_over:
            print("\nPlayer hand:", *game.player_hand, "\nDealer hand:", *game.dealer_hand)
            print("------------------------------------")
            choice = input("What do you want to do? (h/s): ")
            if choice == "h":
                game.take_action("H")
            elif choice == "s":
                game.take_action("S")
            else:
                print("Invalid choice\n")

        game.dealer_hand[1].hidden = False  # reveal dealer's card
        print("\nPlayer hand:", *game.player_hand, "\nDealer hand:", *game.dealer_hand)
        print(f"\nYour total: {game.evaluate_hand(game.player_hand)}\nDealer's total: {game.evaluate_hand(game.dealer_hand)}")
        if game.score == 1:
            print("\nYou won!\n")
        elif game.score == 0:
            print("\nYou tied with the dealer.\n")
        else:
            print("\nYou lost.\n")
    else:
        break
