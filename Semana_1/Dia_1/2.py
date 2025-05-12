# Pide un número al usuario. Di si es positivo, negativo o si es cero.

while (True):
    
    try:
        
        Numero = int (input ("\nIngrese un numero: "))
        
        if Numero > 0:
            print ("\nEl numero es positivo")
            
        elif Numero < 0:
            print ("\nEl numero es negativo")
            
        else:
            print ("\nEl numero es cero")
            
    except ValueError:
        print ("\nError ingrese un numero")