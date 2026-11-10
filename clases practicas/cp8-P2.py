#resuloción ejercicios de listas de parcial y 
#ejemplos sobre manejo de tuplas, dicc, colas y pilas

from typing import TextIO # Importo el tipo de dato TextIO para archivos



'''
Ejercicio 1 [2 puntos]
 Implementar la función cantidad_parejas_que_suman:
 problema cantidad_parejas_que_suman (in s: seq⟨Z⟩, in n: Z) : Z {
    requiere: { - }
    asegura: { res es la cantidad de parejas s[i] y s[j] de números de s tales que s[i] + s[j] = n (con i < j) }
 }

 Ejemplo: cantidad_parejas_que_suman([1,3,2,5,4,8], 5) debe devolver 2
'''
def cantidad_parejas_que_suman(s: list[int], n: int) -> int:
    res : int = 0
    
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] + s[j] == n:
                res += 1
    
    return res

#print(cantidad_parejas_que_suman([1,3,2,5,4,8], 5))

'''
3) Ejercicio 3 [2,5 puntos]

Implementar la función intercambiar_e_invertir_columnas:

problema intercambiar_e_invertir_columnas(inout A: seq⟨seq⟨Z⟩⟩, in col1: Z, in col2: Z) {
  requiere: { Todas las filas de A tienen la misma longitud (estrictamente positiva)}
  requiere: { |A| > 0}
  requiere: { 0 ≤ col1 < |A[0]| }
  requiere: { 0 ≤ col2 < |A[0]| }
  requiere: { col1 ≠ col2 }
  modifica: { A }
  asegura: { A tiene exactamente las mismas dimensiones que A@pre }
  asegura: { A[i][j] = A@pre[i][j] para todo i, j en rango tal que j ≠ col1 y j ≠ col2 }
  asegura: { A[i][col1] = A@pre[|A|-1-i][col2] para todo i tal que 0 ≤ i < |A| }
  asegura: { A[i][col2] = A@pre[|A|-1-i][col1] para todo i tal que 0 ≤ i < |A| }
}


Ejemplo: Si mat = [[1,2,3],[40,50,60], [-7,-8,-9]], luego de ejecutarse 
 intercambiar_e_invertir_columnas(mat,1,2)
 debería ocurrir que print(mat) muestre [[1, -9, -8], [40, 60, 50], [-7, 3, 2]]
  
'''
def intercambiar_e_invertir_columnas(A: list[list[int]], col1: int, col2: int) -> None:
    for fila in range(len(A)):
        valor_en_col1: int = A[fila][col1]
        A[fila][col1] = A[len(A)-fila-1][col2]
        A[len(A)-fila-1][col2] = valor_en_col1

mat = [[1,2,3],[40,50,60], [-7,-8,-9]]
intercambiar_e_invertir_columnas(mat, 1,2)
#print(mat)

from typing import TypeVar #, Tuple
from queue import LifoQueue as Pila
from queue import Queue as Cola


T = TypeVar('T')

#un error común es poner "while not (copia.empty):", sin poner los paréntesis en empty.
#recuerden ponerlo porque si no el comportamiento de la función no será el esperado

def copiar_cola (original:Cola )-> Cola:
    res: Cola = Cola()
    cola_tmp: Cola = Cola()

    while not (original.empty()):
        v = original.get()
        res.put(v) 
        cola_tmp.put(v) #guardo en una cola temporal para luego restaurar

    #restauro la cola original
    while not (cola_tmp.empty()):
        v = cola_tmp.get()
        original.put(v)

    return res

def imprimir(cola:Cola ):
    copia = copiar_cola (cola)
    while not (copia.empty()):
        print(copia.get())


mi_cola:Cola[int] = Cola()

# Agregamos elementos a la cola
mi_cola.put(11)
mi_cola.put(22)
mi_cola.put(3)
copia = copiar_cola(mi_cola)
print(copia.queue)
mi_lista = list(copia.queue)
print(mi_cola.queue)



#ejemplo uso de pila
pila:Pila = Pila()

print(pila.empty())

#agrego elementos
pila.put(1)
pila.put(2)
pila.put(3)

print(pila.empty())
print("Size", pila.qsize())

#saco e imprimo los elementos de la pila
print(pila.get())
print(pila.get())
print(pila.get())

print("Size", pila.qsize())
print(pila.empty())




#Ejemplos de uso de diccionario

#creo un dicc con algunos pares de clave-valor
mi_dicc: dict[str, str] = {
    'auto': 'car',
    'sol': 'sun',
    'luna': 'moon'
}

#agrego clave-valor
mi_dicc['una_clave'] = 'un_valor'

#reemplazo el valor de una clave
mi_dicc['una_clave'] = "nuevo valor"


#recupero un valor
v:str = mi_dicc['una_clave']



#recupero un valor y lo elimino del dicc
v:str = mi_dicc.pop('una_clave')

#recorro un dicc, lo imprimo y lo copio a otro diccionario
nuevo_dic: dict[str, str] = {} #creo un dicc vacio

# recupero las claves y, con cada clave, recupero su valor, lo imprimo y lo agrego a otro diccionario
claves:list[str] = mi_dicc.keys() 
for clave in claves:    
    valor:str = mi_dicc[clave]
    print(f'{clave} - {valor}') 
    nuevo_dic[clave] = valor #lo agrego al nuevo diccionario


#vacío el dicc
nuevo_dic.clear()


#otra forma de recorrer un dicc
otro_dic: dict[str, str] = {} #creo un dicc vacio
for clave, valor in mi_dicc.items():    
    print(f'{clave} - {valor}') 
    otro_dic[clave] = valor

# recupero solo los valores y los imprimo
valores:list[str] = otro_dic.values() 
for v in valores:    
    print(v)  

#truco para pasar de una pila o cola a una lista
lista = list(mi_cola.queue)
#Queue.queue: Devuelve una referencia al objeto interno que almacena los elementos de la cola (es un objeto tipo lista)
#list(...): Convierte esa estructura en una lista.
#algo parecido se puede hacer con las claves de un diccionario
lista = list(otro_dic.keys())
#lo que devuelve keys() no es estricamente una lista, pero se puede crear una así.

#ejemplo de dicc con algunos pares de valores de distinto tipo
#para tipar, si la versión de python es > 3.10, se puede usar esta sintaxis
#si es una versión más vieja, se puede usar dict[str, Union[str, int]]
info_pais_francia:dict[str, str | int] = {'Capital':'París',
                                        'Campeonatos de Mundo':2}


def repaso_creacion() -> None:
    dic: dict[str, float] = {}
    dic ["nombre_clave"] = 3.14
    print ("valor de la clave: ", dic ["nombre_clave"])

    tupla:tuple[str, float] = ("primer_elemento", 1.14)
    print(tupla[0])
    print(tupla[1])

    #tupla[0] = "nuevo_primer_elemento" ESTO DA ERROR. No se puede modificar
    # directamente un valor de una tupla en Python porque las tuplas son inmutables. 

    tupla = ("nuevo", 5) #crea una tupla nueva, no modifica la vieja
    print(tupla[0])
    print(tupla[1])

    tupla_aux = tupla # 2 variables hacen referencia a la misma tupla 
    #(ambas variables apuntan al mismo objeto en memoria.)
    tupla_aux  = ("renuevo", 8) 
    print(tupla_aux[0])
    print(tupla_aux[1])
    print(tupla[0])
    print(tupla[1])

    #LA SIGUIENTE LÍNEA ESTÁ MAL
    una_no_tupla :tuple[int,int] = [1,2] # [] en vez de ()
    #ESTO CREA UNA LISTA, NO UNA TUPLA
    print (una_no_tupla)

    ESTO_ES_UNA_TUPLA = ("HOLA", "CHAU")
    ESTO_ES_UNA_LISTA = ["HOLA", "CHAU"]
    ESTO_ES_UNA_LISTA_CON_UNA_TUPLA = [("HOLA", "CHAU")]
    print(ESTO_ES_UNA_TUPLA)
    print(ESTO_ES_UNA_LISTA)
    print(ESTO_ES_UNA_LISTA_CON_UNA_TUPLA)

    ESTO_ES_UNA_LISTA.append("nuevo elem")
    print(ESTO_ES_UNA_LISTA)
    misma_lista = ESTO_ES_UNA_LISTA

    #esto es un error común
    ESTO_ES_UNA_LISTA = ESTO_ES_UNA_LISTA.append("otro elem")
    print (ESTO_ES_UNA_LISTA)
    print (misma_lista)


    una_pila:Pila[int] = Pila()
    una_cola:Cola[int] = Cola()
    un_dic = {}
    una_tupla:tuple[str, float] = ("no se puede crear vacía", 0)
    una_lista:list[str, float] = []
    print(una_cola)
    print(una_pila)
    print(una_tupla, un_dic, una_lista)


repaso_creacion()



#creo un dicc donde la clave representa un día y el valor es una tupla con la temp mín y max
temp_por_dia: dict[int, (float, float)] = {
    1: (10.5, 20),
    2: (10.3, 20.6),
    3: (1.5, 20)
}

def dia_de_menor_minima (temps :dict[int, (float, float)] ) -> int:
    #asumo que hay por lo menos un día con su temp.
    res: int = list(temps.keys()) [0]  
    temp_min = temps [res] [0] 
    for c, v in temps.items():    
        min_dia:float = v[0]  
        if temp_min > min_dia:
            temp_min = min_dia
            res = c

    return res

dia = dia_de_menor_minima (temp_por_dia)
print(dia)














"""
Ejercicio 17. Dada una secuencia de tuplas, donde cada tupla tiene en la primera componente el nombre de un estudiante
y en la segunda componente la nota que sacó en un examen, se pide devolver un diccionario con los promedios de todos los
estudiantes. La clave del diccionario debe ser el nombre del estudiante y el valor el promedio de todos sus exámenes.
calcular promedio por estudiante(notas : list[tuple[str, float]]) → dict[str, float]
"""
# Ejercicio 17
def calcular_promedio_por_estudiante(notas: list[tuple[str, float]]) -> dict[str, float]:
    
    # Inicializamos un diccionario vacío para guardar la respuesta
    res: dict[str, float] = {}
    
    # Recorremos las notas
    for nota in notas:
        # El estudiante es el primer elemento de la tupla
        estudiante:str = nota[0]

        # Si todavía no calcule su promedio, lo hago. Si ya lo calculé, lo ignoro
        # Noten que aca nos estamos fijando si estudiante es una CLAVE del diccionario res
        estudiantes_ya_agregados:list[str] = list(res.keys())
        if not pertenece (estudiantes_ya_agregados, estudiante):
            # Calculamos el promedio con la función auxiliar
            prom:float = promedio_de_estudiante(estudiante,notas)

            # Guardo el promedio como el valor asociado a la clave estudiante
            res[estudiante] = prom
        
    # Devolvemos el diccionario
    return res

#esta implementación es similar a la anterior, pero con menos variables
def calcular_promedio_por_estudiante2(notas: list[tuple[str, float]]) -> dict[str, float]:

    res: dict[str, float] = {}
    for nota in notas:
        if not pertenece (list(res.keys()), nota[0]): 
            res[nota[0]] = promedio_de_estudiante(notas, nota[0])
    
    return res

def pertenece (cadena: list[T], elem:T) -> bool:
    for i in cadena:
        if i == elem: 
            return True
    return False

def promedio_de_estudiante(notas:list[tuple[str,float]], estudiante:str) -> float:
    # Inicializamos variables para llevar el recuento de la suma y la cantidad de notas
    suma_notas:float = 0.0
    cant_notas:int = 0

    for nota in notas:
        estudiante_actual:str = nota[0]
        # Sumamos la nota actual solo si es de nuestro estudiante
        if estudiante_actual == estudiante:
            suma_notas += nota[1]
            cant_notas += 1
    
    return suma_notas / cant_notas


print(calcular_promedio_por_estudiante([["a", 1], ["a", 3], ["b", 1], ["a", 2], ["b", 7]]))

notas = [
    ("Alice", 8.5),
    ("Bob", 7.0),
    ("Alice", 9.0),
    ("Charlie", 6.0),
    ("Bob", 8.5),
    ("Alice", 7.5),
    ("Charlie", 9.5)
]

# Llamada a la función
promedios = calcular_promedio_por_estudiante(notas)
print(promedios)  # Salida esperada: {'Alice': 8.33, 'Bob': 7.75, 'Charlie': 7.75}


# Ejercicio 21.1
def contar_lineas(nombre_archivo : str) -> int:
    res: int = 0

    # Abro archivo en modo lectura
    archivo:TextIO = open(nombre_archivo, "r")
    res = len(archivo.readlines())

    # Siempre debemos cerrar el archivo luego de usarlo
    archivo.close()

    return res

nombre_archivo:str = "ejemplo.txt"
print("El archivo", nombre_archivo, "tiene", contar_lineas(nombre_archivo), "lineas\n\n")

# Ejercicio 22
def clonar_sin_comentarios(nombre_archivo_entrada: str, nombre_archivo_salida : str) -> None:
     # Abro archivo en modo lectura
    arch_r:TextIO = open(nombre_archivo_entrada, "r")

     # Abro archivo en modo escritura
    arch_w:TextIO = open(nombre_archivo_salida, "w")
    
    lineas_archivo:list[str] = arch_r.readlines()
    arch_r.close()

    for linea in lineas_archivo:
        if not es_comentario(linea):
            arch_w.write(linea)
    
    arch_w.close()

def es_comentario(linea: str) -> bool:
    return sacar_espacios(linea)[0] == "#"

# Saca los espacios al principio del string
def sacar_espacios(linea: str) -> str:
    res: str = ""
    solo_espacios: bool = True
    for letra in linea:
        if letra != ' ':
            solo_espacios = False   
        if not solo_espacios:
            res = res + letra
    
    return res

#Probamos sacar_espacios
# print(sacar_espacios("   123 asda"))
# print(sacar_espacios("      45   s"))
# print(sacar_espacios("89 ."))
# print(sacar_espacios(""))
# print(sacar_espacios("sin_espacios"))

salida_archivo:str = "salida.txt"
print("El archivo", nombre_archivo, "tiene", contar_lineas(nombre_archivo), "lineas")
clonar_sin_comentarios(nombre_archivo, salida_archivo)
print("El archivo", salida_archivo, "tiene", contar_lineas(salida_archivo), "lineas\n\n")

# Ejercicio 16
def agrupar_por_longitud(nombre_archivo: str) -> dict[int, int]:
    res: dict[int, int] = {}

    for palabra in palabras_de_arch(nombre_archivo):
        longitud = len(palabra)
        if pertenece(longitud, list(res.keys())):
            res[longitud] += 1
        else:
            res[longitud] = 1

    return res

def palabras_de_arch(nombre_archivo: str) -> list[str]:
    res:list[str] = []

     # Abro archivo en modo lectura
    arch: TextIO = open(nombre_archivo, "r")
    lineas_archivo:list[str] = arch.readlines()
    arch.close()
    
    for linea in lineas_archivo:
        for palabra in palabras(linea):
            res.append(palabra)
    return res

def palabras(línea: str) -> list[str]:
    res: list[str] = []
    palabra_actual: str = ""
    
    for caracter in línea:
        if es_separador(caracter):
            agregar_si_no_es_vacía(res, palabra_actual)
            palabra_actual = ""
        else:
            palabra_actual += caracter

    agregar_si_no_es_vacía(res, palabra_actual)
    return res

def es_separador(caracter: str) -> bool:
    return caracter == ' ' or es_puntuación(caracter)


def es_puntuación(caracter: str) -> bool:
    caracteres_de_puntuación = [
        '.', ',', ';', ':', '"', '\'', '¡', '!', '¿', '?',
        '(', ')', '[', ']', '{', '}', '>', '<', '\n'
    ]
    return caracter in caracteres_de_puntuación


def agregar_si_no_es_vacía(lista: list[str], palabra: str) -> None:
    if palabra != "":
        lista.append(palabra)

# Ejercicio 18
def la_palabra_mas_frecuente(nombre_archivo : str) -> str:
    frecuencias: dict[str, int] = frecuencias_palabras(nombre_archivo)

    # Busco la palabra con más apariciones
    palabra_mas_frecuente: str = ""
    max: int = 0

    for clave, valor in frecuencias.items():
        if valor > max:
            max = valor
            palabra_mas_frecuente = clave

    return palabra_mas_frecuente

def frecuencias_palabras(nombre_archivo):
    frecuencias: dict[str, int] = {}

    # Armo un diccionario cuyas claves son las palabras, y los valores son la cant. de apariciones de la palabra
    for palabra in palabras_de_arch(nombre_archivo):
        if pertenece(palabra, list(frecuencias.keys())):
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

print("La palabra más frecuente en el archivo", nombre_archivo, "es:", la_palabra_mas_frecuente(nombre_archivo), "\n\n")


'''
Ejercicio 2 [2,5 puntos]

En un supermercado tenemos una fila de clientes esperando para ser atendidos por algún cajero. Cada cliente tiene un nombre, un método de pago y una cantidad de productos. La fila de clientes se representa como una Cola de String x String x Z, donde el primer elemento es el nombre del cliente, el segundo es el método de pago y el tercero es la cantidad de productos. Implementar la función pasar_por_autoservicio:
Nota: los métodos de pago son strings conformados por letras minúsculas.

problema pasar_por_autoservicio (inout clientes: Cola⟨ String x String x Z ⟩) : String {
  requiere:{ Las primeras componentes de clientes son strings no vacíos y todos distintos entre sí }
  requiere:{ Las terceras componentes de clientes son números positivos }
  requiere:{ Existe al menos un elemento c dentro de la cola clientes tal que c1 ≠ "efectivo" y c2 ≤ 15 }
  modifica: { clientes }
  asegura: { Sea c el primer elemento insertado en la cola clientes tal que c1 ≠ "efectivo" y c2 ≤ 15, entonces res = c0 }
  asegura: { clientes contiene todos los elementos de clientes@pre excepto la tupla que contiene a res en su primera posición, en el mismo orden que en clientes@pre. }
}

Ejemplo: pasar_por_autoservicio(clientes) debe devolver "Bruno" (y quitar su tupla de la cola)
si clientes es una cola en la cual se insertaron (en orden) los siguientes elementos:
1.  ("Ana", "efectivo", 13)
2.  ("Juan", "qr", 22)
3.  ("Bruno", "tarjeta", 14)

Ejercicio 4 [2 puntos]

Se realizaron dos censos en los cuales se le preguntó a cada persona en que localidad vive. Estos datos fueron almacenados en dos diccionarios cuyas claves son los nombres de las personas, y sus valores las localidades en las cuales viven. Implementar la función mantuvieron_residencia:

problema mantuvieron_residencia (in censo1: Diccionario⟨String,String⟩, in censo2: Diccionario⟨String,String⟩): Diccionario⟨String,Z⟩ {
  requiere: { Las claves de censo1 son las mismas que las claves de censo2 }
  asegura: { k es clave de res si y sólo si existe alguna clave p en censo1 tal que al obtener su valor tanto en censo1 como en censo2, este es igual a k }
  asegura: { El valor de cada clave de res representa la cantidad de personas que en ambos censos vivía en esa localidad, es decir, que mantuvieron su residencia en la misma localidad entre ambos censos }
}


Ejemplo: mantuvieron_residencia({'Juan': 'Merlo', 'Ana': 'Merlo'}, {'Juan': 'Castelar', 'Ana': 'Merlo'})

debe devolver {'Merlo': 1}
  

'''