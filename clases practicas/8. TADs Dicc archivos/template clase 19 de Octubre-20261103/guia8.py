from queue import LifoQueue as Pila
from queue import Queue as Cola
import random
from typing import TypeVar
 
T = TypeVar('T')

# Ejercicio 1.1
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]: 
    pass

#auxiliares de pila
def pila_desde_lista (lista: list[T]) -> Pila[T]:
    pass

def mostrar_pila (p: Pila[T]) -> None:
    pass

 
# Ejercicio 1.3
def buscar_el_maximo(p: Pila[int]) -> int:
    pass
    
# Ejercicio 2.13.1
def armarSecuencideBingo() -> Cola[int]:
    pass
# Ejercicio 2.13.2
def pertenece (cadena: list[T], elem:T) -> bool:
    pass
    
def jugarCartonDeBingo(carton: list[int], bolillero: Cola[int]) -> int:
    pass

#auxiliares de cola
def cola_desde_lista (lista: list[T]) -> Cola[T]:
    pass

def mostrar_cola (c: Cola[T]) -> None:
    pass
