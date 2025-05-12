# Pide tres números al usuario.
# Usa condicionales (if) para decir cuál es el más pequeño.

while True:
    
    Numero1 = input("\nIngrese el numero 1: ")
    Numero2 = input("\nIngrese el numero 2: ")
    Numero3 = input("\nIngrese el numero 3: ")
    
    if Numero1 < Numero2:
        print ("\nNumero 1 es el mas pequeño")
    elif Numero2 < Numero3:
        print ("\nEl numero 2 es el mas pequeño")
    else:
        print ("\nEl numero 3 es el mas pequeño")