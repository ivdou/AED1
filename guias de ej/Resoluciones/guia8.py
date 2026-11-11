from queue import LifoQueue as Pila
from queue import Queue as Cola
from typing import TextIO 

def mostrar_pila(p: Pila) -> None:

    p_aux: Pila = Pila()

    # Impresion de elementos y guardado en p_aux
    while not p.empty(): 

        elem = p.get()
        print(elem)
        p_aux.put(elem)

    # Restauración de p, desde p_aux
    while not p_aux.empty():

        elem = p_aux.get()
        p.put(elem)

def copiar_pila(p: Pila) -> Pila:
    p_copia: Pila = Pila()
    lista_aux: list = []

    # vacio los elementos de p en lista_aux
    while not p.empty():
       lista_aux.insert(0, p.get())

    # lleno p y p_copia con los elementos de lista_aux
    for elem in lista_aux:
        p.put(elem)
        p_copia.put(elem)

    return p_copia


# ej 3

def maximo(p: Pila[int]) -> int: 
    p_copia: Pila = copiar_pila(p)
    max: int = p_copia.get()

    while not p_copia.empty():
        tope: int = p_copia.get()

        if tope > max:
            max = tope

    return max

# ej 4

Nota = int
Nombre = str
Alumno_Nota = tuple[Nombre, Nota]

def nota(t:Alumno_Nota) -> Nota:
    return t[1]

def buscar_nota_maxima(p: Pila[Alumno_Nota]) -> Alumno_Nota:
    p_copia: Pila = copiar_pila(p)
    
    alumno_nota_max: Alumno_Nota = p_copia.get()
    nota_maxima: Nota = nota(alumno_nota_max)

    while not p_copia.empty():
        alumno_nota_tope: Alumno_Nota = p_copia.get()
        nota_tope: Nota = nota(alumno_nota_tope)
        if nota_tope > nota_maxima:
            nota_maxima = nota_tope
            alumno_nota_max = alumno_nota_tope

    return alumno_nota_max


# ej 6 (notacion polaca invera)

"""
es una forma de escribir expresiones matemáticas en la que los operadores siguen
a sus operandos.
Por ejemplo, la expresión “3 + 4” se escribe como “3 4 +”
"""
OperadorBinario = str
type Token = float| OperadorBinario

def tokenizar(s:str) -> list[str]:

    lista_tokens_str: list[str] = []
    token_str:str = ''

    # 1 separacion por espacio

    for caracter in s:
        # si no hay espacio se sigue concatenando caracteres
        if caracter != ' ':
            token_str += caracter

        # si hay espacio, se agrega el token actual y se resetea token
        else:
            lista_tokens_str.append(token_str)
            token_str = '' 

    # si el texto no termina con espacio, se captura el ultimo token
    if token_str != '':
        lista_tokens_str.append(token_str)

    # 2 conversion de numeros a float

    operadores_binarios: list[OperadorBinario] = ['+', '-', '*', '/']
    lista_tokens: list[Token] = []

    for token_str in lista_tokens_str:

        # si el token es un operador, queda igual
        if token_str in operadores_binarios:
            lista_tokens.append(token_str)

        # sino, es un operando, y se transforma a float
        else: 
            lista_tokens.append(float(token_str)) 

    return lista_tokens

def operacion(operando1: float, operando2: float, operador: OperadorBinario) -> float:
    res: float = 0.0

    if operador == '+':
        res = operando1 + operando2
    elif operador == '-':
        res = operando1 - operando2 
    elif operador == '*':
        res = operando1 * operando2
    else: # operador == '/'
        res = operando1 / operando2

    return res

def evaluar_expresiones(s:str) -> float:
    tokens: list[Token] = tokenizar(s)
    operadores_binarios: list[OperadorBinario] = ['+', '-', '*', '/']
    pila_operandos: Pila[float] = Pila()

    for token in tokens:

        # si el token es operando (no es operador), se agrega a pila_operandos
        if not token in operadores_binarios:
            pila_operandos.put(token)

        # si es un operador, saco dos elementos de la pila, realizo la operacion
        # y meto en la pila_operandos el resultado.
        # Se extrae primero operando2 : el orden importa en resta 
        else: 
            operando_2: float = pila_operandos.get()
            operando_1: float = pila_operandos.get()
            res_operacion: float = operacion(operando_1, operando_2, token) 
            pila_operandos.put(res_operacion)

    # el resultado es finalmente, el único elemento que queda en la pila
    res: float = pila_operandos.get()
    return res


# ej 7

def intercalar_pilas(p1: Pila, p2: Pila) -> Pila:

    p1_copia: Pila = copiar_pila(p1)
    p2_copia: Pila = copiar_pila(p2)

    # defino una pila_aux, donde almaceno intercaladamente los elementos
    pila_aux: Pila = Pila()

    while not p1_copia.empty():
        pila_aux.put(p2_copia.get())
        pila_aux.put(p1_copia.get())

    # saco los elementos de la pila_aux y los pongo en p_res
    p_res: Pila = Pila()

    while not pila_aux.empty():
        p_res.put(pila_aux.get())

    # el pasaje por una cola auxiliar, garantiza el orden requerido en p_res
    return p_res


#### COLAS

def mostrar_cola(cola: Cola) -> None:

    lista_aux: list = []

    # guardo, en orden, los elementos de cola en lista_aux
    while not cola.empty():
        elem = cola.get()
        print(elem)
        lista_aux.append(elem)

    # restauro, en orden, la cola
    for elem in lista_aux:
        cola.put(elem)

def copiar_cola(cola: Cola) -> Cola:
    
    lista_aux: list = []
    cola_copia: Cola = Cola()

    # guardo en orden, los elementos de cola en lista_aux
    while not cola.empty():
        lista_aux.append(cola.get())

    # restauro, en orden, los elementos en cola y cola_copia
    for elem in lista_aux:
        cola.put(elem)
        cola_copia.put(elem)

    return cola_copia

# ej 12

def intercalar(Cola1: Cola, Cola2: Cola) -> Cola:

    # se copian colas, para trabajar con las copias
    Cola1_copia: Cola = copiar_cola(Cola1)
    Cola2_copia: Cola = copiar_cola(Cola2)
    Cola_res: Cola = Cola()

    while not Cola1_copia.empty():
        Cola_res.put(Cola1_copia.get())
        Cola_res.put(Cola2_copia.get())
        
    return Cola_res


# ej 15 atencion a clientes

NombreCliente = str
DNI = int
EsPreferencial = bool
TienePrioridad = bool
Cliente = tuple[NombreCliente, DNI, EsPreferencial, TienePrioridad]

def es_prioritario(cliente: Cliente) -> bool:
    return cliente[2]

def es_preferencial(cliente: Cliente) -> bool:
    return cliente[3]

def atencion_a_clientes(c : Cola[Cliente]) -> Cola[Cliente]:
    c_copia: Cola[Cliente] = copiar_cola(c)
    c_prioritarios: Cola[Cliente] = Cola()
    c_preferenciales: Cola[Cliente] = Cola()
    c_restantes: Cola[Cliente] = Cola()

    while not c_copia.empty():
        cliente: Cliente = c_copia.get()

        # Se evalua que tipo de cliente es, y se pone en su cola:
        if es_prioritario(cliente):
            c_prioritarios.put(cliente)

        elif es_preferencial(cliente):
            c_preferenciales.put(cliente)

        else:
            c_restantes.put(cliente)

    c_ordenada: Cola[Cliente] = Cola()

    # se llena la cola ordenada, llenando en el orden correspondiente:

    # primero los prioritarios 
    while not c_prioritarios.empty():
        cliente_prioritario: Cliente = c_prioritarios.get()
        c_ordenada.put(cliente_prioritario)

    # luego los preferenciales
    while not c_preferenciales.empty():
        cliente_preferencial: Cliente = c_preferenciales.get()
        c_ordenada.put(cliente_preferencial)      

    # finalmente los restantes
    while not c_restantes.empty():
        cliente: Cliente = c_restantes.get()
        c_ordenada.put(cliente)  

    return c_ordenada

#### DICCIONARIOS

# ej 16
Calificacion = float
type Nota = tuple[Nombre, Calificacion]

def alumno(nota: Nota) -> Nombre: 
    return nota[0]

def calificacion(nota: Nota) -> Calificacion:
    return nota[1]

def notas_por_alumno(notas: list[Nota]) -> dict[Nombre, list[Calificacion]]:
    # agrupa las notas por estudiante, en una lista
    dict_notas: dict[Nombre, list[Calificacion]] = {}

    for nota in notas:
        alumno_nota: Nombre = alumno(nota)
        calificacion_nota: Calificacion = calificacion(nota)

        if not (alumno_nota in dict_notas):
            dict_notas[alumno_nota] = [calificacion_nota]
        else:
            dict_notas[alumno_nota].append(calificacion_nota)

    return dict_notas

def promedio(notas: list[Nota]) -> Nota:
    N: int = len(notas)
    suma: float = 0
    for nota in notas:
        suma += nota
    return suma/N

def calcular_promedio_por_estudiante(notas: list[Nota]) -> dict[Nombre, Calificacion]:
    # transformo las notas, de una lista a un diccionario, agrupando por alumno
    dict_notas: dict[Nombre, list[Calificacion]] = notas_por_alumno(notas)

    dict_promedios: dict = {}

    for alumno in dict_notas:
        notas_alumno: list[Nota] = dict_notas[alumno]
        promedio_alumno: float = promedio(notas_alumno)
        dict_promedios[alumno] = promedio_alumno

    return dict_promedios

# ej 18: sistema de gestión de inventario

Precio = float
Cantidad = int
Atributos = dict[str, Precio | Cantidad]

Producto = str
Inventario = dict[Producto, Atributos]

# 18.1
def agregar_producto(inventario: Inventario, 
                     nombre_prod: Producto, 
                     precio: Precio, 
                     cant: Cantidad)-> None:
    
    atributos_prod: Atributos = {
        'precio': precio,
        'cantidad': cant
    }

    inventario[nombre_prod] = atributos_prod


# 18.2
def actualizar_stock(inventario: Inventario,
                     nombre_prod: Producto,
                     cant_nueva: Cantidad)-> None:

    atributos_prod: Atributos = inventario[nombre_prod]
    atributos_prod['cantidad'] = cant_nueva


# 18.3
def actualizar_precio(inventario: Inventario,
                      nombre_prod: Producto,
                      precio_nuevo: Precio)-> None:

    atributos_prod: Atributos = inventario[nombre_prod]
    atributos_prod['precio'] = precio_nuevo


#18.4

def calcular_valor_producto(atributos_prod: Atributos) -> float:  
    return atributos_prod['cantidad'] * atributos_prod['precio'] 

def calcular_valor_inventario(inventario: Inventario) -> float:

    valor_inventario: float = 0.0

    # se usa .values() para iterar directamente sobre los dict internos
    for atributos_prod in inventario.values(): 
        valor_inventario += calcular_valor_producto(atributos_prod)

    return valor_inventario


#### ARCHIVOS


def contar_lineas(nombre_archivo: str) -> int:
    archivo: TextIO = open(nombre_archivo)
    lineas: list[str] = archivo.readlines()
    cant_lineas: int = len(lineas)
    archivo.close()

    return cant_lineas


def existe_palabra(nombre_archivo: str, palabra: str) -> bool:
    res: bool = False
    archivo: TextIO = open(nombre_archivo)
    lineas: list[str] = archivo.readlines()

    for linea in lineas: 
        if palabra in linea: 
            res = True

    archivo.close()

    return res


def cantidad_de_apariciones(nombre_archivo: str, palabra: str) -> int:
    cant_apariciones: int = 0
    archivo: TextIO = open(nombre_archivo)
    lineas: list[str] = archivo.readlines()

    for linea in lineas:
        cant_apariciones_en_linea: int = linea.count(palabra)
        cant_apariciones += cant_apariciones_en_linea

    archivo.close()

    return cant_apariciones
