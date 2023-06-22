from bs4 import BeautifulSoup
import requests

def uredi_podatek (meritev, znacka, tip="float"):
    """Funkcija, ki uredi podatek iz xml-ja

    Args:
        meritev (soup): vremenska meritev
        znacka (str): xml znacka
        tip (str, optional): tip podatka/vrednosti

    Returns:
        _type_: vrne podatek v ustreznem tipu
    """
    
    podatek = meritev.find(znacka)
    if podatek is not None:
        podatek = podatek.get_text()
        if podatek != "":
            if tip == "float":
                return float(podatek)
            elif tip == "int":
                return int(podatek)
            elif tip == "str":
                return podatek
    return None   


def pridobi_vreme_xml (url):
    """Funkcija, ki iz podanega url naslova pridobi vremenske podatke.

    Args:
        url (str): url naslov spletne strani z vremenskimi podatki

    Returns:
        slovar: slovar vremenskih podatkov
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
        temperatura = uredi_podatek(meritev, "t", "float")
        relativna_vlaznost = uredi_podatek(meritev, 'rh', "float")
        smer_vetra = uredi_podatek(meritev,'dd_shortText', "str")
        hitrost_vetra = uredi_podatek(meritev,'ff_val_kmh', "float")
        padavine = uredi_podatek(meritev,'rr_val', "float")
        vsota_padavin = uredi_podatek(meritev,'tp_12h_acc', "float")
        
        # Shranjevanje v panda "okvir"
        return {
            "kraj": kraj,
            "datum": datum,
            "cas": cas,
            "temperatura": temperatura,
            "relativna_vlaznost": relativna_vlaznost,
            "smer_vetra": smer_vetra,
            "hitrost_vetra": hitrost_vetra,
            "padavine": padavine,
            "vsota_padavin": vsota_padavin
            }

    return {
            "kraj": None,
            "datum": None,
            "cas": None,
            "temperatura": None,
            "relativna_vlaznost": None,
            "smer_vetra": None,
            "hitrost_vetra": None,
            "padavine": None,
            "vsota_padavin": None
            }

