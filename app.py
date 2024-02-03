from flask import Flask
from flask import redirect, render_template, request, session
from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key= getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods =["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    hash_value = generate_password_hash(password)
    sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        #todo
        pass
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            #tot
            pass
        else:
            #invsalid
            pass
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST"])
def send():
    content = request.form["content"]
    sql = text("INSERT INTO messages (content) VALUES (:content)")
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return redirect("/board")

@app.route("/result", methods=["GET"])
def result():
    query = request.args["query"]
    sql = text("SELECT id, content FROM messages WHERE content LIKE :query")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    messages = result.fetchall()
    return render_template("result.html")


@app.route("/board")
def board():
    result = db.session.execute(text("SELECT content FROM messages"))
    messages = result.fetchall()
    return render_template("board.html", count=len(messages),messages=messages)
