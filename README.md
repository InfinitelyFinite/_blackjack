# Blackjack Game

## Overview
This is a command-line Blackjack game where the player competes against the dealer to reach a hand total as close to 21 as possible without going over. The game follows the basic rules of Blackjack, allowing the player to hit or stand during their turn. The dealer follows the standard Blackjack rule of standing at 17 or higher. The player's and dealer's cards are displayed in a clean format.

## Features
- **Card Display**: Player and dealer cards are displayed in a clean, formatted view.
- **Player Actions**: The player can choose to:
  - Hit (draw another card)
  - Stand (keep their hand as is)
- **Dealer Actions**: The dealer will automatically hit until their hand reaches 17 or higher.
- **Result Announcements**: The game announces the result, including whether the player or dealer busts or achieves a Blackjack.
- **Bust and Blackjack Handling**: If the player or dealer busts, the game ends immediately. If the player hits 21, the player automatically wins without further actions.

## How to Play
1. The game starts by showing the player's hands.
2. The player is prompted to hit or stand. After the player's turn, the dealer's cards are shown and the winner is decided.
3. In multiplayer format, the game continues until user exits the game or they run out of lives.
4. If more than 2 players are playing in multiplayer format, even if one player runs out of lives, the other player(s) can still continue playing.


## Requirements
- Python 3.x
- No external libraries are required.

## How to Run
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/InfinitelyFinite/_blackjack.git
    ```

2. **Navigate to the Project Directory:**
    ```bash
    cd _blackjack
    ```

3. **Run the Game:**
    ```bash
    python blackjack.py
    ```
    *For multiplayer:*
    ```bash
    python blackjack_multi.py
    ```

4. **Run the Tests:**
     ```bash
    pytest
    ```

## Future Improvements
- Adding a betting system to the game.
- Implementing a graphical user interface (GUI) using a library like Pygame.
- Enhancing the AI of the dealer for more strategic gameplay.
