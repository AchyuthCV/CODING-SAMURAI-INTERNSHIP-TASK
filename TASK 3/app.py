import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "secret123"


# ---------- DATABASE ----------
def get_db():
    return sqlite3.connect("database.db")


def init_db():
    db = get_db()
    cursor = db.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    # Posts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            user_id INTEGER
        )
    """)

    db.commit()
    db.close()



init_db()
# -----------------------------


# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password)

        db = get_db()
        cursor = db.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )
            db.commit()
        except sqlite3.IntegrityError:
            return "Username already exists!"
        finally:
            db.close()

        return redirect(url_for("home"))

    return render_template("register.html")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        db.close()

        if user and check_password_hash(user[2], password):
            session["user_id"] = user[0]
            session["username"] = user[1]
            return redirect(url_for("dashboard"))
        else:
            return "Invalid username or password"

    return render_template("login.html")
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")
@app.route("/create", methods=["GET", "POST"])
def create_post():
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]

        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)",
            (title, content, session["user_id"])
        )
        db.commit()
        db.close()

        return redirect(url_for("dashboard"))

    return render_template("create_post.html")
@app.route("/posts")
def view_posts():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    db.close()

    return render_template("posts.html", posts=posts)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))



# -----------------------------


if __name__ == "__main__":
    app.run(debug=True)
