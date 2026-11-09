from guia7 import maximo, minimo

# ej 1

"""En la veterinaria, al finalizar cada dia, registra en papeles:
 los nombres 
 la cantidad actual de los productos, cuyo stock ha cambiado.
  

. La funcion debe procesar esta lista y devolver: 
un dict[nombre_producto, tupla[stock_minimo , stock_maximo]]

problema stock productos (in stock cambios : seq⟨str ×Z⟩) : seq⟨Z⟩ {
requiere: {Todos los elementos de stock cambios est ́an formados por un str no vac ́ıo y un entero ≥ 0.}
asegura: {res tiene como claves solo los primeros elementos de las tuplas de stock cambios (o sea, un producto).}
asegura: {res tiene como claves todos los primeros elementos de las tuplas de stock cambios.}
asegura: {El valor en res de un producto es una tupla de cantidades. Su primer elemento es la menor cantidad de ese
producto en stock cambios y como segundo valor el mayor.}
}"""

Stock = int
Producto = str
Producto_Stock = tuple[Producto, Stock]


# funcion aux, transforma la lista de tuplas a un dicc con listas
def diccionario_lista_stock(stock_cambios: list[Producto_Stock]) -> dict[Producto, list[Stock]]:
    dict_lista_stock: dict[Producto, list[Stock]] = {}

    for producto_stock in stock_cambios:
        producto: Producto = producto_stock[0]
        stock: Stock = producto_stock[1]

        if not producto in dict_lista_stock:
            dict_lista_stock[producto] = [stock]
        else:
            dict_lista_stock[producto].append(stock)

    return dict_lista_stock

def stock_productos(stock_cambios: list[Producto_Stock]) -> dict[Producto, tuple[Stock, Stock]]:
    # transofrmo a dict con lista de stock
    dict_lista_stock: dict[Producto, list[Stock]] = diccionario_lista_stock(stock_cambios)
    dict_stock: dict[Producto, tuple[Stock, Stock]]= {}

    for producto in dict_lista_stock:
        lista_stock: list[Stock] = dict_lista_stock[producto]
        stock_min: Stock = minimo(lista_stock)  # importada de guia 7
        stock_max: Stock = maximo(lista_stock)  # importada de guia 7
        dict_stock[producto] = (stock_min, stock_max)

    return dict_stock


lista_input: list[Producto_Stock] = [
    ('Antibiotico',6),
    ('Antiparasitario',12),
    ('Suplemento',8),
    ('Snack',12),
    ('Pretal',6),
    ('Juguete',6),
    ('Antibiotico',3),
    ('Antiparasitario',9),
    ('Snack',10),
    ('Antibiotico',1),
    ('Antiparasitario',7),
    ('Snack',8),
    ('Antibiotico',12),
    ('Antiparasitario',15),
    ('Snack',5),   
    ('Pretal',5),
    ('Juguete',5),
    ('Antibiotico',10),
    ('Antiparasitario',13),
    ('Snack',4), 
    ('Snack',20),
    ('Juguete',10)
]

print(diccionario_lista_stock(lista_input))