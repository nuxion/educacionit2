
compras = ["papel cocina", "lavandina", "manzanas", "leche"]

print("Usando un for: ")
for producto in compras:
    print(producto)

print(" ")

print("Usando un while: ")
contador = 0
while contador < len(compras):
    print(compras[contador])
    contador += 1


imprimir = input("Cuantas veces quiere imprimir 'Hola mundo'?")
contador = 0
#while contador < int(imprimir):
#    print(f"Hola mundo, vez {contador}")
#    contador += 1

#for x in range(int(imprimir)):
#    print(f"Hola mundo, vez {x}")

for x in range(5, 10):
    print(x)