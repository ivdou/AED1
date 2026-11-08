import unittest
from guia7 import *

class test_quien_gana_tateti(unittest.TestCase):

    def test_gana_X_diag_principal(self):

        t = [['X','O', 'X'],
            ['O', 'X', ''],
            ['', '', 'X']]

        self.assertEqual(quien_gana_tateti(t), 1)

    def test_no_gana_nadie(self):
        t = [['O','X', 'X'],
            ['X', 'O', 'O'],
            ['X', 'O', 'X']]

        self.assertEqual(quien_gana_tateti(t), 2)

    def test_gana_O_columna(self):

        t = [['X','O', 'X'],
            ['', 'O', ''],
            ['', 'O', 'X']]

        self.assertEqual(quien_gana_tateti(t), 0)


    def test_gana_X_fila(self):
        
        t = [['X','X', 'X'],
            ['', 'O', 'O'],
            ['O', '', 'X']]

        self.assertEqual(quien_gana_tateti(t), 1)
        

if __name__ == '__main__':
    unittest.main(verbosity=2)