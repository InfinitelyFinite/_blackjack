from random import randint

# Prints the given card's official name in the form "Drew a(n) ___".
# If the input card is invalid, prints "BAD CARD"
# 
# Parameters:
#   card_rank: The numeric representation of a card (1-13)
#
# Return:
#   none
def print_card_name(card_rank):
    # Implement card_name function here
    if card_rank == 1:
    # A 1 stands for an ace.
        card_name = "Ace"
    elif card_rank == 11:
    # An 11 stands for a jack.
        card_name = "Jack"
    elif card_rank == 12:
    # A 12 stands for a queen.
        card_name = "Queen"
    elif card_rank == 13:
    # A 13 stands for a king.
        card_name = "King"
    else:
    # All other cards are named by their
    # number, or rank.
        card_name = str(card_rank)

    if card_rank == 1 or card_rank == 8:
        drew_prefix = 'Drew an '
    else:
        drew_prefix = 'Drew a '

    if card_rank < 1 or card_rank > 13:
        print('BAD CARD')
    else:
        print(drew_prefix + card_name)

# Draws a new random card, prints its name, and returns its value.
# 
# Parameters:
#   none
#
# Return:
#   an int representing the value of the card. All cards are worth
#   the same as the card_rank except Jack, Queen, King, and Ace.
def draw_card():
    # Implement draw_card function here
    card_rank = randint(1, 13)
    if card_rank == 11 or card_rank == 12 or card_rank == 13:
        # Jacks, Queens, and Kings are worth 10.
        card_value = 10
    elif card_rank == 1:
        # Aces are worth 11.
        card_value = 11
    else:
        # All other cards are worth the same as their rank.
        card_value = card_rank
    print_card_name(card_rank=card_rank)
    return card_value
# Prints the given message formatted as a header. A header looks like:
# -----------
# message
# -----------
# 
# Parameters:
#   message: the string to print in the header
#
# Return:
#   none
def print_header(message):
    # Implement print_header function here
    print(f"-----------\n{message}\n-----------")
# Prints turn header and draws a starting hand, which is two cards.
# 
# Parameters:
#   name: The name of the player whose turn it is.
#
# Return:
#   The hand total, which is the sum of the two newly drawn cards.
def draw_starting_hand(name):
    # Implement draw_starting_hand function here
    print_header(name+" TURN")
    hand_value = draw_card()
    hand_value += draw_card()
    return hand_value

# Prints the hand total and status at the end of a player's turn.
# 
# Parameters:
#   hand_value: the sum of all of a player's cards at the end of their turn.
#
# Return:
#   none
def print_end_turn_status(hand_value):
    # Implement print_end_turn_status function here
    print("Final hand: {}.".format(hand_value))
    if hand_value == 21:
        print('BLACKJACK!')
    elif hand_value > 21 and hand_value <= 31:
        print('BUST.')
    elif hand_value > 31 or hand_value < 4:
        print('BAD HAND VALUE!')
# Prints the end game banner and the winner based on the final hands.
# 
# Parameters:
#   user_hand: the sum of all cards in the user's hand
#   dealer_hand: the sum of all cards in the dealer's hand
#
# Return:
#   none
def print_end_game_status(user_hand, dealer_hand):
    # Implement print_end_game_status function here
    print_header("GAME RESULT")
    if user_hand>21:
        print("Dealer wins!")
    elif user_hand == 21 and dealer_hand!=21:
        print("You win!")
    elif user_hand<=21 and dealer_hand>21:
        print("You win!")
    elif user_hand<=21 and dealer_hand<=21:
        if user_hand>dealer_hand:
            print("You win!")
        elif dealer_hand>user_hand:
            print("Dealer wins!")
        else:
            print("Push.")

def print_multiplayer_end_game_status(player_names, user_hands, dealer_hand, score):
    print_header("GAME RESULT")
    players_to_remove = []
    for i in range(len(user_hands)):
        dealer_win = False
        user_win = False
        push = False
        if user_hands[i]>21:
            dealer_win = True
        elif user_hands[i] == 21 and dealer_hand!=21:
            user_win = True
        elif user_hands[i]<=21 and dealer_hand>21:
            user_win = True
        elif user_hands[i]<=21 and dealer_hand<=21:
            if user_hands[i]>dealer_hand:
                user_win = True
            elif dealer_hand>user_hands[i]:
                dealer_win = True
            else:
                push = True
        if dealer_win:
            score[i] -= 1
            print(f"{player_names[i]} loses! Score: {score[i]}")
            if score[i] == 0:
                print(f"{player_names[i]} eliminated!")
                players_to_remove.append(i)
        if user_win:
            score[i] += 1
            print(f"{player_names[i]} wins! Score: {score[i]}")
        if push:
            print(f"{player_names[i]} pushes. Score: {score[i]}")
    for index in sorted(players_to_remove, reverse = True):
        del player_names[index]
        del score[index]
        del user_hands[index]
    if len(score) == 0:
        print("All players eliminated!")