#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pridobi_postaje_xml import pridobi_postaje_xml
from pridobi_vreme_xml import pridobi_vreme_xml
from zajem_postaj_pb import zajem_postaj

PODATKOVNA_BAZA = "vremenski_podatki.db"

def main():
    zajem_postaj()
    
    while True:
        pass

    
    # for ime, url in pridobi_vremenske_postaje().items():
    #     print(zajem_vremenskih_podatkov(url))

if __name__ == '__main__':
    main()