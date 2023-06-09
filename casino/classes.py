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
            print("{}".format(usuario.nombre)  + " ha ganado " + "{}".format(360) + "€")
        else:
            usuario.setDinero(usuario.getDinero() - 10)
            self.saldo += 10
            print("{}".format(usuario.nombre)  + " ha perdido " + "{}".format(10) + "€")

    def parImpar(self, usuario, apuesta):
        if apuesta == "par" and self.numero % 2 == 0:
            usuario.setDinero(usuario.getDinero() + 20)
            self.saldo -= 20
            print("{}".format(usuario.nombre)  + " ha ganado " + "{}".format(20) + "€")
        elif apuesta == "impar" and self.numero % 2 != 0:
            usuario.setDinero(usuario.getDinero() + 20)
            self.saldo -= 20
            print("{}".format(usuario.nombre)  + " ha ganado " + "{}".format(20) + "€")
        else:
            usuario.setDinero(usuario.getDinero() - 10)
            self.saldo += 10
            print("{}".format(usuario.nombre)  + " ha perdido " + "{}".format(10) + "€")

    def martingala(self, usuario, apuesta):
        apuesta = "fallida"
        n = 1
        while apuesta == "fallida" and usuario.getDinero() > 0:
            if apuesta == self.numero:
                usuario.setDinero(usuario.getDinero() + 360*n)
                self.saldo -= 360*n
                print("{}".format(usuario.nombre)  + " ha ganado " + "{}".format(360*n) + "€")
            else:
                usuario.setDinero(usuario.getDinero() - 10*n)
                self.saldo += 10*n
                print("{}".format(usuario.nombre)  + " ha perdido " + "{}".format(10*n) + "€")
                n += 1

    def getSaldo(self):
        return self.saldo
    
    def run(self):
        while self.saldo>0:
            time.sleep(3)
            self.numero = random.randint(0, 36)
            print("El numero ganador es: " + "{}".format(self.numero))

        

class Usuario(threading.Thread):
    
        def __init__(self, nombre, numero, tipodeapuesta, casino):
            self.nombre = nombre
            self.dinero = 1000
            self.numero = numero
            self.tipodeapuesta = tipodeapuesta
            self.casino = casino

        def run(self):
            while self.dinero > 0:
                if self.tipodeapuesta == "numero":
                    self.casino.numeroGanador(self, self.numero)

                elif self.tipodeapuesta == "par/impar":
                    self.casino.parImpar(self, self.numero)

                elif self.tipodeapuesta == "martingala":
                    self.casino.martingala(self, self.numero)
                
                time.sleep(3)
    
        def getDinero(self):
            return self.dinero
    
        def setDinero(self, dinero):
            self.dinero = dinero