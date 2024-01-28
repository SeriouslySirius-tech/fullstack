from flask import Flask, render_template, redirect, url_for, request
from officialmodel import BardGenerator
import databasemanagement as database

app = Flask(__name__)
db = database.DBManager()

@app.route('/', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        uname = request.form.get("uname")
        pswd = request.form.get("pswd")
        print(request.form)
        print(name, uname, pswd)
        # db.say_hello()
        # db.add_user(name, uname, pswd)
        # db.show_users()
        return redirect(url_for('index'))
    return render_template("login.html")

@app.route('/login', methods =["GET", "POST"])
def login():
    if request.method == "POST": 
        username = request.form.get("uname")
        pswd = request.form.get("pswd") 
        print(username, pswd)
        if (username == "username" and pswd == "password"):
            return redirect(url_for('index'))  
        else:
            message = "Wrong username or Password"    
    return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")
# @app.route("/flash")
# def flashcards():
#     return render_template("flash.html")

# @app.route("/<username>/flash/direct")
# def generate_question(topic):
#     pass
if __name__=='__main__':
   app.run(debug=True)  