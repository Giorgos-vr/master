from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Log In</p>"

@auth.route('/logout')
def logout():
    return "<p>Log Out</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"
