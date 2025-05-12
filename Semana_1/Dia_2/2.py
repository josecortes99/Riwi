# Crea una lista con 5 números.
# Pide un número al usuario y verifica si está en la lista usando in.

while True:
    
    Numbers = [1, 2, 3, 4, 5]
    Number = int (input ("\nIngrese un numero entero: "))
    
    if Number in Numbers:
        print (f"\nEl numero {Number} esta en la lista.")
    else:
        print (f"\nEl numero {Number} no esta en la lista, ingrese otro numero.")

    
