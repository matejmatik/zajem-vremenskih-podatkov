from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, getcwd
from flask_login import LoginManager # LoginManager skrbi za prijavljene uporabniki

pb = SQLAlchemy()
PODATKOVNA_BAZA = "vremenski_podatki_ai.db"


def ustvari_aplikacijo():
    aplikacija = Flask(__name__)   # Za posstavitev "Flaska"
    aplikacija.config['SECRET_KEY'] = 'skrivnost'   # Za enkripcijo seje in piškotkov
    aplikacija.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{PODATKOVNA_BAZA}'
    pb.init_app(aplikacija)

    from .views import views
    from .auth import auth

    aplikacija.register_blueprint(views, url_prefix='/')
    aplikacija.register_blueprint(auth, url_prefix='/')

    from .models import Uporabnik, VremenskaPostaja         # noqa: F401
    from .models import IzbranaPostaja, VremenskiPodatki    # noqa: F401
    ustvari_bazo(aplikacija)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(aplikacija) # Povemo za katero aplikacijo

    @login_manager.user_loader
    def load_user(_id):
        return Uporabnik.query.get(int(_id)) # Metoda .get isce pricakuje primarni kljuc

    return aplikacija


def ustvari_bazo(aplikacija):
    pot = path.join(getcwd(), 'instance', PODATKOVNA_BAZA)
    if not path.exists(pot):
        #print(pot)
        with aplikacija.app_context():
            pb.create_all()
            print('Podatkovna baza je ustvarjena.')

