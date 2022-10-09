#APARTADO1
set = {"coche", "moto", "autobús", "limusina"}
diccionario = {"nombre":"Nicolás", "edad": 18, "apellido":"Rodríguez", "cicudad":"Madrid"}
#APARTADO2
print(set)
print(diccionario)
print("\n")
#APARTADO3
  #en los sets no se puede mostrar un solo elemento, tienen que ir todos juntos
print(next(iter(diccionario)))
print("\n")
#APARTADO4
  #en los sets no se pueden hacer cambios 
diccionario["segundo apellido"] = diccionario.pop("apellido")
diccionario["segundo apellido"] = "Becerril"
print(diccionario)
print("\n")
#APARTADO5
print(len(set))
print(len(diccionario))
print("\n")
#APARTADO6
print("moto" in set)
print("nombre" in diccionario)
print("\n")
#APARTADO7
set.add("tractor")
diccionario["apellido"] = "Rodríguez"
print(set)
print(diccionario)
print("\n")
#APARTADO8
set.discard("tractor")
diccionario.pop("edad")
print(set)
print(diccionario)