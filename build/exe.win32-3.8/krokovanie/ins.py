import random

class Create_arrows():
    def __init__(self):
        #smer = [1, 1 , 1]
        self.smer = []
        #hodnota na aktualnej pozici
        self.hodnota = 0
        #aktualna sipka
        self.sipka = 0
        #maximalna hodnota
        self.max_sipok = random.randint(9,10)
        #kolko je kamenov
        self.pocet_kamenov = 6
        #smer, hodnota
        self.main_chooser()

    def count_of_numbers(self):
        pocty = []
        for _ in range(10000):
            cislo = random.randint(0,100)
            pocty.append(cislo)

        return [pocty.count(0), pocty.count(1), pocty.count(2)]

    def main_chooser(self):
        while self.sipka <= self.max_sipok:
            pocet_cisel = self.count_of_numbers()
            #ohranicenie hodnot sipok z oboch stran
            if self.hodnota - 1 < 1:
                self.smer.append(1)
                self.hodnota += 1
            elif self.hodnota + 1 > self.pocet_kamenov:
                self.smer.append(-1)
                self.hodnota -= 1
            elif pocet_cisel[0] > pocet_cisel[1]:
                self.smer.append(-1)
                self.hodnota -= 1
            elif pocet_cisel[1] >= pocet_cisel[0] or pocet_cisel[2] >= pocet_cisel[0] or pocet_cisel[0] > pocet_cisel[2]:
                self.smer.append(1)
                self.hodnota += 1

            self.sipka += 1
