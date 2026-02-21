class publicKey():
    def __init__(self, n, e):
        self.n = n
        self.e = e

class privateKey():
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.phin = (self.p - 1)*(self.q - 1)