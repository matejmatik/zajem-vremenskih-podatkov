from pridobi_postaje_xml import pridobi_postaje_xml
from os import path, getcwd
import sqlite3

def zajem_postaj(PODATKOVNA_BAZA):
    """Funkcija, ki shrani postaje in url-je v PB.
    """

    pot = path.join(getcwd(), 'instance', PODATKOVNA_BAZA)
    try:
        povezava = sqlite3.connect(pot)
        kazalec = povezava.cursor()
        #print("Podatkovna baza uspesno odprta!")
    except Exception as e:
        print(f"Napaka pri povezavi: {e}")
    
    for ime, url in pridobi_postaje_xml().items():
        sql = "SELECT * FROM vremenska_postaja WHERE ime = ?"
        kazalec.execute(sql, [ime])
        if not kazalec.fetchall():
            sql = "INSERT INTO vremenska_postaja VALUES(NULL, ?, ?)"
            kazalec.execute(sql, [ime, url])
            print(f'{ime}: {url}')
            povezava.commit()

    povezava.close()
    print("Vremenske postaje vstavljene ali posodobljene v PB.")



