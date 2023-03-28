from flask import render_template
from bookingmanager import app, db


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")
