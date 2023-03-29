from flask import render_template, request
from bookingmanager import app, db


@app.route("/")
def home():
    return render_template("index.html", page_title="About Us")


@app.route("/menu")
def menu():
    return render_template("menu.html", page_title="Menu")


@app.route("/booking", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        print(request.form)
    return render_template("booking.html", page_title="Booking")
