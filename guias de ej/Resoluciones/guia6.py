import math 


## ej 1

# 1.1
def imprimir_hola_mundo () :
	print("¡Hola mundo!") 

# 1.2


# 1.3
def raizDe2() -> float : 
    x : float = math.sqrt(2)
    return round(x,4)

# 1.4

# 1.5
def perimetro() -> float :
    pi : float = math.pi
    return  2 * pi 


## ej 2


# 2.1
def imprimir_saludo(nombre: str) -> str:
    return f"Hola {nombre}"

# 2.2
def raiz_cuadrada_de(numero: float) -> float:
    return math.sqrt(numero)

# 2.3
def farenheit_a_celsius(temp_far: float) -> float:
    F = temp_far
    C = (F - 32) * 5/9
    return C

# 2.4

# 2.5
def es_multiplo_de (n:int ,m:int) -> bool:
    return n % m == 0 

# 2.6
def es_par (numero: int) -> bool:
    return es_multiplo_de(numero, 2) 

# 2.7
def cantidad_de_pizzas(comensales: int, min_cant_porciones: int) -> int:
    c = comensales
    m = min_cant_porciones
    porciones = c * m 
    pizzas = math.ceil (porciones / 8)

    return pizzas 


## ej 3


# 3.1
def alguno_es_0 (numero1:float, numero2:float) -> bool:
    return (numero1 == 0) or (numero2 == 0)

# 3.2
def ambos_son_0 (numero1:float, numero2:float) -> bool:
    return (numero1 == 0) and (numero2 == 0)

# 3.3
def es_nombre_largo (nombre:str) -> bool: 
    L = len(nombre)
    return (L >= 3) and (L <= 8)

# 3.4
def es_bisiesto (año: int) -> bool:
    if es_multiplo_de (año, 400):
        return True
    elif es_multiplo_de (año, 100):
        return False
    elif es_multiplo_de (año, 4):
        return True
    else :
        return False


## ej 4


# 4.1
def peso_pino(altura: float) -> float:
    if altura <= 300 :
        peso = altura * 3.0 
        return peso
    else :
        excedente = altura - 300
        peso_300 = 300 * 3.0
        peso = peso_300 + excedente * 2.0
        return peso

# 4.2
def es_peso_util (peso: int) -> bool: 
    return (peso >= 400) and (peso <= 100)

# 4.3
def sirve_pino (altura: int) -> bool: 
    peso = peso_pino (altura)
    return es_peso_util (peso)

# 4.4
def sirve_pino2 (altura: int) -> bool: 
    return es_peso_util (peso_pino (altura))


## ej 5 

# 5.1
def doble_si_es_par(numero: int) -> int: 
    if es_par(numero):                      # es_par() implementada en ej 2.6
        return numero * 2 
    else:
        return numero 


## ej 6


# 6.2
def imprimir_pares_entre_10_y_40 () -> None: 
    i = 10
    while i <= 40:
        print(i)
        i = i + 2 

# 6.4
def cuenta_regresiva_desde (numero: int) -> None:
    i = numero 
    while i >= 1:
        print(i)
        i = i - 1
    print('Despegue')