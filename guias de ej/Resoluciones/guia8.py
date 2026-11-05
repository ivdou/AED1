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

# print('Estado inicial de p_test')
# mostrar_pila(p_test)

# p_test_copia: Pila = copiar_pila(p_test)

# print('Resultado de la copia en de p_test_copia')
# mostrar_pila(p_test_copia)

# print('Estado de p_test, luego de ser copiada')
# mostrar_pila(p_test)

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

type Nota = int
type Nombre = str
type Alumno_Nota = tuple[Nombre, Nota]

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

# armo p_test como 2,7,4,1|

p_test: Pila[Alumno_Nota] = Pila()
p_test.put(('Juan', 8))
p_test.put(('Pedro', 10))
p_test.put(('Maria', 7))
p_test.put(('Theo', 5))


print('Estado inicial p_test:')
mostrar_pila(p_test)

print('Ejecucion de buscar_nota_maxima(), resulta en:')
res: Alumno_Nota = buscar_nota_maxima(p_test)
print(res)

print('Estado de p_test, luego de ejecución')
mostrar_pila(p_test)
