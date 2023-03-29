import os
from bookingmanager import app
from flask import Flask, render_template, request, flash

if os.path.exists("env.py"):
    import env

app.secret_key = os.environ.get("SECRET_KEY")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
