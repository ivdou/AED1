import unittest
from clase_10 import *

class Test_cambiar_matriz(unittest.TestCase):
    def test_varias_filas_y_columnas(self):
        A = [[1,2,3], [4,5,6], [7,8,9]]
        A_copy = []
        for i in range(len(A)):
            A_copy.append(A[i].copy())
        
        cambiar_matriz(A)

        for i in range(len(A)):
            for j in range(len(A[0])):
                self.assertNotEqual(A[i][j], A_copy[i][j])


if __name__ == "__main__":
    unittest.main()