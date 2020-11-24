import BasicFunctions


class TrustedCenter:

    def __init__(self):
        self.p = BasicFunctions.gen_p()
        self.q = BasicFunctions.gen_p()
        self.n = self.p*self.q
