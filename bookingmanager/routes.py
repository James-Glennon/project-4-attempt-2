from flask import render_template
from bookingmanager import app, db


@app.route("/")
def home():
    return render_template("index.html", page_title="About Us")


@app.route("/menu")
def menu():
    return render_template("menu.html", page_title="Menu")


@app.route("/booking")
def booking():
    return render_template("booking.html", page_title="Booking")

