import threading
import time
import random

class Casino(threading.Thread):

    def __init__(self):
        self.numero = random.randint(0, 36)
        self.saldo = 50000

    def numeroGanador(self, usuario, apuesta):
        if apuesta == self.numero:
            usuario.setDinero(usuario.getDinero() + 360)
            self.saldo -= 360
        else:
            usuario.setDinero(usuario.getDinero() - 10)
            self.saldo += 10

    def parImpar(self, usuario, apuesta):
        if apuesta == "par" and self.numero % 2 == 0:
            usuario.setDinero(usuario.getDinero() + 20)
            self.saldo -= 20
        elif apuesta == "impar" and self.numero % 2 != 0:
            usuario.setDinero(usuario.getDinero() + 20)
            self.saldo -= 20
        else:
            usuario.setDinero(usuario.getDinero() - 10)
            self.saldo += 10

    def martingala(self, usuario, apuesta):
        apuesta = "fallida"
        n = 1
        while apuesta == "fallida" and usuario.getDinero() > 0:
            if apuesta == self.numero:
                usuario.setDinero(usuario.getDinero() + 360*n)
                self.saldo -= 360*n
            else:
                usuario.setDinero(usuario.getDinero() - 10*n)
                self.saldo += 10*n
                n += 1

    def getSaldo(self):
        return self.saldo
        

class Usuario(threading.Thread):
    
        def __init__(self, nombre):
            self.nombre = nombre
            self.dinero = 1000
    
        def getDinero(self):
            return self.dinero
    
        def setDinero(self, dinero):
            self.dinero = dinero


# crear 4 hilos de usuarios que jueguen al casino con numeros al azar

def main():

    casino = Casino()

    usuario1 = Usuario("Pepe")
    usuario2 = Usuario("Juan")
    usuario3 = Usuario("Luis")
    usuario4 = Usuario("Ana")

    hilo1 = threading.Thread(target=casino.numeroGanador(usuario1, 10))
    hilo2 = threading.Thread(target=casino.parImpar(usuario2, "par"))
    hilo3 = threading.Thread(target=casino.martingala(usuario3, 10))
    hilo4 = threading.Thread(target=casino.martingala(usuario4, 10))

    hilo1.start()
    hilo2.start()
    hilo3.start()
    hilo4.start()

    hilo1.join()
    hilo2.join()
    hilo3.join()
    hilo4.join()

    print("Saldo final: %d" % casino.getSaldo())



if __name__ == "__main__":
    main()
