from spletna_aplikacija import ustvari_aplikacijo
from zajem_podatkov.main import zajem

aplikacija = ustvari_aplikacijo()

if __name__ == '__main__':
    aplikacija.run(debug=True)