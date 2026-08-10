from blackjack import Environment

while True:
    print("====================================")
    new = input("Would you like to start a new game? (y/n): ")

    if new == "y":
        env = Environment(five_card_charlie=True)
        env.dealer_hand[1].hidden = True  # hide dealer's second card
        while not env.is_over:
            print("\nPlayer hand:", *env.player_hand, "\nDealer hand:", *env.dealer_hand)
            print("------------------------------------")
            choice = input("What do you want to do? (h/s): ")
            if choice == "h":
                env.step("H")
            elif choice == "s":
                env.step("S")
            else:
                print("Invalid choice\n")

        env.dealer_hand[1].hidden = False  # reveal dealer's card
        print("\nPlayer hand:", *env.player_hand, "\nDealer hand:", *env.dealer_hand)
        print(f"\nYour total: {env.evaluate_hand(env.player_hand)}\nDealer's total: {env.evaluate_hand(env.dealer_hand)}")
        if env.score == 1:
            print("\nYou won!\n")
        elif env.score == 0:
            print("\nYou tied with the dealer.\n")
        else:
            print("\nYou lost.\n")
    else:
        break
