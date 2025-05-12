# Pide un número entero. Indica si es par o impar.

while (True):
    
    try:
        
        NumeroEnt = int (input ("\nIngrese un numero entero: "))
        
        if NumeroEnt % 2 == 0:
            print ("\nEl numero es par")
        else:
            print ("\nEl numero es impar")
            
    except ValueError:
        print ("\nIngrese un numero entero")
    
            
            
        
    
    

