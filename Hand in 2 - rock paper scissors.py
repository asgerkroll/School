import random

username = input("What is your name? ")

print(f"Hello {username} this is a game of rock, paper, scissors")


def user_choice():
    Attempts = 0
    while True:
        user_input = input("Make your choice, rock, paper or scissors: ")
        if user_input.lower() in ["rock", "paper", "scissors"]:
            return user_input.lower()
        elif Attempts < 2:
            print("Invalid input, please try again")
            Attempts += 1
        elif Attempts in range(2, 6):
            print("Come on, its rock, paper, scissors, not a spelling contest for dyslexic monkeys")
            Attempts += 1
        else:
            print("Alright im done, come back when you know how to use a keyboard")
            exit(1)

def Hal9000_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


user_score = 0
Hal9000_score = 0


def game_analysis():
    global user_score
    global Hal9000_score
    temp_user_choice = user_choice()
    temp_hal9000_choice = Hal9000_choice()
    user_win = False
    Hal9000_win = False
    if temp_user_choice == temp_hal9000_choice:
        pass
    elif temp_user_choice == "rock" and temp_hal9000_choice == "scissors":
        user_score += 1
        user_win = True
    elif temp_user_choice == "scissors" and temp_hal9000_choice == "paper":
        user_score += 1
        user_win = True
    elif temp_user_choice == "paper" and temp_hal9000_choice == "rock":
        user_score += 1
        user_win = True
    else:
        Hal9000_score += 1
        Hal9000_win = True
    # Output of round winner
    if user_win:
        print(
            f"{str(username)} wins this round, the score is now:\n{username}: {user_score} \nHal9000: {Hal9000_score}")
    elif Hal9000_win:
        print(
            f"Hal9000 wins this round, the score is now:\n{username}: {user_score} \nHal9000: {Hal9000_score}")
    else:
        print(
            f"TIE! you both chose {temp_user_choice},the score is now:\n{username}: {user_score} \nHal9000: {Hal9000_score}")


def start_game():
    input("Press any key, followed by enter, to start game: ")


def endgame():
    global Hal9000_score
    global user_score
    if user_score == 3:
        print(f"You win! The final score is:\n{username}: {user_score} \nHal9000: {Hal9000_score}")
    elif Hal9000_score == 3:
        print(f"You lose! The final score is:\n{username}: {user_score} \nHal9000: {Hal9000_score}")


start_game()
while user_score < 3 and Hal9000_score < 3:
    game_analysis()
endgame()
