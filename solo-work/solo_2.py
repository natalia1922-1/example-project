
class Trojkat:
    def __init__ (self, a, b, c, h_a):
        self.bok_a = a
        self.b = b
        self.c = c
        self.h_a = h_a
        # self.obwod = a + b + c

    def obwod(self):
        return self.bok_a + self.b + self.c

    def pole(self):
        return (self.bok_a * self.h_a) * 0.5


trojkat_rownoboczny = Trojkat(10, 10, 10, 8)

print(trojkat_rownoboczny.obwod())

print(trojkat_rownoboczny.pole())

class Rownoleglobok:
    def __init__ (self, a, b, h_a):
        self.bok_a = a
        self.bok_b = b
        self.wysokosc_h = h_a

    def obwod(self):
        return 2 * self.bok_a + 2 * self.bok_b

    def pole(self):
        return self.bok_a * self.wysokosc_h

rownoleglobok = Rownoleglobok(10, 4, 5)

print(rownoleglobok.obwod())
print(rownoleglobok.pole())