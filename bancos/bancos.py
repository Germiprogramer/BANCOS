from multiprocessing import Pool
import unittest
from classes import Banco

def repeticion(funcion, n):
    if n == 0:
        return
    else:
        funcion()
        repeticion(funcion, n-1)

def main():

    banco1 = Banco(1000)

    #emplear pool.map para ingresar

    with Pool(processes=40) as pool:
        pool.map_async(banco1.ingresar(100),range(40))

    
    
    po3 = Pool()
    po3.map_async(banco1.ingresar(20),range(60))
    

    #emplear pool.map para retirar

    po = Pool()
    po.map_async(banco1.retirar(100),range(40))
    

    po2 = Pool()
    po2.map_async(banco1.retirar(50),range(20))
   

    po3 = Pool()
    po3.map_async(banco1.retirar(20),range(60))




    print("Saldo final: %d" % banco1.getSaldo())

if __name__ == "__main__":
    main()


# hazme los unit test de los métodos de la clase Banco

class TestBanco(unittest.TestCase):
    def test_ingresar(self):
        banco1 = Banco(1000)
        banco1.ingresar(100)
        self.assertEqual(banco1.getSaldo(), 1100)

    def test_retirar(self):
        banco1 = Banco(1000)
        banco1.retirar(100)
        self.assertEqual(banco1.getSaldo(), 900)

    def test_getSaldo(self):
        banco1 = Banco(1000)
        self.assertEqual(banco1.getSaldo(), 1000)

if __name__ == '__main__':
    unittest.main()



