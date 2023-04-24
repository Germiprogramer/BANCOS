from classes import *


# crear 4 hilos de usuarios que jueguen al casino con numeros al aza
def main():

    casino = Casino()

    usuario1 = Usuario("Pepe")
    usuario2 = Usuario("Juan")
    usuario3 = Usuario("Luis")
    usuario4 = Usuario("Ana")

    hilo1 = threading.Thread(target=usuario1.apostar, args=(10, "numero", casino))
    hilo2 = threading.Thread(target=usuario2.apostar, args=(10, "numero", casino))
    hilo3 = threading.Thread(target=usuario3.apostar, args=(10, "par/impar", casino))
    hilo4 = threading.Thread(target=usuario4.apostar, args=(10, "martingala", casino))
    
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
