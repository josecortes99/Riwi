#Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.

while (True):
    
    try:
         
        Numero1 = float (input ("\nIngrese el numero 1: "))
        Numero2 = float (input ("\nIngrese el numero 2: "))
    
        if Numero1 > Numero2:
            print ("\nEl numero 1 es mayor")
        
        elif Numero1 < Numero2:
            print ("\nEl numero 2 es mayor")
        
        else:
            print ("\nLos numero son iguales")
            
    except ValueError:
        print ("\nIngrese un numero")
        
        
    
    
    
