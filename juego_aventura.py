nombre = input("Hola como te llamas?")
print("Bienvenido ", nombre)


print("Estas en una habitacion encerrado, que elegis hacer: ")
print("1) Revisar bajo la cama, 2) Revisar el tocador 3) golpear fuerte la puerte")
eleccion = input()
if eleccion == '1':
    print("Mala suerte no hay nada...")
elif eleccion == '2':
    print("Que suerte encontraste la llave")
elif eleccion == '3':
    print("El carcelero te escucho y te va castigar")