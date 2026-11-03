import math

#************* Ejercicio 1 *************

# Decidir si un vector esta ordenado tanto ascendente como descendentemente
def esta_ordenado_asc(v):
    i = 0
    longitud = len(v)
    esMenor = False
    while i <= longitud - 2 and esMenor:
        esMenor = v[i] <= v[i + 1]
        i += 1
    return i == longitud - 1


def esta_ordenado_desc(v):
    longitud = len(v)
    i = 0
    esMayor = True
    while i <= longitud - 2 and esMayor:
        esMayor = v[i] >= v[i + 1]
        i += 1
    return i == longitud - 1


def esta_ordenado(v):
    longitud = len(v)
    if longitud == 0 or longitud == 1:
        return True
    else:
        return esta_ordenado_desc(v) and esta_ordenado_asc(v)



#************* Ejercicio 2 *************/

# Decidir si un numero es primo.
def es_primo(numero:int):
    if numero > 2:
        i = 2
        divide = False
        while i <= numero and not divide:
            divide:bool = numero % i != 0
            i += 1
        return i == numero
    elif numero == 2:
        return True
    else:
        return False


#************* Ejercicio 3 *************

# Decidir si un elemento dado pertenece a la lista.
def pertenece(elemento:int, v:list[int]):
    longitud = len(v)
    if longitud == 0:
        return False
    else:
        i = 0
        sigo = True
        while i < longitud and sigo:
            sigo = v[i] != elemento
            i += 1
        return i < longitud



#************* Ejercicio 4 *************

# Encontrar el desvio estandar de una lista de floats.

def desvio_estandar(v: list[float]):
    def suma_de_cuadrados(v):
      suma_de_cuadrados:int = 0
      for i in range(len(v)):
          suma_de_cuadrados += suma_de_cuadrados + (v[i] - promedio(v)) ** 2
      return suma_de_cuadrados

    def promedio(v:list[float]):
      longitud = len(v)
      suma:float = 0
      for i in range(longitud):
          suma += v[i]
      return suma / longitud
    
    return math.sqrt(suma_de_cuadrados(v) / len(v))








#************* Ejercicio 5 *************/

# Encontrar el maximo comun divisor de dos numeros

def maximo_comun_divisor(x, y):
  def maximo(x, y):
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    if x > y:
        return x
    else:
        return y

  def minimo(x, y):
    if x < 0:
        x = -x
    if y < 0:
        y = -y
    if x < y:
        return x
    else:
        return y
    
  a = maximo(x, y)
  b = minimo(x, y)
  resto = 0
  while b != 0 and b != 1:
      resto = a % b
      b = a
      a = resto
  if a == 0:
      return a
  else:
      return 1
    




#************* Ejercicio 6 *************

# Para una lista de enteros, calcular la sumatoria del doble de los elementos positivos y pares.
def suma_doble(v:list[int]):
    suma = 0
    for i in range(len(v)):
        if v[i] % 2 == 0 and v[i] >= 0:
            suma =+ v[i] * 2
    return suma






#************* Ejercicio 7 *************

"""El archivo SensadoRemoto.txt contiene una lista de valores reales provenientes de una estacion
de medicion de una variable fisica dada, cuyos valores son positivos menores a 1.
Escribir un programa que calcule el promedio de los valores tomados durante un periodo de tiempo.
Verificar el resultado obtenido."""

def valor_medio():
    # El primer parámetro es el path al archivo
    # El segundo parámetro "r" indica que es una operación de sólo lectura (no se va a modificar el archivo)
    miArchivo = open("datos/SensadoRemoto.txt", "r")
    acum = 0.0
    cont = 0
    # la variable "val" tiene el valor de cada palabra del archivo de texto
    for val in miArchivo.read().split():
        acum += float(val)
        cont += 1
    miArchivo.close()
    return acum / cont


#************* Ejercicio 8 *************

#Contar la cantidad de palabras que hay en un archivo de texto.
def cant_palabras(filename):
    # El primer parámetro es el path al archivo
    # El segundo parámetro "r" indica que es una operación de sólo lectura (no se va a modificar el archivo)
    miArchivo = open(filename, "r")
    cont = 0
    # la variable "palabra" tiene el valor de cada palabra del archivo de texto
    # En este caso, se usa el método split() para separar las palabras, pero este
    # método no pueden usarlo en sus implementaciones (como en el TP). Deben implementar su propia
    # función para separar las palabras.
    for palabra in miArchivo.read().split():
        cont += 1
    miArchivo.close()
    return cont


