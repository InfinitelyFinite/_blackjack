from blackjack_helper_multi import *

no_of_players = int(input("Welcome to Blackjack! How many players? "))
player_names = []
user_hands = []
score = []
game_active = True
for i in range(no_of_players):
    score.append(3)

for i in range(no_of_players):
    player_names.append(input(f"What is player {i+1}'s name? "))

while game_active:
    user_hands = []
    for i in range(len(score)):
        print_header(f"{player_names[i]}'s TURN")
        user_hand_value = 0
        no_of_draws = 0
        while user_hand_value < 21:
            no_of_draws += 1
            user_hand_value += draw_card()
            if user_hand_value >= 21:
                break
            if(no_of_draws>=2):
                hit_or_not = input("You have {}. Hit (y/n)? ".format(user_hand_value))
                while hit_or_not !='y' and hit_or_not!='n':
                    print("Sorry I didn't get that.")
                    hit_or_not = input("You have {}. Hit (y/n)? ".format(user_hand_value))
                if hit_or_not == 'y':
                    continue
                elif hit_or_not == 'n':
                    break
        user_hands.append(user_hand_value)
        print_end_turn_status(user_hand_value)
    print_header("DEALER TURN")
    dealer_hand_value = 0
    no_of_draws = 0
    while dealer_hand_value < 17:
        no_of_draws += 1
        dealer_hand_value += draw_card()
        if dealer_hand_value >= 17:
            break
        if(no_of_draws>=2):
            print("Dealer has {}.".format(dealer_hand_value))
    print_end_turn_status(dealer_hand_value)
    print_multiplayer_end_game_status(player_names = player_names, user_hands = user_hands, dealer_hand = dealer_hand_value, score = score)
    if len(score) == 0:
        game_active = False
    else:
        play_again = input("Do you want to play another hand (y/n)? ")
        while play_again !='y' and play_again!='n':
            print("Sorry I didn't get that.")
            play_again = input("Do you want to play another hand (y/n)? ")
        if play_again == 'y':
            continue
        else:
            game_active = False