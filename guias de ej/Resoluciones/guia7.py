

# RECORRIDO Y BUSQUEDA EN SECUENCIAS


# ej 1


# 1.1
def pertenece1 (s: list[int], e: int) -> bool:
    return e in s

def pertenece2 (s: list[int], e: int) -> bool:
    B: bool = False
    for x in s: 
        Bx: bool = e == x
        B = B or Bx

    return B

# si no pertenece, avanza hasta i = L , y el retorno resulta Falso

def pertenece3 (s: list[int], e: int) -> bool:  
    L: int = len(s)
    i: int = 0
    while (i < L) and (s[i] != e) : 
        i = i + 1
    return i < L



# 1.3
def suma_total (seq: list[int]) -> int:
    S: int = 0
    for x in seq:
        S = S + x
    return S

# 1.4
def maximo (seq: list[int]) -> int: 
    max: int = seq[0]
    for elem in seq:
        if elem > max:
            max = elem 
    return max

# 1.5
def minimo (seq: list[int]) -> int: 
    min: int = seq[0]
    for elem in seq:
        if elem < min:
            min = elem 
    return min

# 1.6
def ordenados (seq: list[int]) -> bool:
    i: int = 0
    L: int = len(seq)
    
    while i < L - 1:
        if seq[i] >= seq[i+1]: 
            return False  
        i = i + 1


# 1.7
def pos_maximo(seq: list[int]) -> int:
    L: int = len(seq)
    if L == 0:
        return -1
    else: 
        max: int = maximo(seq)
        pos: int = seq.index(max)
        return pos

# 1.8
def pos_miniimo(seq: list[int]) -> int:
    L: int = len(seq)
    if L == 0:
        return -1
    else: 
        min: int = minimo(seq)
        pos: int = seq.index(min)
        return pos

# 19
def long_mayor_a_siete(seq: list[str]) -> bool:
    i: int = 0
    L:int = len(seq)

    for palabra in seq:
        if len (palabra) > 7:
            return True 
    return False

# 1.10 CREO QUE NO SE PUEDE RESOLVER ASI
def invertir_palabra(palabra: str) -> str:
    L: int = len(palabra)
    palabra_invertida: str = ''
    for i in range(L - 1, -1, -1):
        palabra_invertida += palabra[i]
    return palabra_invertida


def es_palindroma(s:str) -> bool:
    return s == invertir_palabra(s)

# 1.11
def iguales_consecutivos(seq: list[int]) -> bool:
    L: int = len(seq) 

    # return temprano, si L < 3
    if L < 3:
        return False
    
    # luego, si L >= 3 comparo indices de a 3

    for i in range(L - 2):
        j: int = i + 1
        k: int = i + 2
        if seq[i] == seq[j] == seq[k]:
                return True
    return False 


# 1.12
def vocales_distintas(palabra: str) -> bool:
    """ Decide si una palabra tiene al menos 3 vocales distintas
     asume palabras sin acentos """

    vocales: list = ['a', 'e', 'i', 'o', 'u']

    # capturo las vocales distintas en la palabra

    vocales_en_palabra: list[int] = []

    for letra in palabra:
        if (letra in vocales) and (not letra in vocales_en_palabra):
            vocales_en_palabra.append(letra)

    return len(vocales_en_palabra) >= 3


# 1.13


# FLITRADO, MODIFICADO Y PROCESADO DE SECUENCIAS


# ej 2 




# ej 3


def promedio(seq: list[int]) -> float:
    N: int = len(seq)
    suma = 0

    for elem in seq:
        suma = suma + elem 

    prom: float = suma / N
    return prom

def todas_mayores_o_iguales(seq: list[int], x: float) -> bool: 
    res: bool = True
    for elem in seq:
        if elem < x:
            res = False
    return res 

def resultado_materia(notas: list[int]) -> int:
    nota_promedio: float = promedio(notas)
    notas_mayores_o_iguales_a_cuatro: bool = todas_mayores_o_iguales(notas, 4)

    res: int = 0
    if notas_mayores_o_iguales_a_cuatro and nota_promedio >= 7:
        res = 1
    elif notas_mayores_o_iguales_a_cuatro and (4 <= nota_promedio < 7):
        res = 2
    else: 
        res = 3
    return res


# MATRICES

Fila = list[int]
Columna = list[int]
Matriz = list[Fila]

# ej 5


# ej 6 

# 6.1
def es_matriz(m: Matriz) -> bool:

    res: bool = True
    cant_filas: int = len(m)
    
    if cant_filas == 0: 
        res = False 

    elif len(m[0]) == 0: 
        res = False

    else:
        for fila in m: 
            dim_primer_fila = len(m[0])
            if len(fila) != dim_primer_fila:
                res = False

    return res

# 6.2
def filas_ordenadas(m: Matriz, res: list[bool]) -> None: 

    res.clear()

    for fila in m:
        fila_ordenada: bool = ordenados(fila)   # implementada en 1.6
        res.append(fila_ordenada)

# 6.3

def columna(m: Matriz, c: int) -> Columna:
    
    columna_c: Columna = []
    
    for fila in m:
        elem_c: int = fila[c]
        columna_c.append(elem_c)
    
    return columna_c

# 6.4

def columnas_ordenadas(m: Matriz) -> bool:

    cant_columnas: int = len(m[0])
    columnas: list[Columna] = []

    # armo lista de columnas
    for i in range(cant_columnas): 
        columna_i: Columna = columna(m, i)
        columnas.append(columna_i)

    res: bool = True
    
    # itero sobre la lista de columnas
    for col in columnas: 
        if not ordenados(col): 
            res = False

    return res


# 6.5

def transponer(m: Matriz) -> Matriz: 
    columnas_m : list[Columna] = []
    cant_columnas: int = len(m[0])

    m_transpuesta: Matriz = Matriz()


    for i in range(cant_columnas):
        m_transpuesta.append(columna(m,i))

    return m_transpuesta


# 1  0 1 5
# 2 -1 3 0
# 6  4 0 1

# 1  2 6
# 0 -1 4
# 1  3 0
# 5  0 1


