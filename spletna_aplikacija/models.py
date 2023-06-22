from . import pb
from flask_login import UserMixin
from sqlalchemy.sql import func

class Uporabnik(pb.Model, UserMixin):
    __tablename__ = "uporabnik"

    _id = pb.Column(pb.Integer, primary_key=True, autoincrement=True)
    elektronski_naslov = pb.Column(pb.String(150), unique=True)
    ime = pb.Column(pb.String(40))
    priimek = pb.Column(pb.String(50))
    geslo = pb.Column(pb.String(150))
    izbrane_postaje = pb.relationship('IzbranaPostaja')

    def get_id(self):
        # Metoda za vracanje id-ja.
        return (self._id) 

class VremenskaPostaja(pb.Model):
    __tablename__ = "vremenska_postaja"

    _id = pb.Column(pb.Integer, primary_key=True, autoincrement=True)
    ime = pb.Column(pb.String(150), unique=True)
    url = pb.Column(pb.String(1000))
    vremenski_podatki = pb.relationship('VremenskiPodatki') 

    def get_id(self):
        # Metoda za vracanje id-ja.
        return (self._id) 

class IzbranaPostaja(pb.Model):
    __tablename__ = "izbrana_postaja"

    _id = pb.Column(pb.Integer, primary_key=True, autoincrement=True)
    id_uporabnik = pb.Column(pb.Integer, 
                             pb.ForeignKey('uporabnik._id')) 
    id_vremenska_postaja = pb.Column(pb.Integer, 
                                     pb.ForeignKey('vremenska_postaja._id')) 
    
    def get_id(self):
        # Metoda za vracanje id-ja.
        return (self._id) 
    
class VremenskiPodatki(pb.Model):
    __tablename__ = "vremenski_podatki"

    _id = pb.Column(pb.Integer, primary_key=True, autoincrement=True)
    datum = pb.Column(pb.Date)
    cas = pb.Column(pb.Time) 
    datum_cas_sistem = pb.Column(pb.DateTime(timezone=True), default=func.now())
    temperatura = pb.Column(pb.Float)
    relativna_vlaznost = pb.Column(pb.Float)
    smer_vetra = pb.Column(pb.String(2))
    hitrost_vetra = pb.Column(pb.Float)
    padavine = pb.Column(pb.Float)
    vsota_padavin = pb.Column(pb.Float)
    id_vremenska_postaja = pb.Column(pb.Integer, 
                                     pb.ForeignKey('vremenska_postaja._id')) 
    
    def get_id(self):
        # Metoda za vracanje id-ja.
        return (self._id) 