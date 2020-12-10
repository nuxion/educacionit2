# diccionarios , clase 4
#lista = ["frutillas", "manzanas", "peras"]
# dic = {"frutas": ["frutillas", "manzanas", "peras"], "ferreteria": ["tuercas": "tornillos"]}

# CRUD -> Create, Read, Update, Delete
# create
print("Create dic")
dic = {'clave': 'valor'}
dic.update({'clave2': 'otro valor'})
print(dic)
# Read
print("Read key")
print(dic['clave'])
print(dic['clave2'])
# Update
print("Update key")
dic['clave'] = "reemplazo el valor viejo"
print(dic['clave'])
# Delete
print("delete key")
del(dic['clave'])
print(dic)






