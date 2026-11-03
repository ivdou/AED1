from queue import LifoQueue as Pila
from queue import Queue as Cola
import random

def mostrar_cola(c):
    long = 0
    while not c.empty():
        print(c.get())
        long += 1
    print("Long es ", long)

def maximo(p: Pila[int]) -> int: 
    
    max : int = p.get()
    p_aux = Pila()
    p_aux.put(max)
    while not p.empty():
        elem = p.get()
        p_aux.put(elem)
        if elem > max: 
            max = elem
    
    while not p_aux.empty():
        p.put(p_aux.get())
    
    return max

def armar_secuencia_de_bingo() -> Cola[int]: 
    # Genero lista [0...99]
    l: list[int] = list(range(0, 100))
    # shuffl
    random.shuffle(l) 
    # meto en una cola 
    res : Cola[int] = armar_cola_desde_lista(l)
    return res 

def armar_cola_desde_lista(l : list[int])-> Cola[int]: 
    # l = [1, 2, 3] -> Cola(1, 2, 3)
    res : Cola[int] = Cola()
    for e in l: 
        res.put(e)
    return res 

def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int: 
    
    carton_nros_sin_salir = carton.copy()
    cant_bolillas_jugadas = 0 
    cola_aux = Cola()

    while len(carton_nros_sin_salir) > 0: 
        bolilla_jugada = bolillero.get()
        if pertenece(bolilla_jugada, carton_nros_sin_salir): 
            carton_nros_sin_salir = sacar(bolilla_jugada, carton_nros_sin_salir)
        cant_bolillas_jugadas += 1 
        cola_aux.put(bolilla_jugada)
    
    # rearmar la cola 
    while not bolillero.empty():
        cola_aux.put(bolillero.get())
    
    while not cola_aux.empty():
        bolillero.put(cola_aux.get())
    
    return cant_bolillas_jugadas

def pertenece(e, l): 
    res = False 
    #TODO: reescribir con while
    for elem in l: 
        if elem == e: 
            res = True
    return res 

def sacar(e, l): 
    #Requiere: e esta en l solo una vez 
    lista_sin_e = list()
    for elem in l:
        if elem != e: 
            lista_sin_e.append(elem)
    return lista_sin_e





