import unittest
from ejercicios import sumar

'''
Ayudamemoria: entre los métodos para testear están los siguientes:

    self.assertEqual(a, b) -> testea que a y b tengan el mismo valor
    self.assertTrue(x)     -> testea que x sea True
    self.assertFalse(x)    -> testea que x sea False
    self.assertIn(a, b)    -> testea que a esté en b (siendo b una lista o tupla)
'''

class EjerciciosTest(unittest.TestCase):

    def test_sumar_cero(self):
        self.assertEqual(sumar(3,0), 3, "test_sumar_cero")

  #  def test_sumar_neg(self):
  #      self.assertEqual(sumar(3,-2), 1, "test_sumar_neg")

  #  def test_sumar_pos(self):
  #      self.assertEqual(sumar(3,5), 8, "test_sumar_pos")


if __name__ == '__main__':
    unittest.main(verbosity=2)



   
