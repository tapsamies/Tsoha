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

@app.route("/signup", methods =["GET","POST"])
def signup():

    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
    if password1!=password2:
        return render_template("error.html", message="Salasanat eivät täsmää")
    hash_value = generate_password_hash(password1)
    try:
        sql = text("INSERT INTO users (username, password, created_at) VALUES (:username, :password, NOW())")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
        return redirect("/")
    except:
        return render_template("error.html", message="Tunnus on jo käytössä")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method =="GET":
        return render_template("login.html")
    if request.method =="POST":
        username = request.form["username"]
        password = request.form["password"]
        sql = text("SELECT id, password, admin FROM users WHERE username=:username")
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()
        if not user:
            return render_template("error.html", message="Tunnus tai salasana väärin")
        else:
            if check_password_hash(user.password, password):
                session["user_id"] = user.id
                session["admin_true"] = user.admin
                return redirect("/")
            else:
                return render_template("error.html", message="Tunnus tai salasana väärin")
            

@app.route("/logout")
def logout():
    del session["user_id"]
    if session["admin_true"]==True:
        del session["admin_true"]
    return redirect("/")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/send", methods=["POST"])
def send():
    user_id = session.get("user_id",0)
    content = request.form["content"]
    sql = text("INSERT INTO messages (content, user_id, sent_at) VALUES (:content, :user_id, NOW())")
    db.session.execute(sql, {"content":content, "user_id":user_id})
    db.session.commit()
    return redirect("/board")

@app.route("/create_category", methods=["POST"])
def create_category():
    user_id = session.get("user_id",0)
    name = request.form["name"]
    public = request.form["public"]
    try:
        sql = text("INSERT INTO categories (name, public) VALUES (:name, :public)")
        db.session.execute(sql, {"name":name, "public":public})
        db.session.commit()
        return redirect("/")
    except:
        return render_template("error.html", message="Nimi käytössä")

@app.route("/result", methods=["GET"])
def result():
    query = request.args["query"]
    sql = text("SELECT id, content FROM messages WHERE content LIKE :query")
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    messages = result.fetchall()
    return render_template("result.html")


@app.route("/board")
def board():
    result = db.session.execute(text("SELECT M.content, U.username, M.sent_at FROM messages M, users U WHERE M.user_id=U.id"))
    messages = result.fetchall()
    return render_template("board.html", count=len(messages),messages=messages)

@app.route("/boards")
def boards():
    result = db.session.execute(text("SELECT id, name FROM categories WHERE public=TRUE"))
    boards = result.fetchall()
    return render_template("boards.html", count=len(boards), boards=boards)

@app.route("/users")
def users():
    result = db.session.execute(text("SELECT id, admin FROM users"))
    users = result.fetchall()
    return render_template("user_list.html", count=len(users),users=users)
