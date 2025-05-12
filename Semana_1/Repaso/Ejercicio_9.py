Nota = int (input ("\nIngrese una nota de 0 a 10: "))

if 0 < Nota < 10:
    
    if 0 <= Nota <= 5:
        print ("\nperdio")
    elif 6 <= Nota <= 8:
        print ("\nAprovado")
    else: 
        print ("\nSobresaliente")
        
else:
    print ("\nIngrese un numero de 0 a 10")
    

 