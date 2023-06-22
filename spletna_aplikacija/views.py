from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Uporabnik, VremenskaPostaja, VremenskiPodatki
from . import pb
from datetime import datetime


views = Blueprint('views', __name__)

@views.route('/')
@login_required # Dekorator - da je nujno potrebno biti prijavljen.
def home():
    
    sql = pb.select(Uporabnik).join(
        Uporabnik.izbrane_postaje).where(
            Uporabnik._id == current_user._id)
        
    podatki = pb.session.execute(sql).fetchall()
    izbrane_postaje = []
    for i, zapis in enumerate(podatki):
        izbrane_postaje.append(zapis[0].izbrane_postaje[i].id_vremenska_postaja)
    
    #print(izbrane_postaje)   
    
    sql = pb.select(VremenskaPostaja).join(
        VremenskaPostaja.vremenski_podatki).where((VremenskaPostaja._id.in_(izbrane_postaje))).distinct()
    
    podatki = pb.session.execute(sql).fetchall()

    vremenski_podatki = []
    
    
    for zapis in podatki:
        vremenski_podatki.append({
            "ime": zapis[0].ime, 
            "datum": datetime.strptime(str(zapis[0].vremenski_podatki[-1].datum), 
                                  '%Y-%m-%d').strftime("%d.%m.%Y"),
            "cas": zapis[0].vremenski_podatki[-1].cas,
            "temperatura": zapis[0].vremenski_podatki[-1].temperatura,
            "relativna_vlaznost": zapis[0].vremenski_podatki[-1].relativna_vlaznost,
            "padavine": zapis[0].vremenski_podatki[-1].padavine,
            "hitrost_vetra": zapis[0].vremenski_podatki[-1].hitrost_vetra        
            })

    
        
    #print(vremenski_podatki)
    return render_template("domov.html", 
                           uporabnik=current_user, 
                           vremenski_podatki=vremenski_podatki)