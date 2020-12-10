cursos = ["python", "javascript", "html", "mobile"]
alumnos = ["Jose", "Julieta", "Javier", "Simon", "Lorena"]

python = ["Jose", "Javier"]
html = ["Lorena", "Jose"]
javascript = ["lorena", "javier"]


def listar_alumnos_por_curso(python, html, javascript):

  for curso in [python, html, javascript]:
    print("Para el curso ", curso)
    for alumno in curso:
      print(alumno)


def listar_alumnos(cursos):
    for key in cursos:
        print(f"La key es: {key}")
        print(f"El elemento de la key {key} es {cursos[key]}")

# listar_alumnos_por_curso(python, html, javascript)
#          0       1        2
lista = ["pepe", "jose", "julia"]
lista[0]
lista[1]
cursos = { 
    'python': [ 'javier'],
    'html': ['lorena', 'jose'],
    'javascript': ['lorena', 'javier', 'jose'],
    'mobile': ['jose'],
    'Machine Learning': ['lorena', 'jose']
    }
cursos['python']
cursos['html']
# Ejercicio, dado el diccionario cursos, se necesita
# una funcion que dado un alumno, devuelva un array de los cursos
# en los que esta anotado.
# Ej:
# 
# funcion(cursos, "jose") -> ['python', 'html']

def buscar_en_lista(lista, alumno):
    """
    dada la lista ['jose', 'pepe', 'maria']
    si alumno esta:
        devuelvo: True
    sino:
        devuelvo: False
    """
    esta = False
    for x in lista:
        if x == alumno:
            esta = True
    return esta


def buscar_en_dic(cursos, alumno):
    resultado = []
    for nombre_curso, lista_alumnos in cursos.items():
        if alumno in lista_alumnos:
            resultado.append(nombre_curso)
    return resultado


resul = buscar_en_dic(cursos, 'jose')
print("Los cursos en los que esta asignado jose, son: ", resul)