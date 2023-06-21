from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Uporabnik(db.Model, UserMixin):
    __tablename__ = "uporabnik"

    _id = db.Column(db.Integer, primary_key=True)
    elektronski_naslov = db.Column(db.String(150), unique=True)
    ime = db.Column(db.String(40))
    priimek = db.Column(db.String(50))
    geslo = db.Column(db.String(150))
    izbrane_postaje = db.relationship('IzbranaPostaja') 

class VremenskaPostaja(db.Model):
    __tablename__ = "vremenska_postaja"

    _id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(150), unique=True)
    url = db.Column(db.String(1000)) 

class IzbranaPostaja(db.Model):
    __tablename__ = "izbrana_postaja"

    _id = db.Column(db.Integer, primary_key=True)
    id_uporabnik = db.Column(db.Integer, db.ForeignKey('uporabnik._id')) 
    id_vremenska_postaja = db.Column(db.Integer, 
                                     db.ForeignKey('vremenska_postaja._id')) 
    
class VremenskiPodatki(db.Model):
    __tablename__ = "vremenski_podatki"

    _id = db.Column(db.Integer, primary_key=True)
    datum = db.Column(db.Date)
    cas = db.Column(db.Time) 
    datum_cas_sistem = db.Column(db.DateTime(timezone=True), default=func.now())
    temperatura = db.Column(db.Float)
    relativna_vlaznost = db.Column(db.Float)
    smer_vetra = db.Column(db.String(2))
    hitrost_vetra = db.Column(db.Float)
    padavine = db.Column(db.Float)
    vsota_padavin = db.Column(db.Float)
    id_vremenska_postaja = db.Column(db.Integer, 
                                     db.ForeignKey('vremenska_postaja._id')) 