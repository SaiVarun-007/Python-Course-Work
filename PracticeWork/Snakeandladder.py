import random
import time

# Board setup
snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def roll_dice():
    return random.randint(1, 6)

def move_player(position):
    new_position = position
    dice = roll_dice()
    print(f"Rolled: {dice}")
    new_position += dice
    if new_position > 100:
        print("Can't move, need the exact number to finish.")
        return position
    if new_position in snakes:
        print(f"Oops! Landed on a snake at {new_position}, down to {snakes[new_position]}")
        new_position = snakes[new_position]
    elif new_position in ladders:
        print(f"Yay! Climbed a ladder from {new_position} to {ladders[new_position]}")
        new_position = ladders[new_position]
    return new_position

def play_game():
    player_positions = [0, 0]
    player_names = ["Player 1", "Player 2"]
    turn = 0
    while True:
        input(f"{player_names[turn]}'s turn. Press Enter to roll the dice...")
        player_positions[turn] = move_player(player_positions[turn])
        print(f"{player_names[turn]} is now at {player_positions[turn]}\n")
        if player_positions[turn] == 100:
            print(f"Congratulations! {player_names[turn]} wins!")
            break
        turn = 1 - turn  # Swap turns

if __name__ == "__main__":
    play_game()
