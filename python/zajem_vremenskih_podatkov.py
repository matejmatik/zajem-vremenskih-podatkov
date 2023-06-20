from urllib import request
from bs4 import BeautifulSoup
from bs4.element import Comment
import pandas as pd
import numpy as np
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

    # Pridobivanje imena kraja
    kraj = meritev.find("domain_longTitle").get_text()

    # Pridobivanje datuma, casa 
    datum_cas_meritve = meritev.find('tsValid_issued').get_text().split(" ")
    datum = datum_cas_meritve[0]
    cas = datum_cas_meritve[1]

    # Pridobivanje temperature, vlaznosti
    try: 
        temperatura = float(meritev.find('t').get_text())
    except:
        temperatura = None
    try: 
        relativna_vlaznost = float(meritev.find('rh').get_text())
    except:
        relativna_vlaznost = None

    # Pridobivanje preostalih podatkov
    # - Veter
    try:
        smer_vetra = meritev.find('dd_shortText').get_text()
        hitrost_vetra = float(meritev.find('ff_val_kmh').get_text())
    except:
        smer_vetra, hitrost_vetra = None, None

    # - Padavine
    try:
        padavine = float(meritev.find('rr_val').get_text())
        vsota_padavin = float(meritev.find('tp_12h_acc').get_text())
    except:
        padavine, vsota_padavin = None, None

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

