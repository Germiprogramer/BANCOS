class Banco():
    def __init__(self, saldo):
        self.saldo = saldo

    def ingresar(self, dinero):
        self.saldo += dinero
        print("Ingreso de %d. Total: %d" % (dinero, self.saldo))

    def retirar(self, dinero):
        self.saldo -= dinero
        print("Retirada de %d. Total: %d" % (dinero, self.saldo))

    def getSaldo(self):
        return self.saldo