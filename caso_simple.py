lista = [1, 2, 3]
suma = 0
for x in lista:
    suma += x

print("La suma total de numeros es: ", suma)

lista = [[1, 2, 3], [4, 5, 6]]
for x in lista:
    print(x)
    for y in x:
        print(y)