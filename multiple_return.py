import datetime

def suma(a, b):
    resultado = a + b
    if resultado < 0:
        return resultado, False
    else:
        return resultado, True

res, positivo = suma(10, 50)
print(res, positivo)
print(type(res), type(positivo))
print(datetime.datetime.now())