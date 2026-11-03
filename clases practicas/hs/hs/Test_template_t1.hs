import Test.HUnit
import Template_t1

main = runTestTT tests

tests = test [
    -- "nombre" ~: (funcion parametros) ~?= resultado_esperado
    "Ej 1 - cantDivisores " ~: cantDivisores 1 ~?= 1,
    "Ej 1 - cantDivisores2 " ~: cantDivisores 7 ~?= 2,
    "Ej 1 - cantDivisores3 " ~: cantDivisores 8 ~?= 4,

    "Ej 1 - mayorNumeroConNDivisores" ~: mayorNumeroConNDivisores 2 5 3 ~?= 4,
    "Ej 1 - mayorNumeroConNDivisores2" ~: mayorNumeroConNDivisores 2 5 2 ~?= 5
    ]
