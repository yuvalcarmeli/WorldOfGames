from flask import Flask, render_template
from Utils import SCORES_FILE_NAME

app = Flask(__name__)

@app.route("/")
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as scoresfile:
            score=int(scoresfile.read())
        return render_template('index.html', score=score)
    except FileNotFoundError as e:
        error_message = f"Error: Score file not found: {e}"
        return render_template('index1.html', score=error_message)
    except ValueError as e:
        error_message = f"Error: Invalid score value: {e}"
        return render_template('index1.html', score=error_message)
    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        return render_template('index1.html', score=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)









