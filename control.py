limite_compra = 190
limite_venta = 200
limite_se_prende_fuego_todo = 500

print("Ingrese el valor actual del dolar: ")
valor = input()
dolar_hoy = float(valor)

if dolar_hoy > limite_compra and dolar_hoy < limite_venta:
    print("Vende dolares")
elif dolar_hoy > limite_venta and dolar_hoy < limite_se_prende_fuego_todo:
    print("Compra dolares")
elif dolar_hoy > limite_se_prende_fuego_todo:
    print("Retira todo tu dinero del banco")
else:
    print("Por ahora no hagamos nada")
  
print("Programa finalizado")