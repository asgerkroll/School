import random
import logging
import enum

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.WARN)

username = input("What is your name? ")

print(f"Hello {username} this is a game of rock, paper, scissors")

class WhoWon(enum.Enum):
    User = 1
    Hal = 2
    Tie = 3
def user_input():
    while True:
        user_choice = input("Make your choice, rock paper or scissors: ")
        if user_choice.lower() in ["rock", "paper", "scissors"]:
            return user_choice.lower()
        else:
            print("Invalid input, please try again")

def Hal9000_choice(verbose=False):
    choices = ["rock", "paper", "scissors"]
    return_val = random.choice(choices)
    logging.info(f"Hal9000 Choice: {return_val}")
    return return_val

user_score = 0
Hal9000_score = 0

#def display(game=0, )

def get_round_winner(user_choice, Hal9000_choice):
    global user_score
    global Hal9000_score
    logging.info(f"user: {user_score}, HAL9000: {Hal9000_score}")
    tmp_user_choice = user_choice()
    tmp_hal_choice = Hal9000_choice()
    didiwin=False
    didhalwin=False

    if tmp_user_choice == tmp_hal_choice:
        pass
    elif tmp_user_choice == "rock" and tmp_hal_choice == "scissors":
        user_score += 1
        didiwin=True
    elif tmp_user_choice == "scissors" and tmp_hal_choice == "paper":
        user_score += 1
        didiwin=True
    elif tmp_user_choice == "paper" and tmp_hal_choice == "rock":
        user_score += 1
        didiwin=True
    else:
        Hal9000_score += 1
        didhalwin=True
    # DISPLAY OUTPUT
    if didiwin:
        print(f"{str(username)} wins this round, the score is now:\n{username}: {user_score} \nHal9000: {Hal9000_score}")
    elif didhalwin:
        print(f"Hal9000 wins this round, the score is now:\n{username}: {user_score} \nHal9000: {Hal9000_score}")
    else:
        print(f"TIE! You both chose {tmp_user_choice}, the score is now: \n{username}: {user_score} \nHal9000: {Hal9000_score}")


def who_won(user_choice, hal9000_choice):
    if user_choice == hal9000_choice:
        print(f'DRAW')
    elif user_choice == "rock" and hal9000_choice == "scissors":
        print(f'user won')

def start_game():
    input("Press any key, followed by enter, to start game: ")

def endgame():
    global Hal9000_score
    global user_score
    if user_score > Hal9000_score:
        print(f"You win! The final score is:\n{username}: {user_score} \nHal9000: {Hal9000_score}")
    elif Hal9000_score > user_score:
        print(f"You lose! The final score is:\n{username}: {user_score} \nHal9000: {Hal9000_score}")
    else:
        print(f"TIE! The final score is:\n{username}: {user_score} \nHal9000: {Hal9000_score}")

start_game()
for x in range(5):
    logging.info(f'Game: {x}')
    get_round_winner(user_input, Hal9000_choice)
endgame()
