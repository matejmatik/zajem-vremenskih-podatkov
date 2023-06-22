#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from zajem_postaj_pb import zajem_postaj
from zajem_vreme_pb import zajem_vreme_pb
from time import sleep

PODATKOVNA_BAZA = "vremenski_podatki_ai.db"

def main():
    print("\n------------------------")
    print("Pridobivanje url podatkov vremenskih postaj")
    print("------------------------\n")
    
    zajem_postaj(PODATKOVNA_BAZA)
    
    print("\n------------------------")
    print("Zajem vremenskih podatkov")
    print("------------------------\n")
    
    while True:
        zajem_vreme_pb(PODATKOVNA_BAZA)
        print("\n------------------------")
        print("Naslednja meritev, čez eno uro ...")
        print("------------------------\n")
        sleep(60*60) # 1 ura zakasnitve        

if __name__ == '__main__':
    main()