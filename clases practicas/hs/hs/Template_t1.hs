{--
Yo: Paula 
Certifico que el siguiente archivo fue elaborado únicamente por mí, sin ayuda de otras personas o herramientas.
--}


module Template_t1 where

-- Ejercicio 1
mayorNumeroConNDivisores :: Integer -> Integer -> Integer -> Integer
mayorNumeroConNDivisores d h n | tieneNDivisores n h = h 
                               | otherwise = mayorNumeroConNDivisores d (h-1) n

tieneNDivisores :: Integer -> Integer -> Bool
-- el nro m tiene n divisores  
tieneNDivisores n m = cantDivisores m == n

cantDivisores :: Integer -> Integer
cantDivisores m = cantDivisoresDesde m 1

cantDivisoresDesde :: Integer -> Integer -> Integer
-- requiere d <= m 
-- la voy a llamar con cantDivisoresDesde m 1
cantDivisoresDesde m d | m == d = 1
                       | m `mod` d == 0 = 1 + cantDivisoresDesde m (d+1)
                       | otherwise = cantDivisoresDesde m (d+1)

-- Ejercicio 2
sanguchitoDeCerosMasGrande :: [Integer] -> Integer
sanguchitoDeCerosMasGrande lista = 0

-- Ejercicio 3
agruparPorCantidadDeTemporadas :: [(String, Integer)] -> [(Integer, [String])]
agruparPorCantidadDeTemporadas lista = []

-- Ejercicio 4
reemplazarMinimoDeCadaFila :: [[Integer]] -> Integer -> [[Integer]]
reemplazarMinimoDeCadaFila matriz numero  = []

{--
Siendo la última modificación con la solución final:
COMPLETE FECHA y HORA DE ULTIMA MODIFICACIÓN ACA
--}
