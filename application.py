import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Make sure no blank fields are entered
        if not request.form.get("name") or not request.form.get("month") or not request.form.get("day"):
            return redirect("/")
        else:
            # set variables to inputed data in form
            name = request.form.get("name")
            month = request.form.get("month")
            day = request.form.get("day")

            # place variables into database
            db.execute("INSERT INTO birthdays (name, day, month) VALUES(?, ?, ?)", name, day, month)


        return redirect("/")

    else:

        # select all data from birthdays table in db
        brian = db.execute("SELECT * FROM birthdays")
        # use brian=brian to send that data with render template
        return render_template("index.html", brian=brian)


