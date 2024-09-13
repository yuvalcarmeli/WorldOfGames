from MemoryGame import is_list_equal
from GuessGame import compare_results
from CurrencyRouletteGame import play
def welcome():
    while True:
        try:
            name = input("please Enter your name:")
            if  name.replace(" ", "").replace("-", "").isalpha():
                return (f"hello {name} and welcome to the World Of games (WoG).\n Here you can find many cool games to play.")
            else:
                print("You didn't input a valid name")
        except BaseException as e:
            print(f"error: {e}")


def load_game():
    print("please choose a game to play:")
    print("1.Memory Game-a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2.Guess Game-guess a number and see if you chose like the computer")
    print("3.Currency Roulette-try and guess the value of a random amount of USD in ILS")
    while True:
        try:
            number_of_game = int(input(f"Enter the number of the game you want to play (1-3):"))
            if number_of_game <= 3:
                break
            else:
                print ("please Enter a number between 1-3")
        except BaseException as e:
            print("You didnt enter an integer")
#
    while True:
        try:
            level_of_difficulty = int(input(f"Please choose a game difficulty level (1 to 5):"))
            if level_of_difficulty <= 5:
                break
            else:
                print ("please Enter a number between 1-5")
        except BaseException as e:
            print("You didnt enter an integer")
    if number_of_game == 1:
        is_list_equal(level_of_difficulty)
    elif number_of_game == 2:
        compare_results(level_of_difficulty)
    else:
        play(level_of_difficulty)




