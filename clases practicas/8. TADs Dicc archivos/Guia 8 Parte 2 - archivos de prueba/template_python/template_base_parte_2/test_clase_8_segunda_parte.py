from base_clase_8_segunda_parte import (calcular_promedio_por_estudiante, contar_lineas,
                                        clonar_sin_comentarios, agrupar_por_longitud, la_palabra_mas_frecuente)

import unittest


class TestPromedio(unittest.TestCase):
    def test_unico(self):
        notas = [("juan", 8.0)]
        resultado_esperado = {"juan": 8.0}
        resultado = calcular_promedio_por_estudiante(notas)
        self.assertEqual(resultado, resultado_esperado)


class TestAgruparPorLongitud(unittest.TestCase):
    def test_agrupa_archivo_palabras(self):
        archivo = "archivos_test/archivo_palabras.txt"
        esperado = {5: 4, 3: 8, 8: 1, 4: 1, 2: 3, 6: 2, 7: 1}
        resultado = agrupar_por_longitud(archivo)
        self.assertEqual(resultado, esperado)


class TestContarLineas(unittest.TestCase):
    def test_contar_lineas_archivo_vacio(self):
        archivo = "archivos_test/archivo_vacio.txt"
        resultado = contar_lineas(archivo)
        self.assertEqual(resultado, 0)


class TestClonarSinComentarios(unittest.TestCase):
    def test_clonar_archivo_vacio(self):
        archivo_entrada = "archivos_test/archivo_vacio.txt"
        archivo_salida = "archivos_test/archivo_salida.txt"
        clonar_sin_comentarios(archivo_entrada, archivo_salida)
        f = open(archivo_salida, 'r')
        contenido = f.read()
        f.close()
        self.assertEqual(contenido, "")


class TestPalabraMasFrecuente(unittest.TestCase):

    def test_frecuente_archivo_palabras(self):
        archivo = "archivos_test/archivo_frecuencia_palabras.txt"
        esperado = ["manzana", "pera", "uva"]  # puede ser cualquiera de estas
        resultado = la_palabra_mas_frecuente(archivo)
        self.assertIn(resultado, esperado)


if __name__ == '__main__':
    unittest.main(verbosity=2)
