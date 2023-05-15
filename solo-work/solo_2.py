
# class Trojkat:
#     def __init__ (self, a, b, c, h_a):
#         self.bok_a = a
#         self.b = b
#         self.c = c
#         self.h_a = h_a
#         # self.obwod = a + b + c
#
#     def obwod(self):
#         return self.bok_a + self.b + self.c
#
#     def pole(self):
#         return (self.bok_a * self.h_a) * 0.5
#
#
# trojkat_rownoboczny = Trojkat(10, 10, 10, 8)
#
# print(trojkat_rownoboczny.obwod())
#
# print(trojkat_rownoboczny.pole())
#
# class Rownoleglobok:
#     def __init__ (self, a, b, h_a):
#         self.bok_a = a
#         self.bok_b = b
#         self.wysokosc_h = h_a
# #
# #     def obwod(self):
# #         return 2 * self.bok_a + 2 * self.bok_b
# #
# #     def pole(self):
# #         return self.bok_a * self.wysokosc_h
# #
# # rownoleglobok = Rownoleglobok(10, 4, 5)
#
# # print(rownoleglobok.obwod())
# # print(rownoleglobok.pole())
#
# class Student:
#     def __init__ (self, imie, nazwisko, numer_indeksu):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.numer_indeksu = numer_indeksu
#         self.oceny = []
#
#     def __str__(self):
#         return f"{self.imie} {self.nazwisko} {self.numer_indeksu}"
#
#     def __int__(self):
#         return 5
#
#     def dodaj_ocene(self, ocena):
#         self.oceny.append(ocena)
#
#     def zwroc_srednia(self):
#         return sum(self.oceny) / len(self.oceny)
#
# student_ola = Student("Aleksandra", "Wojewoda", 123123)
# student_ola.dodaj_ocene(4.5)
# student_ola.dodaj_ocene(5)
#
#
# print(student_ola.zwroc_srednia())




class Zapotrzebowanie:
    def __init__ (self, imie, nazwisko, plec, wiek, wzrost, masa_ciala, poziom_akt_fiz, bialka, weglowodany, tluszcze):
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec
        self.wiek = wiek
        self.wzrost = wzrost
        self.masa_ciala = masa_ciala
        self.poziom_akt_fiz = poziom_akt_fiz
        self.procentowy_udzial_bialka = bialka
        self.procentowy_udzial_weglowodany = weglowodany
        self.procentowy_udzial_tluszcze = tluszcze

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.plec} {self.wiek} {self.wzrost} {self.masa_ciala} {self.poziom_akt_fiz}"

    def __int__(self):
        return 2150

    def zwroc_zapotrzeb_kalorie(self):
        if (self.poziom_akt_fiz=="sredni"):
            return 1.55 * (655 + (9.6 * self.masa_ciala) + (1.8 * self.wzrost) - (4.7*self.wiek))
        elif (self.poziom_akt_fiz == "niski"):
            return 1.2 * (655 + (9.6 * self.masa_ciala) + (1.8 * self.wzrost) - (4.7 * self.wiek))
        elif (self.poziom_akt_fiz == "wysoki"):
            return 1.9 * (655 + (9.6 * self.masa_ciala) + (1.8 * self.wzrost) - (4.7 * self.wiek))
        else:
            print("blednie zdefiniowany pompom aktywnosci ficzynej (dostepne: niski, wysoki, sredni")
            return 0

    def zwroc_zapotrzeb_bialko(self):
        return (self.zwroc_zapotrzeb_kalorie() * self.procentowy_udzial_bialka)/4
    def zwroc_zapotrzeb_weglowodany(self):
        return (self.zwroc_zapotrzeb_kalorie() * self.procentowy_udzial_weglowodany)/4
    def zwroc_zapotrzeb_tluszcze(self):
        return (self.zwroc_zapotrzeb_kalorie() * self.procentowy_udzial_tluszcze)/9

Zapotrzebowanie_Aleksandra = Zapotrzebowanie("Aleksandra", "Kowalska", "kobieta", 30, 165, 60, "sredni", 0.20, 0.50, 0.30)

print(Zapotrzebowanie_Aleksandra)
print(Zapotrzebowanie_Aleksandra.zwroc_zapotrzeb_kalorie())
print(Zapotrzebowanie_Aleksandra.zwroc_zapotrzeb_bialko())
print(Zapotrzebowanie_Aleksandra.zwroc_zapotrzeb_weglowodany())
print(Zapotrzebowanie_Aleksandra.zwroc_zapotrzeb_tluszcze())
