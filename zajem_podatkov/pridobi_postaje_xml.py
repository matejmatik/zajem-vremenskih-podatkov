# postaja.py>
from bs4 import BeautifulSoup
import requests


def pridobi_postaje_xml():
    """Funkcija, ki iz arso pridobi vse vremenske postaje.

    Returns:
        slovar: slovar postaj, kjer kljuc ime postaje, vrednost pa url xml-ja
    """

    url = "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observation_si/index.html"

    xml_podatki = requests.get(url).content

    soup = BeautifulSoup(xml_podatki, "xml")
    seznam_meritev = soup.find_all("table", "meteoSI-table")

    tabela_vrstice_skupaj = seznam_meritev[2].find_all("tr") # pridobimo posamezno vrstico
    vremenske_postaje = {}

    for vrstica in tabela_vrstice_skupaj:
        podatki = vrstica.find_all("td")
        if podatki != []: 
            try:
                ime_kraja = podatki[0].get_text()
                xml_url = "https://meteo.arso.gov.si/" + podatki[1].find_all("a")[0]["href"]
                vremenske_postaje[ime_kraja] = xml_url
                #print(f"{ime_kraja}: {xml_url}")
            except Exception as e:
                print(e)

    return vremenske_postaje



