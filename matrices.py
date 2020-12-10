# lista = ["a", "strings", "manzanas"]
matriz = [[1, 2, 1,], [2, 3, 5], [1, 4, 5]]

suma = 0
for x in range(0, len(matriz)):
    for y in range(0, len(matriz[x])):
        suma +=matriz[x][y]


print("La suma total de todos los numeros es: ", suma)
