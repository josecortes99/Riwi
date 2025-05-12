lista = [1,3,5,7,9]

numero = int (input("\nIngrese un numero: "))
posicion = int (input("\nEn que posicion quiere agregar el numero: "))

lista.insert(posicion, numero)
print (f"\nSe inserto el numero {numero} en la posicion", posicion)
print ("\nLista actualizada", lista)
