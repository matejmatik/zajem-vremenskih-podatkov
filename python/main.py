#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from postaja import pridobi_vremenske_postaje
from zajem_vremenskih_podatkov import zajem_vremenskih_podatkov

def main():
    for ime, url in pridobi_vremenske_postaje().items():
        print(zajem_vremenskih_podatkov(url))

if __name__ == '__main__':
    main()