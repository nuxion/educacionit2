# lista    0            1         2           3
lista = ["manzanas", "peras", "frutillas", "arandanos"]

contador = 1
invertido = []
while contador <= len(lista):
    invertido.append(lista[len(lista) - contador])
    contador += 1

print("Original: ", lista)
print("Invertido: ", invertido)