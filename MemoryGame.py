import random
from time import sleep
from Scores import add_score
from Utils import screen_cleaner

def generate_sequence(difficulty):
    list_number = []
    for i in range(difficulty):
        random_number = int(random.randrange(1,101))
        list_number.append(random_number)
    return list_number

def get_list_from_user(difficulty):
    list_number_from_user = []
    for i in range(difficulty):
        try:
            number_user = int(input("please enter a number to insert to the list:"))
            list_number_from_user.append(number_user)
        except BaseException as e:
            print("you didnt enter an integer")
            number_user = int(input("please enter a number:"))
            list_number_from_user.append(number_user)
    return list_number_from_user


def is_list_equal(difficulty):
    random_list_number = generate_sequence(difficulty)
    print(random_list_number)
    sleep(0.7)
    print("\n" * 100)
    screen_cleaner()
    user_list_number = get_list_from_user(difficulty)
    if random_list_number == user_list_number:
        add_score(difficulty)
    else:
        print("False")