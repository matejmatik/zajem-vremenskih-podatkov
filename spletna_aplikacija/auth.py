from flask import Blueprint, flash, render_template, request, redirect, url_for
from .models import Uporabnik
from . import pb
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/prijava', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        elektronski_naslov = request.form.get('elektronski_naslov')
        geslo  = request.form.get('geslo')

        # Poizvedba
        uporabnik = Uporabnik.query.filter_by(elektronski_naslov=elektronski_naslov).first()
        # Ce smo dobili uporabnika ...
        if uporabnik:
            if check_password_hash(uporabnik.geslo, geslo):
                flash('Uspešno si se prijavil', category='success')
                login_user(uporabnik, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Nepravilno geslo. Poskusi znova.', category='error')
        else: 
            flash('Ta elektronski naslov ne obstaja!', category='error')
        
    return render_template("prijava.html", uporabnik=current_user)


@auth.route('/odjava')
@login_required # Dekorator - da je nujno potrebno biti prijavljen.
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/registracija', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        elektronski_naslov = request.form.get('elektronski_naslov')
        ime = request.form.get('ime')
        priimek = request.form.get('priimek')
        geslo1 = request.form.get('geslo1')
        geslo2 = request.form.get('geslo2')

        uporabnik = Uporabnik.query.filter_by(elektronski_naslov=elektronski_naslov).first()
        if uporabnik:
            flash('Uporabnik s tem elektronskim naslovom že obstaja.', category='error')    
        elif len(elektronski_naslov) < 4:
            flash('Elektronski naslov mora biti daljši od 4 znakov!', category='error')
        elif len(ime) < 3:
            flash('Ime mora biti daljše od 2 znakov!', category='error')
        elif len(priimek) == 0:
            flash('Vnesti moraš priimek!', category='error')
        elif geslo1 != geslo2:
            flash('Gesli se ne ujemata!', category='error')
        else:
            nov_uporabnik = Uporabnik(
                elektronski_naslov=elektronski_naslov,
                ime=ime,
                priimek=priimek,
                geslo=generate_password_hash(geslo1, 'sha256')   
            )
            pb.session.add(nov_uporabnik)
            pb.session.commit()
            login_user(nov_uporabnik, remember=True)
            flash('Račun je bil ustvarjen.', category='success')
            return redirect(url_for('views.home')) # preusmerimo na domačo stran.
    
    return render_template("registracija.html", uporabnik=current_user)