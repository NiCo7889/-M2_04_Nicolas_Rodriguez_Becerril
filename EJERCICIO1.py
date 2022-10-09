#APARTADO1
lista = ["coche", "moto", "autobús", "furgoneta"]
tupla = ("hamburguesa", "pizza", "macarrones", "ensalada")
#APARTADO2
print(lista)
print(tupla)
print("\n")
#APARTADO3
print(lista[1])
print(tupla[-2])
print("\n")
#APARTADO4
lista[0]="nuevo elemento"
print(lista)
print("\n")
  #no se puede modificar el contenido de una tpla
#APARTADO5
print(len(lista))
print(len(tupla))
print("\n")
#APARTADO6
print("coche" in lista)
print("hamburguesa" in tupla)
print("\n")
#APARTADO7
lista.append('limusina')
print(lista)
  #no se pueden añadir elementos en una tupla
print("\n")
#APARTADO8
lista.pop(0)
lista.pop(2)
lista.pop(-1)
print(lista)
print("\n")
  #no se puede eliminar el contenido de una tupla