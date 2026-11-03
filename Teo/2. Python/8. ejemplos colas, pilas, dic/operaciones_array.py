# Importar módulo array
import array

# Declarar lista con valores numéricos
lista1:list = [1, 0, 1, 0, 1, 1, 0, 0]
#lista1:list = ["Pepito", "Pepita", "Juancito"]

# Obtener cadena con todos los tipos de arrays disponbiles
print("Todos los tipos de arrays disponbiles: " + array.typecodes)  # 'bBuhHiIlLqQfd'

# Declarar 'array1' de tipo 'char sin signo' con datos de 'lista1'
array1 = array.array('B', lista1)
print("array1: " + str(array1))

# Declarar 'array2' de tipo 'float' con datos de 'lista1'
array2 = array.array('f', lista1)
print("array2: " + str(array2))

# Declarar 'array3' de tipo 'int sin signo' con datos de 
# 'lista1' en orden inverso 
array3 = array.array('I', (elemento for elemento in lista1[::-1]))
print("array3: " + str(array3))

# Declarar 'array4' de tipo 'char con signo' a partir cadena de bytes
cadena = b'Python'
array4 = array.array('b', cadena)
print("array4: " + str(array4))

# Declarar 'array5' de tipo 'int con signo' con valores del 0 al 9
array5 = array.array('i', range(10))
print("array5: " + str(array5))

# Obtener tipo de array y datos de 'array1'
array1  # array('B', [1, 0, 1, 0, 1, 1, 0, 0])
print("array1: " + str(array1))

# Obtener tipo de array y datos de 'array2'
array2  # array('f', [1.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0])
print("array2: " + str(array2))

# Obtener tipo de array y datos de 'array3'
array3  # array('I', [0, 0, 1, 1, 0, 1, 0, 1])
print("array3: " + str(array3))

# Obtener tipo de array y datos de 'array4'
array4  # array('b', [80, 121, 116, 104, 111, 110])
print("array4: " + str(array4))

# Obtener tipo de array y datos de 'array4'
array5  # array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("array5: " + str(array5))

# Obtener tipo de objeto de 'array1'
type(array1)  # array.array
print("Type de array1: " + str(type(array1)))

# Obtener tipo de array de 'array1', 'array2' y 'array2'
array1.typecode  # 'B'
print("Typecode array1: " + array1.typecode)

array2.typecode  # 'f'
print("Typecode array2: " + array2.typecode)

array3.typecode  # 'I'
print("Typecode array3: " + array3.typecode)

# Crear una lista a partir de un array e imprimirla
lista3:list  = list(array3) 
print("Creo una lista3 a partir de array3: " + str(lista3))

# Crear una lista a partir de otra lista e imprimirla
lista4:list = list(lista3)
print("Creo una lista4 a partir de lista3: " + str(lista4))

lista3.remove(0)
print("Imprimo la lista3 luego de remover el 0: " + str(lista3))
print("Imprimo la lista4 luego de remover el 0: " + str(lista4))

# Añadir nuevos elementos a 'array1' y 'array2'
print("Antes de agregar 1: array1: " + str(array1))
array1.append(1)
print("Despues de agregar 1: array1: " + str(array1))
array1.append(0)
print("Despues de agregar 0: array1: " + str(array1))

# Obtener número de elementos de 'array1', 'array2' y 'array3'
len(array1)  # 10
print("Tamaño array1: " + str(len(array1)))

len(array2)  # 9
print("Tamaño array2: " + str(len(array2)))

# Obtener el número de veces que se repite un valor en un array
array1.count(1)  # 5
print("Cantidad de apariciones de 1 en array1: " + str(array1.count(1)))

array3.count(0)  # 4
print("Cantidad de apariciones de 0 en array3: " + str(array3.count(0)))

# Obtener posición donde aparece por primera vez elemento buscado
array1.index(1)  # 0
print("Primera posición del 1: " + str(array1.index(1)))

# Insertar un elemento delante de la posición indicada en 'array1'
print("Antes de insertar 10: array1: " + str(array1))
array1.insert(3, 10)
print("Despues de insertar 10: array1: " + str(array1))
 


# Borrar el primer elemento en 'array1' que coincida con el indicado
array1.remove(10)
print("Despues de remover 10: array1: " + str(array1))
array1  # array('B', [1, 0, 1, 0, 1, 1, 0, 0, 1])
