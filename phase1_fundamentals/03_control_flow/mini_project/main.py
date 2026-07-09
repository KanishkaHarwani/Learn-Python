import random

# Declaring global variables
player_score = 0
computer_score = 0

# valid moves
moves = ("rock", "paper", "scissors")

print("=== Rock Paper Scissors ===")
print("Commands:")
print("  rock")
print("  paper")
print("  scissors")
print("  reset")
print("  quit")


# Main Game Loop
while True:
    player_move = input("\nEnter your move: ").strip().lower()

    match player_move:
        case "quit":
            print("\nFinal Scores")
            print(f"Player   : {player_score}")
            print(f"Computer : {computer_score}")
            print("Thanks for playing!")
            break

        case "reset":
            player_score = 0
            computer_score = 0
            print("Scores have been reset.")
            continue

        case "rock" | "paper" | "scissors":
            pass

        case _:
            print("Invalid input. Please enter rock, paper, scissors, reset, or quit.")
            continue

    # computer moves
    computer_move = random.choice(moves)

    print(f"\nYou chose      : {player_move}")
    print(f"Computer chose : {computer_move}")

    # check round result
    match (player_move, computer_move):

        # Ties
        case ("rock", "rock") | ("paper", "paper") | ("scissors", "scissors"):
            print("It's a tie!")

        # Player wins
        case ("rock", "scissors") | \
             ("paper", "rock") | \
             ("scissors", "paper"):
            player_score += 1
            print("You win this round!")

        # Computer wins
        case _:
            computer_score += 1
            print("Computer wins this round!")


    # Scoreboard
    print("\nCurrent Scores")
    print(f"Player   : {player_score}")
    print(f"Computer : {computer_score}")
