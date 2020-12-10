## Verificar segun lo que ingresa el usuario, si ese valor existe en una lista.

mi_lista = ["manzanas", "peras", "queso", "jamon", "fideos", "fideos"]
palabra = input("Ingrese un a palabra a buscar: ")

# va a venir mi algoritmo 
estado = False
contador = 0
while estado == False and contador < len(mi_lista):
    if mi_lista[contador] == palabra:
        estado = True
    print(mi_lista[contador])
    contador += 1


# Tengo que responder si esta o no esta
if estado:
    print("La palabra existe")
else:
    print("La palabra no existe")