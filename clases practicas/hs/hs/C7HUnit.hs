module C7HUnit where


fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib ( n-1) + fib ( n-2)












--devolver una lista que solo contenga todos los 
--elementos pares que están en la lista recibida. 
--Incluir repetidos. No importa el orden
pares :: [Int] -> [Int]
pares [] = []
pares (x:xs)    | esPar x = x:pares xs
                | otherwise = pares xs

esPar:: Int  -> Bool
esPar x = mod x 2 == 0


eliminar :: (Eq t) => t -> [t] -> [t]
eliminar e [] = []
eliminar e (x:s) | e == x = s
               | otherwise = x:(eliminar e s)                


--precondición la lista de entradas no debe ser vacía
indiceMax :: [Int] -> Int
indiceMax xs = findMax xs 0 0 (head xs)

findMax :: [Int] -> Int -> Int -> Int -> Int
findMax [] _ maxIdx _ = maxIdx
findMax (y:ys) idx maxIdx maxVal
  | y > maxVal = findMax ys (idx + 1) idx y   -- Nuevo máximo encontrado
  | otherwise  = findMax ys (idx + 1) maxIdx maxVal  -- Continuar sin cambios


funcionQueDevuelveCasi1 :: Float
funcionQueDevuelveCasi1 = 0.9999999