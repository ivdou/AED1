import unittest
import clase
from queue import LifoQueue as Pila

class test_maximo_pila(unittest.TestCase):
    
    def test_pila_un_solo_elem(self):
        l = [3]
        p = generar_pila(l)
        p_copia = generar_pila(l)
        
        max = clase.maximo(p)
        self.assertEqual(max, 3) 
        self.assertTrue(son_iguales(p, p_copia))
    
    def test_todos_maximos(self):
        l = [3,3]
        p = generar_pila(l)
        p_copia = generar_pila(l)
        
        max = clase.maximo(p)
        self.assertEqual(max, 3) 
        self.assertTrue(son_iguales(p, p_copia))
    
    def test_maximo_al_final(self):
        l = [3, 5, 1, 10]
        p = generar_pila(l)
        p_copia = generar_pila(l)
        
        max = clase.maximo(p)
        self.assertEqual(max, 10) 
        self.assertTrue(son_iguales(p, p_copia))
    
    def test_maximo_al_principio(self):
        l = [30, 5, 1, 10]
        p = generar_pila(l)
        p_copia = generar_pila(l)
        
        max = clase.maximo(p)
        self.assertEqual(max, 30) 
        self.assertTrue(son_iguales(p, p_copia))
    
    def test_maximo_al_principio(self):
        l = [-30, 5, 1, -10]
        p = generar_pila(l)
        p_copia = generar_pila(l)
        
        max = clase.maximo(p)
        self.assertEqual(max, 5) 
        self.assertTrue(son_iguales(p, p_copia))

def son_iguales(p1: Pila[int], p2: Pila[int]): 
    res : bool = True
    while not p1.empty() and not p2.empty(): 
        if p1.get() != p2.get():
            res = False
    if not p1.empty() or not p2.empty():
        res = False 
    return res 

def generar_pila(l: list[int]) -> Pila[int]:
    # [1, 2, 3] ->  Pila(1, 2, 3) 
    p = Pila()
    for i in range(len(l)-1, -1, -1): 
        p.put(l[i])
    return p




if __name__ == '__main__':
    unittest.main(verbosity=2)
