#Pide al usuario su peso (kg) y altura (m). Calcula su IMC (peso / altura²) y muestra:

#"Bajo peso" si es menor a 18.5
#"Normal" si está entre 18.5 y 24.9
#"Sobrepeso" si está entre 25 y 29.9
#"Obesidad" si es mayor o igual a 30

while (True):
    
    try:
        
        Peso = int (input ("\nIngrese su pero en Kg: "))
        Altura = float (input ("\nIngrese su altura en m ej (1.70): "))
        
        IMC = (Peso / (Altura ** 2))
        
        print (IMC)
        
        if IMC < 18.5:
            print ("\nBajo peso")
            
        elif 18.6 <= IMC <= 24.9:
            print ("\nNormal")
            
        elif 25 <= IMC <=29.9:
            print ("\nSobrepeso")
            
        else:
            print ("\nObesidad")
            
    except ValueError:
        print ("\nIngrese solo numeros")