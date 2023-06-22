from pridobi_vreme_xml import pridobi_vreme_xml
from os import path, getcwd
import sqlite3
from datetime import datetime

def zajem_vreme_pb(PODATKOVNA_BAZA):
    """Funkcija, ki shrani prebrane vremenske podatke v PB.
    """
    
    pot = path.join(getcwd(), 'instance', PODATKOVNA_BAZA)
    try:
        povezava = sqlite3.connect(pot)
        kazalec = povezava.cursor()
        #print("Podatkovna baza uspesno odprta!")
    except Exception as e:
        print(f"Napaka pri povezavi: {e}")
        
    sql = "SELECT * FROM vremenska_postaja"
    kazalec.execute(sql, [])
    
    podatki = kazalec.fetchall()
    
    for zapis in podatki:
        _id = zapis[0]
        ime = zapis[1]
        url = zapis[2]
        
        vreme_zapis = pridobi_vreme_xml(url)
        if vreme_zapis["datum"] is not None:
            datum_cas_sistem = datetime.now()
            
            sql = """INSERT INTO vremenski_podatki 
            VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""        
            
            kazalec.execute(sql, [
                datetime.strptime(vreme_zapis["datum"], 
                                  "%d.%m.%Y").strftime('%Y-%m-%d'), # DATUM
                datetime.strptime(vreme_zapis["cas"], 
                                  "%H:%M").strftime('%H:%M:%S'), # CAS
                datum_cas_sistem, # DATETIME
                vreme_zapis["temperatura"],
                vreme_zapis["relativna_vlaznost"],
                vreme_zapis["smer_vetra"],
                vreme_zapis["hitrost_vetra"],
                vreme_zapis["padavine"],
                vreme_zapis["vsota_padavin"],
                _id
                ])
            
            print((f'{ime}, {vreme_zapis["datum"]} {vreme_zapis["cas"]}: '
                   f'{vreme_zapis["temperatura"]}°C'))
            
            povezava.commit()
    povezava.close()



