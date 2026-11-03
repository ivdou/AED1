from typing import TypeVar
from queue import LifoQueue as Pila
from queue import Queue as Cola
import random


T = TypeVar('T')


def sucesor (y:int) -> int :
    y = y + 1
    return y

def sumar_uno (li:list[int]) -> None :
    for i in range (len(li)):
        li[i] = li[i] + 1
		
y:int = 10
res:int = sucesor (y)
print (res)
print (y)

mi_lista:list[int] = [2,6,7]
sumar_uno (mi_lista)
print (mi_lista)


def probar():
    mi_lista = ['a', 'b', 'c']
    otra_referencia_a_s:list[str] = mi_lista
    otra_referencia_a_s[0] = 'z'
    print(mi_lista)

    copia_de_s:list[str] = mi_lista.copy()
    copia_de_s[1] = 'x'
    print(mi_lista)

probar()

T = TypeVar('T')

def mostrar(p:Pila[T] ):
    pila_tmp = Pila()
    while not (p.empty()):
        e:T = p.get()
        print(e)
        pila_tmp.put (e)

    #restauro
    while not (pila_tmp.empty()):
        e:T = pila_tmp.get()
        p.put (e)


#8 implementar una funcion `generarNrosAlAzar(in n: int, in desde: int, in hasta: int) -> list[int]` 
# que genere una lista de n numeros enteros al azar en el rango [desde, hasta]. 
# Pueden user la funcion `random.randint()`

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    res:Pila[int] = Pila()
    for _ in range(cantidad):
        x = random.randint(desde, hasta)
        res.put(x)
    return res

mostrar (generar_nros_al_azar(5,7,1000))


def pila_desde_lista(li:list[T] ) -> Pila[T] :
    res:Pila[T] = Pila()

    for e in li:
        res.put (e)

    return res
