# zadanie 1.1

# hello = "Hello"
# student = "Ola"
# print("{} {}".format(hello, student))

# zadanie 1.2
#
# student = input("Wpisz swoje imie ")
# print("Hello", student)

# zadanie 1.3

# studenci = ["Ania", "Kuba", "Piotr", "Jan"]
#
# liczba_studentow = len(studenci)
# print("Liczba studentow wynosi:", liczba_studentow)

# # zadanie 1.4
#
# studenci = ["Ania", "Kasia", "Piotr", "Tomek"]
#
# for x in studenci:
#     print("Hello", x)

# # zadanie 1.5
#
# liczba = 3
# potega = 4
#
# wynik = liczba ** potega
#
# print("Wyniki wynosi ", wynik)

# # zadanie 1.6
#
# ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
# liczba_nawiasow_otwierajacych = ciag_znakow.count("(")
#
# print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

# posortuj alfabetycznie (od imienia) studentow
# studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
#
# studenci.sort()
#
# print("Alfabetyczna lista studentow wynosi: ")
# for student in studenci:
#     print(student)

# # zadanie 1.8
#
# # posortuj alfabetycznie (od nazwiska) studentow
# studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
#
# studenci.sort(key=lambda x: x.split()[1])
#
# print("Alfabetyczna lista studentow wynosi: ")
# for student in studenci:
#     print(student)

# zadanie 1.9

## policz wszystkich studentow z tablicy, ktorych nazwisko zaczyna sie na N
# studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
#
# liczba_n = 0
# for student in studenci:
#     nazwisko = student.split()[1]
#     if nazwisko[0] == 'N':
#         liczba_n = liczba_n + 1
#
# print("Liczba studentow na N wynosi:", liczba_n)

# zadanie 1.10

# zmienne poniezej preprezentuja ulozenie punktow na wykresie,
# do zadania dolaczono takze rysunek pomocniczy
wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

wykres_1_funkcja_liniowa = True
wykres_2_funkcja_liniowa = True
wykres_3_funkcja_liniowa = True

y1 = wykres_1[0][1]
y2 = wykres_1[1][1]
x1 = wykres_1[0][0]
x2 = wykres_1[1][0]

a = (y2 - y1)/(x2 - x1)
b = y1 - a * x1

for punkt in wykres_1:
    if not (punkt[1] == a * punkt[0] + b):
        wykres_1_funkcja_liniowa = False

y1 = wykres_2[0][1]
y2 = wykres_2[1][1]
x1 = wykres_2[0][0]
x2 = wykres_2[1][0]

a = (y2 - y1)/(x2 - x1)
b = y1 - a * x1

for punkt in wykres_3:
    if not (punkt[1] == a * punkt[0] + b):
        wykres_3_funkcja_liniowa = False


y1 = wykres_3[0][1]
y2 = wykres_3[1][1]
x1 = wykres_3[0][0]
x2 = wykres_3[1][0]

a = (y2 - y1)/(x2 - x1)
b = y1 - a * x1

for punkt in wykres_3:
    if not (punkt[1] == a * punkt[0] + b):
        wykres_3_funkcja_liniowa = False


# zbadaj kazdy wykres, czy dla wyznaczonych punktow istnieje funkcja
# liniowa laczaca punkty
# jesli sie nie da, to zwroc False
# jesli sie da, zwroc True



if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")

# oczekiwany rezultat:
# Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.
# Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.
# Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.
