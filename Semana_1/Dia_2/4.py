# Pide al usuario su edad.
# Si la edad es menor que 0 o mayor que 120, imprime "Edad no válida".
# Si está en el rango correcto, imprime "Edad válida".

while True:
    
    age = int (input ("\nIngrese su edad: "))
    
    if age < 0 or age > 120:
        print ("\nEdad no valida, ingrese una edad entre 0 y 120")
    
    else:
        print ("\nEdad valida")

