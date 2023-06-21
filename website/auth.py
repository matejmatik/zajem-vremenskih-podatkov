from flask import Blueprint, flash, render_template, request


auth = Blueprint('auth', __name__)


@auth.route('/prijava', methods=['GET', 'POST'])
def login():
    podatki = request.form
    return render_template("prijava.html")


@auth.route('/odjava')
def logout():
    return "<p>Odjava</p>"


@auth.route('/registracija', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        elektronski_naslov = request.form.get('elektronski_naslov')
        ime = request.form.get('ime')
        priimek = request.form.get('priimek')
        geslo1 = request.form.get('geslo1')
        geslo2 = request.form.get('geslo2')

        if len(elektronski_naslov) < 4:
            flash('Elektronski naslov mora biti daljši od 4 znakov.', category='error')
        elif len(ime) < 3:
            flash('Ime mora biti daljše od 2 znakov.', category='error')
        elif geslo1 != geslo2:
            flash('Gesli se ne ujemata!', category='error')
        else:
            flash('Račun je bil ustvarjen!', category='success')
            # Dodamo v podatkovno bazo
    
    return render_template("registracija.html")