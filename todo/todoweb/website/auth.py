from os import name
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    data = request.form
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Log Out</p>"

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 5:
            flash("Email must be longer than 5 characters.", category="Error")
        elif len(firstName) < 3:
            flash("Name must be longer than 3 characters.", category="Error")
        elif len("password 1") < 8:
            flash("Password must be longer than 7 characters.", category="Error")
        elif password1 != password2:
            flash("Passwords do not match.", category="Error")
        else:
            flash("Account created!", category="Confirm")

    return render_template("sign_up.html")
