from flask import Flask, request, render_template, redirect, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "panda"

# Configure MySQL connection
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Aneesh123"
app.config["MYSQL_DB"] = "the_app"

# Initialize MySQL
mysql = MySQL(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # Check if the username or email is already registered
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM users WHERE username = %s OR email = %s", (username, email)
        )
        existing_user = cur.fetchone()

        if existing_user:
            return "Username or email is already registered."

        # If the username and email are not already registered, insert the new user
        cur.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, password),
        )
        mysql.connection.commit()
        cur.close()

        return "Form Submitted"

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute("SELECT password FROM users WHERE username = %s", (username,))
        tocheck = cur.fetchone()
        cur.close()

        if tocheck and password == tocheck[0]:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return "Incorrect password or username"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "username" in session:
        username = session["username"]
        return render_template("dashboard.html", username=username)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


@app.route("/slots")
def select_slot():
    if "username" not in session:
        return redirect(url_for("login"))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM FacultySlots")
    slots = cur.fetchall()
    cur.close()

    return render_template("slots.html", slots=slots)


@app.route("/submit", methods=["POST"])
def submit_slots():
    selected_slots = request.form.getlist("slot")
    username = session.get("username")

    cur = mysql.connection.cursor()

    for slot_id in selected_slots:
        cur.execute(
            "SELECT * FROM SelectedSlots s JOIN FacultySlots f ON s.slot_id = f.id WHERE f.id = %s AND s.username = %s",
            (slot_id, username),
        )
        existing_entry = cur.fetchone()
        if existing_entry:
            return "You have already selected a slot for this subject and type combination."

    for slot_id in selected_slots:
        cur.execute(
            "SELECT f.subject, f.type, f.slots FROM SelectedSlots s JOIN FacultySlots f ON s.slot_id = f.id WHERE s.username = %s",
            (username,),
        )
        existing_slots = cur.fetchall()
        for existing_slot in existing_slots:
            if any(slot in existing_slot[2] for slot in selected_slots):
                return "You have already selected a slot that overlaps with an existing selection."

    for slot_id in selected_slots:
        cur.execute(
            "INSERT INTO SelectedSlots (slot_id, username) VALUES (%s, %s)",
            (slot_id, username),
        )

    mysql.connection.commit()
    cur.close()

    return redirect(url_for("show_slots"))


@app.route("/show_slots")
def show_slots():
    username = session.get("username")

    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT f.subject, f.type, f.faculty, f.slots \
                      FROM SelectedSlots s \
                      JOIN FacultySlots f ON s.slot_id = f.id \
                      WHERE s.username = %s",
        (username,),
    )
    selected_slots = cur.fetchall()
    cur.close()

    return render_template(
        "selected_slots.html", selected_slots=selected_slots, username=username
    )


if __name__ == "__main__":
    app.run(debug=True)
