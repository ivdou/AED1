import Test.HUnit
import C7HUnit
--import C7HUnit (indiceMax)

run = runTestTT tests9

tests9 = test [
    "Caso base 1" ~: ( fib 0 ) ~?= 0 ,
    "Caso base 2" ~: ( fib 1 ) ~?= 1 ,
    "Caso recursivo" ~: ( fib 2) ~?= 1,
    
    "xxx" ~: ( expectPermutacion (pares [1,2,3]) [2])  ,
    "xxx" ~: ( expectPermutacion (pares [1,2, 3,2]) [2,2]) ,
    "xxx" ~: ( expectPermutacion (pares [4,2, 3,2]) [2,4,2]),
    "MuchosMaximos" ~: ( expectAny (indiceMax [ 2 , 4 , 4 , 1 ])  [1,2]),
    "comparacionReales" ~:  assertBool "Cercano a 1" ( aproximado funcionQueDevuelveCasi1  1 ) ]



--Funciones auxiliares útiles para testear

-- expectAny permite saber si el elemento que devuelve la función es alguno de los esperados.
-- útil para cuando hay más de una respuesta correcta. Por ejemplo, devolver el elemento que más veces está repetido en una lista
-- "repetido" ~: expectAny (masRepetido [1,1,2,2,3]) [1,2], en este caso, es correcto devolver 1 o 2

-- expectAny (actual: a, expected: [a]): Test
-- asegura: res es un Test Verdadero si y sólo si actual pertenece a la lista expected
expectAny :: (Foldable t, Eq a, Show a, Show (t a)) => a -> t a -> Test
expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)



incluido :: (Eq t) => [t] -> [t] -> Bool
incluido [] l = True
incluido (x:c) l = elem x l && incluido c  l


-- expectPermutacion es útil cuando la función devuelve una lista sin importar el orden, con lo cual puede haber más de una respuesta correcta
-- Las lista [1,2] y [2,1] si las comparamos con "==" son distintas, pero para algunos problemas las podemos considerar ambas como 
-- respuestas correctas. Por ejemplo, una función que mezcla todos los elementos de una lista, tiene varias respuestas correctas.
-- " comentario " ~: (expectPermutacion(mezclar ["u1", "u2","u3","u4"] ) ["u1", "u2","u3","u4"]),

-- expectPermutacion (actual: [T], expected[T]) : Test
-- asegura: res es un Test Verdadero si y sólo si:
--            para todo elemento e de tipo T, #Apariciones(actual, e) = #Apariciones(expected, e)

expectPermutacion :: (Ord a, Show a) => [a] -> [a] -> Test
expectPermutacion actual expected = incluido actual expected 
                    && incluido expected actual ~? ("expected list: " ++ show expected ++ "\nbut got: " ++ show actual)

quitar :: (Eq t) => t -> [t] -> [t]
quitar e [] = []
quitar e (x:s) | e == x = s
               | otherwise = x:(quitar e s)

margenFloat = 0.00001
aproximado :: Float -> Float -> Bool
aproximado x y = abs (x - y) < margenFloat