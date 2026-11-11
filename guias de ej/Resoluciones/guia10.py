from guia7 import maximo, minimo

# ej 1

Stock = int
Producto = str
Producto_Stock = tuple[Producto, Stock]


# funcion aux, transforma la lista de tuplas a un dicc con listas
def diccionario_lista_stock(stock_cambios: list[Producto_Stock]) -> dict[Producto, list[Stock]]:
    dict_lista_stock: dict[Producto, list[Stock]] = {}

    for producto_stock in stock_cambios:
        producto: Producto = producto_stock[0]
        stock: Stock = producto_stock[1]

        if not producto in dict_lista_stock:
            dict_lista_stock[producto] = [stock]
        else:
            dict_lista_stock[producto].append(stock)

    return dict_lista_stock

def stock_productos(stock_cambios: list[Producto_Stock]) -> dict[Producto, tuple[Stock, Stock]]:
    # transofrmo a dict con lista de stock
    dict_lista_stock: dict[Producto, list[Stock]] = diccionario_lista_stock(stock_cambios)
    dict_stock: dict[Producto, tuple[Stock, Stock]]= {}

    for producto in dict_lista_stock:
        lista_stock: list[Stock] = dict_lista_stock[producto]
        stock_min: Stock = minimo(lista_stock)  # importada de guia 7
        stock_max: Stock = maximo(lista_stock)  # importada de guia 7
        dict_stock[producto] = (stock_min, stock_max)

    return dict_stock



# ej 4

# columna: dia
# fila rango horario


Responsable = str
Grilla = list[list[Responsable]]


def responsables_dia(grilla_horaria: Grilla, dia: int):
    responsables: list[Responsable] = []
    for responsables_hora in grilla_horaria:
        responsable_del_dia_en_hora: Responsable = responsables_hora[dia]
        responsables.append(responsable_del_dia_en_hora)

    return responsables

def responsables_dia_turno(grilla_horaria: Grilla, dia: int, turno: str) -> list[Responsable]:
    responsables_del_dia: list[Responsable] = responsables_dia(grilla_horaria, dia)
    responsables_turno: list[Responsable] = []

    if turno == 'mañana':
        for i in range(4): 
            responsables_turno.append(responsables_del_dia[i])

    else: 
        for i in range(4, 8):
            responsables_turno.append(responsables_del_dia[i])

    return responsables_turno

def todos_iguales(lista: list[Responsable]) -> bool: 
    res: bool = True
    primer_responsable: Responsable = lista[0]
    
    for responsable in lista:
        if responsable != primer_responsable:
            res = False

    return res

def un_responsable_por_turno (grilla_horaria: Grilla) -> list[tuple[bool, bool]]:
    cant_dias: int = len(grilla_horaria[0])

    # reordeno agrupando por dia
    responsables_por_dia: list[list[Responsable]] = []
    for dia in range(cant_dias): 
        responsables_del_dia: list[Responsable] = responsables_dia(grilla_horaria, dia)
        responsables_por_dia.append(responsables_del_dia)

    res: list[tuple[bool, bool]]= []
    for dia in range(cant_dias):  
        un_responsable_turno_mañana: bool = todos_iguales(responsables_dia_turno(grilla_horaria, dia, 'mañana'))
        
        un_responsable_turno_tarde: bool = todos_iguales(responsables_dia_turno(grilla_horaria, dia, 'noche'))
        
        res_dia: tuple[bool, bool] = (
            un_responsable_turno_mañana,
            un_responsable_turno_tarde
        )

        res.append(res_dia)

    return res


# ej 10 Cola en el banco
from queue import Queue as Cola
Nombre = str
TipoAfiliado = str
Cliente = tuple[Nombre, TipoAfiliado]
from typing import TypeVar

T = TypeVar('T')

def copiar_cola[T](cola: Cola[T]) -> Cola[T]: 

    # Creo una lista auxiliar y una nueva copia
    lista_aux: list[T] = []
    cola_copia: Cola[T] = Cola()

    # Almaceno en orden, los elementos de cola en lista_aux
    while not cola.empty():
        elem: T = cola.get()
        lista_aux.append(elem)

    # Inserto en orden, los elementos de lista_aux en cola y cola_copia
    for elem in lista_aux: 
        cola.put(elem)
        cola_copia.put(elem)

    return cola_copia

def reordenar_priorizando_vips(filaClientes: Cola[Cliente]) -> Cola[Nombre]:

    # Creo una cola copia, y una cola para vips y otra para comunes
    fila_copia: Cola[Cliente] = copiar_cola(filaClientes)
    cola_vips: Cola[Nombre] = Cola()
    cola_comunes: Cola[Nombre] = Cola()

    # lleno las colas de vips y comunes
    while not fila_copia.empty():
        cliente: Cliente = fila_copia.get()
        tipo_afiliado: TipoAfiliado = cliente[1]
        nombre: Nombre = cliente[0]

        if tipo_afiliado == 'vip':
            cola_vips.put(nombre)
        else:
            cola_comunes.put(nombre)

    # Creo una cola_ordenada, donde lleno en el orden requerido los clientes
    cola_ordenada: Cola[Nombre] = Cola()

    # primero los vips
    while not cola_vips.empty():
        cliente_vip: Nombre = cola_vips.get()
        cola_ordenada.put(cliente_vip)

    # luego los comunes
    while not cola_comunes.empty():
        cliente_comun: Nombre = cola_comunes.get()
        cola_ordenada.put(cliente_comun)       

    
    return cola_ordenada

