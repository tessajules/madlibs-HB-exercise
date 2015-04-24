from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html", person=player, compliments=compliments)

@app.route('/game')
def show_game_form():
    gamechoice = request.args.get("gamechoice")

    if gamechoice == 'no':
        return render_template("goodbye.html")
    elif gamechoice == 'yes':
        return render_template("game.html")

@app.route('/madlib', methods=['GET', 'POST'])
def show_madlib():
    if request.method == 'GET':
        color = request.args.get("color")
        person_name = request.args.get("person_name")
        noun = request.args.get("noun")
        adjective = request.args.get("adjective")
        verbs = request.args.getlist("verbs")
    else:
        color = request.form.get("color")
        person_name = request.form.get("person_name")
        noun = request.form.get("noun")
        adjective = request.form.get("adjective")
        verbs = request.form.getlist('verbs')

    MADLIB_TEMPLATES = ["madlib.html", "madlib2.html"]

    madlib_choice = choice(MADLIB_TEMPLATES)
    print madlib_choice

    return render_template(madlib_choice, color=color, person_name=person_name, noun=noun, adjective=adjective, verbs=verbs)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
