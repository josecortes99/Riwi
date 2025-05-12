# Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número secreto.

while (True):
    
    try:
        
        print ("\n#Adivina el numero#")
        NumeroSecreto = int (input ("\nIngrese un numero: "))
        
        if  NumeroSecreto > 7:
            print ("\nEl numero es mayor")
        
        
        elif NumeroSecreto < 7:
            print ("\nEl numero es menor")
        
        
        else:
            print ("\nNumero correcto, gracias por participar")
            break
    
    except ValueError:
        print ("\nIngrese un numero")
        
        

        
    
    
    
    