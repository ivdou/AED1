from guia8 import *

notas: list[tuple[str, int]] = [
    ('Ivan', 8.50),
    ('Juan', 7.50),
    ('Maria',6.25),
    ('Ivan', 8.25),
    ('Juan' , 9.00),
    ('Maria', 6.75)
]


print(calcular_promedio_por_estudiante(notas))
