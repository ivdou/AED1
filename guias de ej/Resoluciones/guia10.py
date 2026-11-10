from guia7 import maximo, minimo

# ej 1

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

