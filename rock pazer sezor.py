import random

choices = ["rock", "paper", "scissors"]

def get_ai_choice():
    return random.choice(choices)

def determine_winner(player, ai):
    if player == ai:
        return "It's a tie!"
    elif (
        (player == "rock" and ai == "scissors") or
        (player == "paper" and ai == "rock") or
        (player == "scissors" and ai == "paper")
    ):
        return "You win!"
    else:
        return "AI wins!"

print("Rock Paper Scissors with AI")
print("Type 'quit' to exit.")

player_score = 0
ai_score = 0

while True:
    player = input("\nChoose rock, paper, or scissors: ").lower()

    if player == "quit":
        break

    if player not in choices:
        print("Invalid choice. Try again.")
        continue

    ai = get_ai_choice()

    print(f"AI chose: {ai}")

    result = determine_winner(player, ai)
    print(result)

    if result == "You win!":
        player_score += 1
    elif result == "AI wins!":
        ai_score += 1

    print(f"Score — You: {player_score} | AI: {ai_score}")

print("\nThanks for playing!")
print(f"Final Score — You: {player_score} | AI: {ai_score}")
