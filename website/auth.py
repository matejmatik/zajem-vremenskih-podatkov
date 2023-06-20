from flask import Blueprint, render_template


auth = Blueprint('auth', __name__)


@auth.route('/prijava')
def login():
    return render_template("prijava.html")


@auth.route('/odjava')
def logout():
    return "<p>Odjava</p>"


@auth.route('/registracija')
def sign_up():
    return render_template("registracija.html")