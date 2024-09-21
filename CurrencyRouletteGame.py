import requests
from Scores import add_score
import random

def get_money_interval(difficulty):
    url = 'https://v6.exchangerate-api.com/v6/a384ee03308df33256c0d601/latest/USD'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    exchange_rate = data['conversion_rates']['ILS']
    random_usd_amount = random.randint(1, 100)
    converted_amount =round(random_usd_amount * exchange_rate, 2)
    lower_bound = converted_amount - 5 - difficulty
    upper_bound = converted_amount + 5 - difficulty
    return lower_bound , upper_bound

def get_guess_from_user():
    while True:
        try:
            guess_user = int(input(f"what is the value of the generated number from USD to ILS:"))
            return guess_user
        except BaseException as e:
            print(f"you didnt enter an integer")


def play(difficulty):
    user_guess = get_guess_from_user()
    Lowest_range,Highest_range = get_money_interval(difficulty)
    if Lowest_range <= user_guess <= Highest_range:
        add_score(difficulty)
    else:
        print("False")

