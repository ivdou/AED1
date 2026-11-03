import cases

def main():
    successes = 0
    total = 8

    print("=====Test 01=====")
    successes += cases.test01_esta_ordenado()
    print("Exitos acumulados:", successes)

    print("\n=====Test 02=====")
    successes += cases.test02_es_primo()
    print("Exitos acumulados:", successes)

    print("\n=====Test 03=====")
    successes += cases.test03_pertenece()
    print("\nExitos acumulados:", successes)

    print("=====Test 04=====")
    successes += cases.test04_desvio_estandar()
    print("\nExitos acumulados:", successes)

    print("\n=====Test 05=====")
    successes += cases.test05_maximo_comun_divisor()
    print("Exitos acumulados:", successes)

    print("\n=====Test 06=====")
    successes += cases.test06_suma_doble()
    print("Exitos acumulados:", successes)

    print("\n=====Test 07=====")
    successes += cases.test07_valor_medio()
    print("Exitos acumulados:", successes)

    print("\n=====Test 08=====")
    successes += cases.test08_contar_palabras()
    print("Exitos acumulados:", successes)

    print("\n# Ejercicios correctos:", successes)
    print("# Ejercicios incorrectos:", total - successes)

if __name__ == "__main__":
    main()
