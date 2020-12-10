# Funciones, clase 4
lista = ["manzanas", "peras", "frutillas", "arandanos"]
nueva_lista = ["destornillador", "tuercas", "clavos"]
buscar = input("Ingrese un valor a buscar: ")

def buscar_lista(lista, elemento):
    existe = False
    for x in lista:
        if x == buscar:
            existe = True

    return existe 
resultado1 = buscar_lista(lista, buscar)
resultado2 = buscar_lista(nueva_lista, buscar)
if resultado1 or resultado2:
        print("El valor existe")
    else: 
        print("El valor no existe")






