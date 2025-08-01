
from flask import Flask, render_template, request
from app.rps import determine_winner, generate_random_choice


app = Flask(__name__)

# route for home page
@app.route('/')
def home():
    return render_template("home.html")

# route for about page
@app.route('/about')
def about():
    return "THIS IS THE ABOUT PAGE"

# route for results page
@app.route('/results', methods=['POST'])
def results():

    print(request.form)

    # Get the user's choice from the form data
    user_choice = request.form.get('user_choice')

    computer_choice = generate_random_choice()

    outcome = determine_winner(user_choice, computer_choice)

    return render_template("results.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        outcome=outcome
    )

if __name__ == '__main__':

    app.run(debug=True)