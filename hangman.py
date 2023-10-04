from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# List of words for the Hangman game (you can add more words).
''',
    "cat",
    "flamingo",
    "crow",
    "pigeon",
    "dinosaur",
    "lion",
    "giraffe",
    "elephant",
    "tiger",
    "zebra",
    "cheetah",
    "dolphin",
    "kangaroo",
    "crocodile",
    "rhinoceros",
    "chimpanzee",
    "octopus",
    "panda","wolf","rabbit","fox","gorilla"'''
words = ["dog"]

# Initialize game variables.
current_word = ""
guessed_word = ""
max_attempts = 6
attempts_left = max_attempts

def start_new_game():
    global current_word, guessed_word, attempts_left
    current_word = random.choice(words)
    guessed_word = "_ " * len(current_word)
    attempts_left = max_attempts

@app.route("/")
def index():
    return render_template("index.html", guessed_word=guessed_word, attempts_left=attempts_left)

@app.route("/guess", methods=["POST"])
def guess():
    global guessed_word, attempts_left

    if request.method == "POST":
        guess = request.form["guess"]

        if guess in current_word:
            # Update guessed_word with the correctly guessed letter(s).
            for i in range(len(current_word)):
                if current_word[i] == guess:
                    guessed_word = guessed_word[:2 * i] + guess + guessed_word[2 * i + 1:]
        else:
            attempts_left -= 1

        if guessed_word.replace(" ", "") == current_word:
            return render_template("win.html", word=current_word)
        elif attempts_left == 0:
            return render_template("lose.html", word=current_word)

    return redirect(url_for("index"))


@app.route("/play_again", methods=["POST"])
def play_again():
    start_new_game()
    return redirect(url_for("index"))

if __name__ == "__main__":
    start_new_game()
    app.run(debug=True)
