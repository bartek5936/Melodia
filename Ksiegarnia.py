class Ksiazki:

    def __init__ (self, autor, tytul, cena):
        self.autor = autor
        self.tytul = tytul
        self.cena = cena
        self.ksiegozbior = {"Autor ksiazki": autor, "Tytul ksiazki": tytul, "cena ksiazki": cena}
        self.spis = []
        self.spis.append(self.ksiegozbior)


    def dodaj_ksiazke(self, autor, tytul, cena):
        ksiazka = {"Autor ksiazki": autor, "Tytul ksiazki": tytul, "cena ksiazki": cena}
        return self.spis.append(ksiazka)

    def pokaz(self):
        return print(self.spis)

    def zapisz(self):
        plik = open("Ksiegarnia1.txt", "w")
        plik.write(str(self.spis) + '\n')
        plik.close()

    def odczytaj(self):
        plik = open("Ksiegarnia1.txt", "r")
        for l in plik:
            print(l)



dorek = Ksiazki("tuwin", "dziadny", 20)
dorek.dodaj_ksiazke("tuwin", "dziady", 21)
print("Zwykly odczyt")
dorek.pokaz()
dorek.zapisz()
print("Odczyt z pliku")
dorek.odczytaj()