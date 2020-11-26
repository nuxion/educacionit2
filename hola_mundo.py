# Distintas maneras de imprimir un hola mundo por pantalla

# 1) la mas simple
print("Hola mundo")

# 2) creo una variable 
mensaje = "Hola mundo"
print(mensaje)

# 3)
print("Hola", "mundo")

# 4) puedo concatenar varias variables para producir un resultado:
a = "Hola"
b = "mundo"
mensaje = a + " " + b
print(mensaje)

# 5) usando f strings
mensaje = "Hola mundo"
print(f"{mensaje}")

# 6) usando format
mensaje = "{} {}".format("Hola", "mundo")
