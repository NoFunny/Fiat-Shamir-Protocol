import BasicFunctions


class FiatShamirProtocol:

    def __init__(self, tc, userA, userB):
        self.tc = tc
        self.usrA = userA
        self.ursB = userB

    def start(self, rounds):
        for i in range(0, rounds):
            flag = self.round_()
            if flag:
                continue
            elif not flag:
                print('Error: Identity not confirmed')
                return False
        return True

    def round_(self):
        x = self.usrA.calcX(self.tc.n)
        e = self.ursB.coinToss()
        y = self.usrA.calcY(e, self.tc.n)
        if self.compare(y, x, e, self.usrA.open, self.tc.n):
            print("Left = ", BasicFunctions.fast_modulo_exponentiation(y, 2, self.tc.n), "Right =",
                  (x % self.tc.n) * BasicFunctions.fast_modulo_exponentiation(self.usrA.open, e, self.tc.n) % self.tc.n)
            print("e = ", e)
            return True
        elif not self.compare(y, x, e, self.usrA.open, self.tc.n):
            print("Left = ", BasicFunctions.fast_modulo_exponentiation(y, 2, self.tc.n), "Right =",
                  (x % self.tc.n) * BasicFunctions.fast_modulo_exponentiation(self.usrA.open, e, self.tc.n) % self.tc.n)
            print("e = ", e)
            return False
        pass

    def compare(self, y, x, e, v, n):
        if BasicFunctions.fast_modulo_exponentiation(y, 2, n) == x%n * BasicFunctions.fast_modulo_exponentiation(v, e, n) % n:
            return True
        else:
            return False
        pass
