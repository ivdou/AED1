# Importar módulo array
import array
import sys

# Declarar lista con valores numéricos
lista1 = [1, 0, 1.5, 0, 1, 1, 0, 0]
array2 = array.array('u', ['a','b','c'])
# Declarar 'array1' de tipo 'char sin signo' con datos de 'lista1'
array1 = array.array('f', lista1)
lista1[2] = "hola"
#array1 = array.array('f', lista1)

array3 =  array.array('f')
print(len(array3))
print(sys.getsizeof(array1))
print(array2)
print(lista1)
lista2 = list(array1)
print(len(lista2))
#print("Buffer info: " + str(array1.buffer_info()))
#print("Buffer info: " + str(lista1.buffer_info()))



