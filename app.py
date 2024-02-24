from flask import Flask, render_template, redirect, url_for, request, session,jsonify
from officialmodel import BardGenerator
from flask_session import Session
import datetime
import requests

app = Flask(__name__)
app.secret_key = "BADKEY"
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(minutes=2)
Session(app)

isYadla=True

def go_to_login():
    if(isYadla):
        return False
    if "uname" not in session or not session.get("uname"):
        return True
    else:
        return False

@app.route('/', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        session["uname"] = request.form.get("uname")
        session["pswd"] = request.form.get("pswd")
        return redirect(url_for('index'))
    if(isYadla):
        return render_template("index.html")
    return render_template("login.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["uname"] = request.form.get("uname")
        session["pswd"] = request.form.get("pswd")
        if session["uname"] == "username" and session["pswd"] == "password":
            return redirect(url_for('index'))
    return render_template("login.html")

@app.route("/index")
def index():
    if go_to_login():
        return redirect(url_for('login'))
    return render_template("index.html")

@app.route("/timer")
def timer():
    if go_to_login():
        return redirect(url_for('login'))
    return render_template("pomo.html")

@app.route("/flash")
def flash():
    if go_to_login():
        return redirect(url_for('login'))
    return render_template("quiz.html")

@app.route("/quizform")
def quizform():
    if go_to_login():
        return redirect(url_for('login'))
    return render_template("quizform.html")

@app.route('/generate_quiz', methods=["POST"])
def generate_quiz():
    topic = request.form.get("topic")
    difficulty = request.form.get("difficulty")

    # Call your API or function to generate questions based on topic and difficulty
    bard = BardGenerator()
    bard.generate_questions_from_text_mcq(topic, difficulty)
    questions = bard.questions

    return jsonify(questions)

# ... (existing code)

# Update the existing quiz route to handle both GET and POST requests
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if go_to_login():
        return redirect(url_for('login'))

    if request.method == "POST":
        # Redirect to the quiztemp.html with the provided topic and difficulty
        return redirect(url_for('quiztemp', topic=request.form.get("topic"), difficulty=request.form.get("difficulty")))

    return render_template("quizform.html")

# Add a new route for quiztemp that takes topic and difficulty as parameters
@app.route("/quiztemp")
def quiztemp():
    if go_to_login():
        return redirect(url_for('login'))

    # Retrieve topic and difficulty from the URL parameters
    topic = request.args.get("topic")
    difficulty = request.args.get("difficulty")

    # Call the API endpoint to get questions based on the provided topic and difficulty
    response = requests.post('http://127.0.0.1:5000/generate_quiz', data={"topic": topic, "difficulty": difficulty})
    questions = response.json()

    return render_template("quiztemp.html", questions=questions)



if __name__ == '__main__':
    app.run(debug=True)