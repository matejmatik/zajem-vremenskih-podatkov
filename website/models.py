from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
# func.now() -- Pridobi trenutni cas.


class Uporabnik(db.Model, UserMixin):
    _id = db.Column(db.Integer, primary_key=True)
    elektronski_naslov = db.Column(db.String(150), unique=True)
    ime = db.Column(db.String(40))
    priimek = db.Column(db.String(50))
    geslo = db.Column(db.String(150))
    izbrane_postaje = db.relationship('IzbranaPostaja') # Uporabimo ime razreda (Z veliko)


class VremenskaPostaja(db.Model):
    pass

class IzbranaPostaja(db.Model):

    # Tuji kljuc
    id_uporabnik = db.Column(db.Integer, db.ForeignKey('uporabnik._id')) # Uporabimo ime razreda (z malo)