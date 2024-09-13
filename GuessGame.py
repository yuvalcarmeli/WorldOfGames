import random
from Scores import add_score
def generate_number(difficulty):
    if difficulty == 1:
        secret_number = 1
        return secret_number
    else:
        secret_number = int(random.randrange(1, difficulty))
        return secret_number

def get_guess_from_user(difficulty):
    while True:
        choose_number= int(input(f"please enter a number between 1 to {difficulty}:"))
        if 1<= choose_number <=difficulty:
            return choose_number
        else:
            print(f"you need to enter a number between 1 to {difficulty}")

def compare_results(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    if secret_number == user_guess:
        add_score(difficulty)
    else:
        print("False")


