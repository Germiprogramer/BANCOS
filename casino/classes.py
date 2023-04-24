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

        def apostar(self, numero, tipodeapuesta, casino):
            if tipodeapuesta == "numero":
                casino.numeroGanador(Usuario, numero)

            elif tipodeapuesta == "par/impar":
                casino.parImpar(Usuario, numero)

            elif tipodeapuesta == "martingala":
                casino.martingala(Usuario, numero)
            
            time.sleep(3)
    
        def getDinero(self):
            return self.dinero
    
        def setDinero(self, dinero):
            self.dinero = dinero