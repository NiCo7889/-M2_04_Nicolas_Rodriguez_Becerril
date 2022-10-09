#APARTADO
lista = ["coche", "moto", "autobús", "furgoneta"]
tupla = ("hamburguesa", "pizza", "macarrones", "ensalada")
#APARTADO
print(lista)
print(tupla)
print("\n")
#APARTADO
print(lista[1])
print(tupla[-2])
print("\n")
#APARTADO
lista[0]="nuevo elemento"
print(lista)
print("\n")
  #no se puede modificar el contenido de una tpla
#APARTADO
print(len(lista))
print(len(tupla))
print("\n")
#APARTADO
print("coche" in lista)
print("hamburguesa" in tupla)
print("\n")
#APARTADO
lista.append('limusina')
print(lista)
  #no se pueden añadir elementos en una tupla
print("\n")
#APARTADO
lista.pop(0)
lista.pop(2)
lista.pop(-1)
print(lista)
print("\n")
  #no se puede eliminar el contenido de una tupla