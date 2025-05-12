# Pide un año al usuario. Determina si es bisiesto (es divisible entre 4 y no entre 100, excepto si también es divisible entre 400).

while (True):
    
    Año = int (input ("\nIngrese un año: "))

    if (Año % 4 == 0 and Año % 100 != 0) or (Año % 400 == 0):
        print ("\nEl año es bisiesto")
    
    else:
        print ("\nEl año no es bisiesto")