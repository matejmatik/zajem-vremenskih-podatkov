from flask import Blueprint, render_template
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

@views.route('/')
@login_required # Dekorator - da je nujno potrebno biti prijavljen.
def home():
    return render_template("domov.html", uporabnik=current_user)