import BasicFunctions
import random


class User:

    def __init__(self):
        self.secret = None
        self.open = None
        self.x = None
        self.e = None
        self.y = None
        self.r = None

    def initUserA(self, n):
        self.secret = BasicFunctions.gen_g(n)
        self.open = BasicFunctions.fast_modulo_exponentiation(self.secret, 2, n)
        return self

    def initUserB(self):
        self.e = random.randint(0, 1)
        return self

    def initEva(self, n):
        return self

    def calcX(self, n):
        self.r = random.randint(1, n - 1)
        self.x = BasicFunctions.fast_modulo_exponentiation(self.r, 2, n)
        return self.x

    def coinToss(self):
        self.e = random.randint(0, 1)
        return self.e

    def calcY(self, e, n):
        if self.secret is None or self.open is None:
            self.secret = 100500
            self.open = 100500
        self.y = (self.r % n) * BasicFunctions.fast_modulo_exponentiation(self.secret, e, n) % n
        return self.y