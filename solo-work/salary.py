import csv


class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = float(wynagrodzenie_brutto)
        self.skladka_rentowa_prcw = self.wynagrodzenie_brutto * 0.015
        self.skladka_emerytalna_prcw = self.wynagrodzenie_brutto * 0.0976
        self.skladka_chorobowa = self.wynagrodzenie_brutto * 0.0245
        self.skladka_zdrowotna = 0.09
        self.koszty_uzysk_przych = 250
        self.kwota_wolna = 300
        self.procent_ppk_pracodawcy = 0.0
        self.procent_ppk_pracownika = 0.0

    def __str__(self):
        pass

    def set_koszty_uzysk_przych(self, koszty):
        if (koszty == 0 or koszty == 250 or koszty == 300):
            self.koszty_uzysk_przych = koszty
        else:
            print("Koszty uzyskanych przychodow moga .... 0, 250 lub 300, ustawiono na 250")
            self.koszty_uzysk_przych = 250

    def set_kwota_wolna(self, kwota):
        if (kwota == 0 or kwota == 100 or kwota == 150 or kwota == 300):
            self.kwota_wolna = kwota
        else:
            print("kwota wolna może wynosić 0, 100, 150, lub 300, ustawiono na wartość 300")
            self.kwota_wolna = 300

    def set_ppk_pracownika(self, procent):
        if procent < 0.005:
            self.procent_ppk_pracownika = 0.0
        elif procent > 0.04:
            self.procent_ppk_pracownika = 0.0
        else:
            self.procent_ppk_pracownika = procent

    def set_ppk_pracodawcy(self, procent):
        if procent < 0.005:
            self.procent_ppk_pracodawcy = 0.0
        elif procent > 0.04:
            self.procent_ppk_pracodawcy = 0.0
        else:
            self.procent_ppk_pracodawcy = procent

    def skladka_ppk_pracownika(self):
        return self.procent_ppk_pracownika * self.wynagrodzenie_brutto

    def skladka_ppk_pracowdacy(self):
        return self.procent_ppk_pracodawcy * self.wynagrodzenie_brutto

    def oblicz_koszty_pracownika(self):
        koszty_pracownik = self.skladka_rentowa_prcw + self.skladka_emerytalna_prcw \
                           + self.skladka_zdrowotna + self.skladka_chorobowa
        return koszty_pracownik

    def oblicz_koszty_pracodawcy(self):
        skladka_rentowa_prcd = self.wynagrodzenie_brutto * 0.065
        skladka_emerytalna_prcd = self.wynagrodzenie_brutto * 0.0976
        fundusz_pracy = self.wynagrodzenie_brutto * 0.0245
        skladka_wypadkowa = self.wynagrodzenie_brutto * 0.0167
        fgsp = self.wynagrodzenie_brutto * 0.001
        koszty_pracodawcy = self.skladka_ppk_pracowdacy() + skladka_rentowa_prcd + skladka_emerytalna_prcd + \
                            fundusz_pracy + fgsp + skladka_wypadkowa
        return koszty_pracodawcy

    def oblicz_netto(self):

        ubezpieczenie_zdrowotne = (self.wynagrodzenie_brutto - (self.skladka_rentowa_prcw +
                                                                self.skladka_emerytalna_prcw +
                                                                self.skladka_chorobowa)) * self.skladka_zdrowotna

        podstawa_opod = (self.wynagrodzenie_brutto - (self.skladka_rentowa_prcw + self.skladka_emerytalna_prcw +
                                                      self.skladka_chorobowa)) - self.koszty_uzysk_przych \
                        + self.skladka_ppk_pracowdacy()

        zaliczka_pod_doch = (podstawa_opod * 0.12) - self.kwota_wolna

        koszty_pracownik = self.oblicz_koszty_pracownika()
        return self.wynagrodzenie_brutto - koszty_pracownik - ubezpieczenie_zdrowotne - zaliczka_pod_doch - self.skladka_ppk_pracownika()

    def calkowity_koszt_pracodawcy(self):
        return self.oblicz_netto() + self.oblicz_koszty_pracodawcy() + self.oblicz_koszty_pracodawcy()


pracownicy = []  # z csv
with open('salary.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            pracownik = Pracownik(row[0], row[1], row[2])
            pracownicy.append(pracownik)

pracownicy[0].set_koszty_uzysk_przych(250)
pracownicy[1].set_koszty_uzysk_przych(250)
pracownicy[2].set_koszty_uzysk_przych(250)
pracownicy[3].set_koszty_uzysk_przych(300)
pracownicy[4].set_koszty_uzysk_przych(300)
pracownicy[5].set_koszty_uzysk_przych(0)

pracownicy[0].set_kwota_wolna(0)
pracownicy[1].set_kwota_wolna(0)
pracownicy[2].set_kwota_wolna(300)
pracownicy[3].set_kwota_wolna(300)
pracownicy[4].set_kwota_wolna(150)
pracownicy[5].set_kwota_wolna(300)

pracownicy[0].set_ppk_pracodawcy(0.0)
pracownicy[1].set_ppk_pracodawcy(0.02)
pracownicy[2].set_ppk_pracodawcy(0.0)
pracownicy[3].set_ppk_pracodawcy(0.0)
pracownicy[4].set_ppk_pracodawcy(0.0)
pracownicy[5].set_ppk_pracodawcy(0.02)

pracownicy[0].set_ppk_pracownika(0.0)
pracownicy[1].set_ppk_pracownika(0.02)
pracownicy[2].set_ppk_pracownika(0.0)
pracownicy[3].set_ppk_pracownika(0.0)
pracownicy[4].set_ppk_pracownika(0.0)
pracownicy[5].set_ppk_pracownika(0.02)

for pracownik in pracownicy:
    print("Pracownik :", pracownik.imie, pracownik.nazwisko)
    print("- prensja brutto: ", pracownik.wynagrodzenie_brutto)
    print("- pensja netto: ", pracownik.oblicz_netto())
    print("- koszty pracodawcy: ", pracownik.oblicz_koszty_pracodawcy())
    print("- koszt całkowity: ", pracownik.calkowity_koszt_pracodawcy())

# print("Suma kosztów wynosi: xxx")

# zdrowotna, emerytalna, rentowna - koszty pracownika
# koszty pracodawcy -
