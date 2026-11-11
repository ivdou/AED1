import unittest
from guia10 import *

        
lista_input: list[Producto_Stock] = [
    ('Antibiotico',6),
    ('Antiparasitario',12),
    ('Suplemento',8),
    ('Snack',12),
    ('Pretal',6),
    ('Juguete',6),
    ('Antibiotico',3),
    ('Antiparasitario',9),
    ('Snack',10),
    ('Antibiotico',1),
    ('Antiparasitario',7),
    ('Snack',8),
    ('Antibiotico',12),
    ('Antiparasitario',15),
    ('Snack',5),   
    ('Pretal',5),
    ('Juguete',5),
    ('Antibiotico',10),
    ('Antiparasitario',13),
    ('Snack',4), 
    ('Snack',20),
    ('Juguete',10)
]

 

class test_stock_productos(unittest.TestCase):

    def test_stock_productos_correcto(self):

        dict_esperado: dict[Producto, tuple[Stock, Stock]] = {
            'Antibiotico': (1, 12),
            'Antiparasitario': (7, 15), 
            'Suplemento': (8, 8), 
            'Snack': (4, 20), 
            'Pretal': (5, 6), 
            'Juguete': (5, 10)
        }

        self.assertEqual(
            stock_productos(lista_input),
            dict_esperado
        )

    def test_diccionario_lista_stock(self):

        dict_esperado: dict[Producto, list[Stock]] = { 
            'Antibiotico': [6, 3, 1, 12, 10],
            'Antiparasitario': [12, 9, 7, 15, 13], 
            'Suplemento': [8], 
            'Snack': [12, 10, 8, 5, 4, 20], 
            'Pretal': [6, 5], 
            'Juguete': [6, 5, 10]
        }
        
        self.assertEqual(
            diccionario_lista_stock(lista_input),
            dict_esperado
        )

class test_un_responsable_por_turno(unittest.TestCase):

    def test_todos_con_un_responsable(self):

        grilla_horaria: Grilla = [
            [ 'Sergio', 'Andrea', 'Julian'],
            [ 'Sergio', 'Andrea', 'Julian'],
            [ 'Sergio', 'Andrea', 'Julian'],
            [ 'Sergio', 'Andrea', 'Julian'],
            [ 'Debora', 'Debora', 'Debora'],
            [ 'Debora', 'Debora', 'Debora'],
            [ 'Debora', 'Debora', 'Debora'],
            [ 'Debora', 'Debora', 'Debora']]

        res_esperado: list[tuple[bool, bool]] = [
            (True, True),
            (True, True), 
            (True, True)
        ]


        self.assertEqual(
            un_responsable_por_turno(grilla_horaria),
            res_esperado
        )

    def test_un_turno_con_dos_responsables(self):
        grilla_horaria: Grilla = [
            [ 'Sergio', 'Andrea', 'Julian'],
            [ 'Sergio', 'Andrea', 'Julian'],
            [ 'Sergio', 'Andrea', 'Julian'],
            [ 'Sergio', 'Andrea', 'Julian'],
            [ 'Debora', 'Debora', 'Debora'],
            [ 'Debora', 'Debora', 'Debora'],
            [ 'Debora', 'Ivan', 'Debora'],
            [ 'Debora', 'Ivan', 'Debora']]

        res_esperado: list[tuple[bool, bool]] = [
            (True, True),
            (True, False), 
            (True, True)
        ]


        self.assertEqual(
            un_responsable_por_turno(grilla_horaria),
            res_esperado
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)