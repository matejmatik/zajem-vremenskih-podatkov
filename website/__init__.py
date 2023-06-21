from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
PODATKOVNA_BAZA = "vremenski_podatki.db"


def create_app():
    app = Flask(__name__)   # za postavitev "Flaska"
    app.config['SECRET_KEY'] = 'skrivnost'   # za enkripcijo seje in piškotkov
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{PODATKOVNA_BAZA}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #from .models import Uporabnik, VremenskaPostaja, IzbranaPostaja, VremenskiPodatki

    create_database(app)

    return app


def create_database(app):
    if not path.exists('website/' + PODATKOVNA_BAZA):
        with app.app_context():
            db.create_all()
            print('Podatkovna baza je ustvarjena.')
