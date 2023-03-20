import random

username = input("What is your name? ")

print(f"Hello {username} this is a game of rock, paper, scissors")

def user_input():
    while True:
        user_choice = input("Make your choice, rock paper or scissors: ")
        if user_choice.lower() in ["rock", "paper", "scissors"]:
            return user_choice.lower()
        else:
            print("Invalid input, please try again")

def Hal9000_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

user_score = 0
Hal9000_score = 0

def get_round_winner(user_choice, Hal9000_choice):
    global user_score
    global Hal9000_score
    if user_choice == Hal9000_choice():
        print(f"TIE! You both chose {str(user_choice)}, the score is now: \n{username}: {user_score} \nHal9000: {Hal9000_score}")
    elif user_choice() == "rock" and Hal9000_choice() == "scissors":
        user_score += 1
        print(f"{str(username)} wins this round, the score is now:\n{username}: {user_score} \nHal9000: {Hal9000_score}")
    elif user_choice() == "scissors" and Hal9000_choice() == "paper":
        user_score += 1
        print(f"{str(username)} wins this round, the score is now:\n{username}: {user_score} \nHal9000: {Hal9000_score}")
    elif user_choice() == "paper" and Hal9000_choice() == "rock":
        user_score += 1
        print(f"{str(username)} wins this round, the score is now:\n{username}: {user_score} \nHal9000: {Hal9000_score}")
    else:
        Hal9000_score += 1
        print(f"Hal9000 wins this round, the score is now:\n{username}: {user_score} \nHal9000: {Hal9000_score}")

def start_game():
    input("Press any key, followed by enter, to start game: ")

def endgame():
    global Hal9000_score
    global user_score
    if user_score == 5:
        print(f"You win! The final score is:\n{username}: {user_score} \nHal9000: {Hal9000_score}")
    elif Hal9000_score == 5:
        print(f"You lose! The final score is:\n{username}: {user_score} \nHal9000: {Hal9000_score}")

start_game()
for x in range(5):
    get_round_winner(user_input, Hal9000_choice)
endgame()
