# postaja.py>

from unittest import expectedFailure
from urllib import request
from bs4 import BeautifulSoup
from bs4.element import Comment
import pandas as pd
import numpy as np
import requests


def pridobi_vremenske_postaje ():

    url = "https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observation_si/index.html"

    xml_podatki = requests.get(url).content

    soup = BeautifulSoup(xml_podatki, "xml")
    seznam_meritev = soup.find_all("table", "meteoSI-table")

    tabela_vrstice_skupaj = seznam_meritev[2].find_all("tr")

    vremenske_postaje = {}

    for vrstica in tabela_vrstice_skupaj:
        try:
            podatki = vrstica.find_all("td")
            ime_kraja = podatki[0].get_text()
            xml_url = "https://meteo.arso.gov.si/" + podatki[1].find_all("a")[0]["href"]
            vremenske_postaje[ime_kraja] = xml_url
            #print(f"{ime_kraja}: {xml_url}")
        except:
            pass

    return vremenske_postaje



