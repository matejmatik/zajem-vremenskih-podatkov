from flask import Blueprint


auth = Blueprint('auth', __name__)


@auth.route('/prijava')
def login():
    return "<p>Login</p>"


@auth.route('/odjava')
def logout():
    return "<p>Logout</p>"


@auth.route('/registracija')
def sign_up():
    return "<p>Sign up</p>"