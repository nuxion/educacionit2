# scope, clase 4
#default = "Hola mundo"
glob = "Yo soy global"
def saludar(mensaje="hola mundo", repeat=5):
    glob = "Sobreescribo global"
    print(glob)
    local = "Yo soy una variable local"
    print(local)
    for x in range(repeat):
        print(mensaje)

print("Funcion saludar() con sus valores por defecto: ")
saludar()
print("Funcion saludar() con valores NO por defecto: ")
saludar("Chau universo", 1)
local = "Soy otra local"
print(local)
