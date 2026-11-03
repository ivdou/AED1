ganadores = [['Messi', 'Cristiano', 'Mbappe'], [44, 35, 16]]

# Accedemos a cada fila (que es una lista)
for fila in ganadores:
    # Accedemos a cada columna dentro de la fila
    for columna in fila:
        print(columna)


# Recorriendo los índices
# i serían las filas
print("++ Con for - i son filas ++")
for i in range(len(ganadores)):
    for j in range(len(ganadores[i])):
        print("ganadores["+str(i)+"]["+str(j)+"] = " + str(ganadores[i][j]))
        #ganadores[i][j] = 0

print("++ Con while y los índices ++")
# Con while y los índices
fila = 0
cant_cols = len(ganadores[fila])
while fila < len(ganadores):
    columna = 0
    while columna < cant_cols:
        print("ganadores["+str(fila)+"]["+str(columna)+"] = " + str(ganadores[fila][columna]))
        columna += 1
    fila += 1
