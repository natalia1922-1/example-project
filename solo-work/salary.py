import csv

class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto, procent_skladki_wypadkowej=0.03):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = wynagrodzenie_brutto
        self.procent_skladki_wypadkowej = procent_skladki_wypadkowej

    def __str__(self):
        pass

    def oblicz_netto(self):
        if (self.składka_zdrowotna == ""):
            return

    def oblicz_koszty_pracodawcy(self):
        skladka_rentowa = self.wynagrodzenie_brutto * 0.015
        skladka_emerytalna = self.wynagrodzenie_brutto * 0.0976
        fundusz_pracy = self.wynagrodzenie_brutto * 0.0245
        skladka_wypadkowa = self.wynagrodzenie_brutto * self.procent_skladki_wypadkowej
        FGŚP = self.wynagrodzenie_brutto * 0.001
        koszty_pracodawcy = skladka_rentowa + skladka_emerytalna + fundusz_pracy + FGŚP + skladka_wypadkowa
        return koszty_pracodawcy



pracownicy = [] # z csv
with open('salary.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            pracownik = Pracownik(row[0], row[1], row[2])
            pracownicy.append(pracownik)

# for pracownik in_pracownicy:
#     print("Pracownik Kowalski: ")
#     print("- prensja brutto: ")
#     print("- pensja netto: ")
#     print("- koszty pracodawcy: ")
#     print("- koszt całkowity: ")

# print("Suma kosztów wynosi: xxx")

# zdrowotna, emerytalna, rentowna - koszty pracownika
# koszty pracodawcy -

