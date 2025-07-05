
from flask import Flask
import random
random_num = random.randint(0,9)
print(random_num)

app = Flask(__name__)


@app.route('/')
def home_page():
    return '<h1>Guess the Number between 0 - 9</h1>'\
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
        
@app.route('/<int:guess>')
def Guessed_num(guess):
    if guess < random_num:
        return '<h1>Too low,Try Again</h1>'\
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    if guess > random_num:
        return '<h1>Too high,Try Again</h1>'\
        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1>You Found me</h1>'\
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
            






if __name__ == "__main__":
    app.run(debug=True)