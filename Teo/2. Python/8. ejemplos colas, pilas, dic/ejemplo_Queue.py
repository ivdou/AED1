from queue import Queue as Cola

def contar_pares(c:Cola)->int:
    res:int = 0

    while (not c.empty()):
        elem = c.get()
        if (elem % 2 == 0):
            res += 1

    return res

def contar_pares_rebuild(c:Cola)->int:
    res:int = 0
    colaAux = Cola()

    while (not c.empty()):
        elem = c.get()
        if (elem % 2 == 0):
            res += 1
        colaAux.put(elem)
    
    while (not colaAux.empty()):
        c.put(colaAux.get())

    return res

cola = Cola()

## checking whether cola is empty or not -> true
print(cola.empty())

## pushing the elements
cola.put(1)
cola.put(2)
cola.put(3)
cola.put(4)
cola.put(5)

#llamamos a la función contar_pares pasando la cola construida como parámetro
#El pasaje de parámetro es por referencia!
#print(contar_pares(cola))
#Cuando termina de ejecutar la función... que pasó con el parámetro?
#print(contar_pares_rebuild(cola))


## again checking whether cola is empty or not -> false
print(cola.empty())

## popping all the elements
print(cola.get())
print(cola.get())
print(cola.get())

## checking the cola size
print("Size", cola.qsize())

print(cola.get())
print(cola.get())
 
## checking the whether cola is empty or not for the last time -> true
print(cola.empty())