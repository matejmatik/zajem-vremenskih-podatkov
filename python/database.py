#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

try:
    povezava = sqlite3.connect('./sql/vremenski_podatki.db')
    print("Podatkovna baza uspesno odprta!")
except Exception as e:
    print(f"Napaka pri povezavi: {e}")

povezava.execute('''
    CREATE TABLE IF NOT EXISTS ime_tabele (
        id INT PRIMARY KEY NOT NULL,
        test VARCHAR(30)
    );
    ''')

povezava.close()