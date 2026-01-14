import random

def get_user_choice():
    choice = input("Choose Rock, Paper, or Scissors: ").lower()
    if choice in ['rock', 'paper', 'scissors']:
        return choice
    else:
        print("Invalid choice. Try again.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user = get_user_choice()
        computer = get_computer_choice()

        print(f"\nYou chose: {user}")
        print(f"Computer chose: {computer}")
        result = determine_winner(user, computer)
        print(result)

        if "You win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"Score → You: {user_score} | Computer: {computer_score}")

        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_game()
