from bs4 import BeautifulSoup
import pandas as pd
# import numpy as np
import requests


def zajem_vremenskih_podatkov (url):
    """Funkcija, ki iz podanega naslova pridobi vremenske podatke.

    Args:
        url (string): url naslov spletne strani z vremenskimi podatki

    Returns:
        panda_okvir: vrne panda okvir vremenskih podatkov
    """

    # Pridobivanje podatkov s spletne strani
    xml_podatki = requests.get(url).content
    soup = BeautifulSoup(xml_podatki, "xml")
    
    meritev = soup.find("metData")
    if meritev is not None: # V kolikor je meritev, pridobimo podatke
        # Pridobivanje imena kraja
        kraj = meritev.find("domain_longTitle").get_text()

        # Pridobivanje datuma, casa 
        datum_cas_meritve = meritev.find('tsValid_issued').get_text().split(" ")
        datum = datum_cas_meritve[0]
        cas = datum_cas_meritve[1]

        # Pridobivanje vremenskih podatkov
        temperatura = meritev.find('t')
        if temperatura is not None:
            temperatura = temperatura.get_text()
            if temperatura != "":
                temperatura = float(temperatura)

        relativna_vlaznost = meritev.find('rh')
        if relativna_vlaznost is not None:
            relativna_vlaznost = relativna_vlaznost.get_text()
            if relativna_vlaznost != "":
                relativna_vlaznost = float(relativna_vlaznost)

        # smer_vetra = meritev.find('dd_shortText').get_text()
        # hitrost_vetra = float(meritev.find('ff_val_kmh').get_text())
        # padavine = float(meritev.find('rr_val').get_text())
        # vsota_padavin = float(meritev.find('tp_12h_acc').get_text())

        # Shranjevanje v panda "okvir"
        zapis = pd.DataFrame(
            {
            "kraj": [kraj],
            "datum": [datum],
            "cas": [cas],
            "temperatura": [temperatura],
            "relativna_vlaznost": [relativna_vlaznost]
            }
            )
        
        return zapis

    return 
