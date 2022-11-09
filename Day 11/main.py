import random
from art import logo

while True:
    user_decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

    if user_decision == "y":
        print(logo)

        game_playing = True

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        def deal_card(cards):
            number_of_cards = len(cards) - 1
            random_card = random.randint(0, number_of_cards)
            return cards[random_card]

        user_cards = []
        computer_cards = []

        for number in range(0, 2):
            user_card = deal_card(cards=cards)
            computer_card = deal_card(cards=cards)
            user_cards.append(user_card)
            computer_cards.append(computer_card)

        def calculate_score(lst):
            if sum(lst) == 21:
                return 0
            for i in range(len(lst)):
                if lst[i] == 11 and sum(lst) > 21:
                    lst[i] = 1
            return sum(lst)

        computer_score = calculate_score(lst=computer_cards)
        user_score = calculate_score(lst=user_cards)

        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        while game_playing == True:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if get_another_card == "y":
                user_cards.append(deal_card(cards=cards))

                computer_score = calculate_score(lst=computer_cards)
                user_score = calculate_score(lst=user_cards)

                print(f" Your cards: {user_cards}, current score: {user_score}")
                print(f" Computer's first card: {computer_cards[0]}")
            if get_another_card == "n":
                while computer_score < 17:
                    computer_cards.append(deal_card(cards=cards))
                    computer_score = calculate_score(lst=computer_cards)
                print(f" Your final hand: {user_cards}, final score: {user_score}")
                print(
                    f" Computer's final hand: {computer_cards}, final score: {computer_score}"
                )
                if computer_score == 0:
                    print("You lose 😤")
                elif user_score == 0:
                    print("You win 😁")
                elif computer_score > 21:
                    print("Opponent went over. You win 😁")
                elif computer_score > user_score:
                    print("You lose 😤")
                    # print("Opponent went over. You win 😁")
                elif user_score > computer_score:
                    print("You win")
                elif computer_score == user_score:
                    print("It's a draw")
                game_playing = False
    else:
        break
