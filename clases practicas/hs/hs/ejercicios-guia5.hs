-- Ejercicio 2.5
quitar :: Int -> [Int] -> [Int]
quitar _ [] = []
quitar elem (x:xs) | elem == x = xs
                   | otherwise = x: quitar elem xs


-- Ejercicio 3.3
maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:xs) | x > y = maximo (x:xs)
                | otherwise = maximo (y:xs)

-- Ejercicio 3.9
ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar xs = (ordenar (quitar max xs)) ++ [max]
            where max = maximo xs

-- Ejercicio 6
type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ [] = False
enLosContactos nombre ((contactoNombre, _):contactos) = nombre == contactoNombre || enLosContactos nombre contactos

agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto c [] = [c]
agregarContacto (nombre, nuevoTel) ((contactoNombre, contactoTel):contactos) | contactoNombre == nombre = (nombre, nuevoTel):contactos
                                                                             | otherwise = (contactoNombre, contactoTel):(agregarContacto (nombre, nuevoTel) contactos)
-- Ejercicio 8
multiplicarFilas :: [[Integer]] -> [Integer]
multiplicarFilas [] = []
multiplicarFilas (x:xs) = (multiplicarFila x) : multiplicarFilas xs

multiplicarFila :: [Integer] -> Integer
multiplicarFila [x] = x
multiplicarFila (x:xs) = x * multiplicarFila xs 

cantidadDeApariciones :: Integer -> [[Integer]] -> Integer 
cantidadDeApariciones e [] = 0
cantidadDeApariciones e (x:xs) = cantidadDeAparicionesEnFila e x + cantidadDeApariciones e xs

cantidadDeAparicionesEnFila :: Integer -> [Integer] -> Integer
cantidadDeAparicionesEnFila e [] = 0
cantidadDeAparicionesEnFila e (x:xs)
    | x == e = 1 + cantidadDeAparicionesEnFila e xs
    | otherwise = cantidadDeAparicionesEnFila e xs
