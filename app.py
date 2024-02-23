from flask import Flask, render_template, redirect, url_for, request, session,jsonify
from officialmodel import BardGenerator
from flask_session import Session
import datetime

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

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if go_to_login():
        return redirect(url_for('login'))

    if request.method == "POST":
        bard = BardGenerator()
        topic = request.form.get("topic")
        difficulty = request.form.get("difficulty")
        bard.generate_questions_from_text_mcq(topic, difficulty)
        questions = bard.questions
        return render_template("quiztemp.html", questions=questions)

    return render_template("quizform.html")

@app.route('/quizform', methods=["GET", "POST"])
def quizform():
    if go_to_login():
        return redirect(url_for('login'))

    if request.method == "POST":
        bard = BardGenerator()
        topic = request.form.get("topic")
        difficulty = request.form.get("difficulty")
        bard.generate_questions_from_text_mcq(topic, difficulty)
        questions = bard.questions
        return render_template("quiztemp.html", questions=questions)

    return render_template("quizform.html")


@app.route('/get_questions', methods=["POST"])
def get_questions():
    if go_to_login():
        return redirect(url_for('login'))

    if request.method == "POST":
        try:
            num_questions = 5
            bard = BardGenerator()
            topic = request.form.get("topic")
            difficulty = request.form.get("difficulty")

            questions = []
            for _ in range(num_questions):
                bard.generate_questions_from_text_mcq(topic, difficulty)
                questions.append(bard.questions)

            return jsonify({"questions": questions})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return render_template("quizform.html")

if __name__ == '__main__':
    app.run(debug=True)