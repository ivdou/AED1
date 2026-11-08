from queue import LifoQueue as Pila
from queue import Queue as Cola

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

pila1: Pila = Pila()
pila2: Pila = Pila ()
pila1.put(8)
pila2.put(7)
pila1.put(3)
pila2.put(4)
pila1.put(1)
pila2.put(0)

print('pila1:')
mostrar_pila(pila1)
print('')
print('pila2:')
mostrar_pila(pila2)

print('')
print('ejecucion de intercalado...')
pila_intercalada: Pila = intercalar_pilas(pila1, pila2)

print('resultado de intercalado; pila_intercalada:')
mostrar_pila(pila_intercalada)
print('')
print('estado final de pila1 y pila2:')
print('pila1:')
mostrar_pila(pila1)
print('')
print('pila2:')
mostrar_pila(pila2)


# 012378

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


# ej 15

#### DICCIONARIOS

# ej 16

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


