import unittest
from guia7 import suma_total

class test_suma(unittest.TestCase):
    #se pueden definir los casos por separado
    def test_suma_0(self):
        mi_secuencia: list = [0,0,0]
        self.assertEqual(suma_total(mi_secuencia), 0)

    
if __name__ == '__main__':
    unittest.main(verbosity=2)
