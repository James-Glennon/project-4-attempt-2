from flask import Flask, render_template, request, flash
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
        flash(
            "{}, Thank you for your interest. Your booking request is being processed".format(request.form.get("name")))
        flash("Your requested booking is {}".format(request.form.get("booking-date")))
        flash("At {}".format(request.form.get("booking-time")))
    return render_template("booking.html", page_title="Booking")
