from classes import *


# crear 4 hilos de usuarios que jueguen al casino con numeros al aza
if __name__ == "__main__":
    # crear objeto casino
    casino = Casino()
    # crear 4 objetos usuario y arrancar los hilos
    usuarios = []
    for i in range(4):
        usuario = Usuario("usuario"+str(i+1), random.randint(0, 36), random.choice(["numero", "par/impar", "martingala"]), casino)
        usuarios.append(usuario)
        usuario.start()
    # arrancar hilo del casino
    casino.start()
    # esperar a que todos los hilos terminen
    for usuario in usuarios:
        usuario.join()
    casino.join()
