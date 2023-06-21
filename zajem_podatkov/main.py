#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from zajem_postaj_pb import zajem_postaj
from zajem_vreme_pb import zajem_vreme_pb
from time import sleep

PODATKOVNA_BAZA = "vremenski_podatki.db"

def main():
    zajem_postaj()
    
    while True:
        zajem_vreme_pb()
        sleep(60*60) # 1 ura zakasnitve        

    
    # for ime, url in pridobi_vremenske_postaje().items():
    #     print(zajem_vremenskih_podatkov(url))

if __name__ == '__main__':
    main()