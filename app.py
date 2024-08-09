from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Initialize the game variables
number_to_guess = random.randint(1, 100)
attempts = 0
lower_bound = 1
upper_bound = 100

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    global number_to_guess, attempts, lower_bound, upper_bound
    guess = int(request.form['guess'])
    attempts += 1

    if guess < lower_bound or guess > upper_bound:
        return jsonify(message=f"Please enter a number between {lower_bound} and {upper_bound}.", lower_bound=lower_bound, upper_bound=upper_bound, success=False)

    if guess < number_to_guess:
        lower_bound = guess + 1
        return jsonify(message="Too low!", lower_bound=lower_bound, upper_bound=upper_bound, success=False)
    elif guess > number_to_guess:
        upper_bound = guess - 1
        return jsonify(message="Too high!", lower_bound=lower_bound, upper_bound=upper_bound, success=False)
    else:
        return jsonify(message=f"Congratulations! You guessed the number {number_to_guess} correctly in {attempts} attempts.", success=True)

if __name__ == "__main__":
    app.run(debug=True)
