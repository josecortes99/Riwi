# Pide un número al usuario. Di si está dentro del rango de 1 a 10 (inclusive).

while(True):
    Numero = int ( input ("\nIngresa un numero entre de 1 y 10: "))
    if Numero in range(1,11):
        print ("\nEl numero esta dentro el rango")
        break
    else:
        print ("\nError, ingrese un numero dentro del rango especificado")

print (f"\nEl numero escogido es: {Numero}")
        
    
    

