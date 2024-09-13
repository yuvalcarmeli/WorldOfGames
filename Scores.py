import os
from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    points_to_add = (difficulty * 3) + 5
    if os.path.exists(SCORES_FILE_NAME):
        try:
            with open(SCORES_FILE_NAME, 'r') as scoresfile:
                content=scoresfile.read()
            try:
                  score_number = int(content)
            except ValueError:
                  score_number = 0
            score_number += points_to_add
            with open(SCORES_FILE_NAME, 'w') as scoresfile:
                scoresfile.write(str(score_number))
        except BaseException as e:
            print(f"the error: {e}")
    else:
        try:
            with open(SCORES_FILE_NAME, 'w') as scoresfile:
                scoresfile.write(str(points_to_add))
        except BaseException as e:
            print(f"the error: {e}")








