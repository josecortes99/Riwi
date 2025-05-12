Numeros = [1, 3, 5, 7, 9]
numero = int (input("\nIngrese un numero que este en la lista: "))

if numero in Numeros:
    print (f"\nEl numero {numero} esta en la lista")
    posicion = Numeros.index(numero)
    print (f"\nEsta en la posicion: ", posicion)
else:
    print (f"\nEl numero {numero} no esta en la lista")