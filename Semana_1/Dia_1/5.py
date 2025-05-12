# Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina.

while (True):
    
    TotalCuenta = float (input ("\nIngrese el total de la cuenta en pesos ej (7.500): "))
    porcentaje = int (input ("\nIngrese un porcentaje ej (10): "))
    
    if porcentaje in [10, 15, 20]:
        
        propina = TotalCuenta * (porcentaje/100)
        print (f"\nla propina es {propina:.3f}")
        break
        
    else:
        print ("\nIngrese un porcentaje correcto")
        