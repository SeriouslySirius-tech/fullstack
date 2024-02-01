from flask import Flask, render_template, redirect, url_for, request, session
from officialmodel import BardGenerator
from flask_session import Session
import datetime

# import databasemanagement as database

app = Flask(__name__)
app.secret_key = "BADKEY"
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(minutes=10)   
Session(app)


def go_to_login():
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
        # db.show_users()
        return redirect(url_for('index'))
    print()
    return render_template("login.html")

@app.route('/login', methods =["GET", "POST"])
def login():
    if request.method == "POST": 
        session["uname"] = request.form.get("uname")
        session["pswd"] = request.form.get("pswd") 
        if (session["uname"] == "username" and session["pswd"] == "password"):
            return redirect(url_for('index'))  
        else:
            pass
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

@app.route("/quiz")
def quiz():
    if go_to_login():
        return redirect(url_for('login'))
    return render_template("quiz.html")

@app.route("/flash")
def flash():
    if go_to_login():
        return redirect(url_for('login'))
    return render_template("flash.html")
# @app.route("/flash")
# def flashcards():
#     return render_template("flash.html")

# @app.route("/<username>/flash/direct")
# def generate_question(topic):
#     pass
if __name__=='__main__':
   app.run(debug=True)  