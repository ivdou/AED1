import ejercicios

def print_begin_test(test_number, test_name):
    print("Corriendo test {} {}".format(test_number, test_name))

def print_end_test(test_number, test_name):
    print("Finalizado test {} {}".format(test_number, test_name))

def es_aproximado(calc, orig):
    precision:float = 0.01
    abs_err:float = abs(calc - orig)
    if calc == 0 or orig == 0:
        return abs_err < precision
    else:
        return abs_err / abs(calc) < precision


def asegurar(estimated, expected):
    return estimated == expected


def test01_esta_ordenado():
    test_number:int = 1
    test_name:str = "esta_ordenado"

    print_begin_test(test_number, test_name)

    ordered_desc:list[int] = [123, 3, 0, -1, -123]
    ordered_asc:list[int] = [-501, 0, 12, 456, 501, 99999]
    empty:list[int] = []
    unordered:list[int] = [-1, 0, 1, -1, 56, 98, 10]
    one_only:list[int] = [23]
    two_only:list[int] = [1, 2]
    two_peaks:list[int] = [0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1]
    equal:list[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    res: bool = asegurar(ejercicios.esta_ordenado(ordered_desc), True)
    res &= asegurar(ejercicios.esta_ordenado(ordered_asc), True)
    res &= asegurar(ejercicios.esta_ordenado(empty), True)
    res &= asegurar(ejercicios.esta_ordenado(unordered), False)
    res &= asegurar(ejercicios.esta_ordenado(one_only), True)
    res &= asegurar(ejercicios.esta_ordenado(two_only), True)
    res &= asegurar(ejercicios.esta_ordenado(two_peaks), False)
    res &= asegurar(ejercicios.esta_ordenado(equal), True)

    print_end_test(test_number, test_name)
    return res

def test02_es_primo():
    test_number:int = 2
    test_name:str = "es_primo"

    print_begin_test(test_number, test_name)

    res: bool = asegurar(ejercicios.es_primo(0), False)
    res &= asegurar(ejercicios.es_primo(1), False)
    res &= asegurar(ejercicios.es_primo(2), True)
    res &= asegurar(ejercicios.es_primo(3), True)
    res &= asegurar(ejercicios.es_primo(5), True)
    res &= asegurar(ejercicios.es_primo(17), True)
    res &= asegurar(ejercicios.es_primo(-2), False)
    res &= asegurar(ejercicios.es_primo(919), True)
    res &= asegurar(ejercicios.es_primo(643), True)
    res &= asegurar(ejercicios.es_primo(-643), False)
    res &= asegurar(ejercicios.es_primo(100), False)

    print_end_test(test_number, test_name)
    return res

def test03_pertenece():
    test_number:int = 3
    test_name:str = "pertenece"
    print_begin_test(test_number, test_name)

    enteros:list[int] = [5, -323, 253, 0, -7, 100]
    vacio:list[int] = []
    todos_iguales:list[int] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    res =  asegurar(ejercicios.pertenece(0, enteros), True)
    res &= asegurar(ejercicios.pertenece(7, enteros), False)
    res &= asegurar(ejercicios.pertenece(100, enteros), True)
    res &= asegurar(ejercicios.pertenece(-323, enteros), True)
    res &= asegurar(ejercicios.pertenece(1, vacio), False)
    res &= asegurar(ejercicios.pertenece(1, todos_iguales), True)
    res &= asegurar(ejercicios.pertenece(4, todos_iguales), False)

    print_end_test(test_number, test_name)
    return res


def test04_desvio_estandar():
    test_number:int = 4
    test_name:str = "desvio_estandar"
    print_begin_test(test_number, test_name)

    notas:list[float] = [20, 15, 26, 32, 18, 28, 35, 14, 26, 22, 17]
    norm:list[float] = [-0.5, 0.98, 1.2, -1.0, -0.345, 0.478, 1.230]
    todos_cero:list[float] = [0, 0, 0, 0, 0]
    otra_data:list[float] = [9.87, 9.60, 9.56, 8.01, 7.99, 9.87, 7.67, 9.14]

    res =  es_aproximado(ejercicios.desvio_estandar(notas), 6.6332)
    res &= es_aproximado(ejercicios.desvio_estandar(norm), 0.83790)
    res &= es_aproximado(ejercicios.desvio_estandar(todos_cero), 0)
    res &= es_aproximado(ejercicios.desvio_estandar(otra_data), 0.86354)

    print_end_test(test_number, test_name)
    return res


def test05_maximo_comun_divisor():
    test_number:int = 5
    test_name:str = "maximo_comun_divisor"
    print_begin_test(test_number, test_name)

    res:bool = asegurar(ejercicios.maximo_comun_divisor(1, 1), 1)
    res &= asegurar(ejercicios.maximo_comun_divisor(1, 2), 1)
    res &= asegurar(ejercicios.maximo_comun_divisor(6, 2), 2)
    res &= asegurar(ejercicios.maximo_comun_divisor(17, 19), 1)
    res &= asegurar(ejercicios.maximo_comun_divisor(100, 0), 100)
    res &= asegurar(ejercicios.maximo_comun_divisor(100, 10), 10)
    res &= asegurar(ejercicios.maximo_comun_divisor(28, 56), 28)
    res &= asegurar(ejercicios.maximo_comun_divisor(6, 10), 2)
    res &= asegurar(ejercicios.maximo_comun_divisor(-6, 10), 2)
    res &= asegurar(ejercicios.maximo_comun_divisor(10, -6), 2)
    res &= asegurar(ejercicios.maximo_comun_divisor(0, 1), 1)

    print_end_test(test_number, test_name)
    return res


def test06_suma_doble():
    test_number:int = 6
    test_name:str = "suma_doble"
    print_begin_test(test_number, test_name)

    impares:list[int] = [1, 3, 5, 7, 9, 11, 23, 33, 99, 101]
    pares:list[int] = [2, 4, 6, 8, 10, 50, 990]
    mezcla:list[int] = [-1, 0, 500, 22, -2, 35, 16, -10, 12, 66, 76, -2]
    vacio:list[int] = []
    paresNeg:list[int] = [-2, 1, 1, 1, -2, 2, 1, -2, -2, 1]

    res: bool = asegurar(ejercicios.suma_doble(impares), 0)
    res &= asegurar(ejercicios.suma_doble(pares), 2140)
    res &= asegurar(ejercicios.suma_doble(mezcla), 1384)
    res &= asegurar(ejercicios.suma_doble(vacio), 0)
    res &= asegurar(ejercicios.suma_doble(paresNeg), 4)
    print_end_test(test_number, test_name)
    return res




def test07_valor_medio():
    test_number:int = 7
    test_name:str = "valorMedio"
    print_begin_test(test_number, test_name)

    res: bool = True
    res &= es_aproximado(ejercicios.valor_medio(), 0.4948)

    print_end_test(test_number, test_name)
    return res


def test08_contar_palabras():
    testNumber:int = 8
    testName:str = "cantPalabras"
    print_begin_test(testNumber, testName)

    res:bool = True
    res &= asegurar(ejercicios.cant_palabras("datos/loremIpsum.txt"), 98);
    res &= asegurar(ejercicios.cant_palabras("datos/losprofetas.txt"), 64);

    print_end_test(testNumber, testName)
    return res