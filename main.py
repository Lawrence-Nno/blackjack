def blackjack():
    import random
    BlackJack = """
    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
          |  \/ K|                            _/ |                
          `------'                           |__/           
    """

    # A loop that keeps the game running
    game_on = True
    while game_on:
        jack = queen = king = joker = 10
        # List of cards in a deck
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, joker, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, joker,
                 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, joker, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king, joker]

        computer_card_list = []
        player_card_list = []
        computer_hit_choice = ['yes', 'no']
        print(BlackJack)

        # Picks a card from cards at random for computer
        computer_picked_card = random.choice(cards)

        # Appends the picked card to the computer cards list
        computer_card_list.append(computer_picked_card)

        # Removes the picked card from the deck of cards(cards list)
        cards.remove(computer_picked_card)

        # Picks a card from cards at random for the player
        player_picked_card = random.choice(cards)

        # Appends the card to the player's card list
        player_card_list.append(player_picked_card)

        # Removes the picked card from the deck of cards (cards list)
        cards.remove(player_picked_card)

        # Prints the first computer card for all to see.
        print(f"Computer's first card: {computer_card_list[0]}")

        # Prints the player's cards list for him to see
        print(f"Your card: {player_card_list}")

        # This While loop runs if the player wants to keep picking more cards
        while True:
            go_on = input("Type 'hit' to get another card or 'stand' to stop\n")

            # What happens if the player chooses to pick a card more
            if go_on == 'hit':
                player_picked_card = random.choice(cards)
                player_card_list.append(player_picked_card)
                cards.remove(player_picked_card)
                print(f"Your card: {player_card_list}")

                # Computer chooses if he will pick a card or not
                computer_chose_option = random.choice(computer_hit_choice)

                # What happens if the computer chooses to pick a card more
                if computer_chose_option == 'yes':
                    computer_picked_card = random.choice(cards)
                    computer_card_list.append(computer_picked_card)
                    cards.remove(computer_picked_card)
                print(f"Computer's first card: {computer_card_list[0]}")
            else:
                # Sums up the computer's card total and prints it
                print(f"Computer's card: {computer_card_list} : Total = {sum(computer_card_list)}")

                # Sums up the player's card total and prints it
                print(f"Player's Card: {player_card_list} : Total = {sum(player_card_list)}")

                # Calculates who wins the game
                if sum(player_card_list) > 21 and sum(computer_card_list) > 21:
                    print("You both Lose")
                elif (sum(player_card_list) > sum(computer_card_list)) and sum(player_card_list) <= 21:
                    print("You Win!")
                elif (sum(player_card_list) < sum(computer_card_list)) and sum(computer_card_list) <= 21:
                    print("Computer Wins!")
                elif (sum(player_card_list) < sum(computer_card_list)) and sum(computer_card_list) > 21:
                    print("You Win!")
                elif sum(player_card_list) == sum(computer_card_list):
                    print("No winners, It's a draw")
                else:
                    print("Computer Wins!")
                break

        # Asks the player if he/she wants to keep playing
        game = input("Do you wish to play again? Type 'yes' or 'no\n")
        if game == 'yes':
            pass
        else:
            game_on = False


if __name__ == '__main__':
    blackjack()
