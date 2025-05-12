Usuario = {
    'saldo':0
}

while True:
    print("\n---Bienvenido a BBVA ¿Que deseas realizar hoy?---")
    print("1. Ver saldo actual")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Historial")
    print("5. salir")
        
    Opcion = int(input("\nIngrese una opcion (Numero): "))
        
    if Opcion == 1:
        print(f"\nSaldo actual: {Usuario["saldo"]}")
        
    elif Opcion == 2:
        retiro = int(input("\nCuanto desea retirar: "))
        if retiro > Usuario["saldo"]:
            print(f"\nFondos insuficientes")
        else:
            Usuario["saldo"] -= retiro
            print(f"Saldo actual: {Usuario['saldo']}")
        
    elif Opcion == 3:
        deposito = int(input("\nCuanto desea depositar?: "))
        Usuario["saldo"] += deposito
        print(f"Saldo actual: {Usuario['saldo']}")
        
    elif Opcion == 4:
        print()
    elif Opcion == 5:
        print("\nGracias por visitarnos, hasta luego")
        break
    else:
            print("\n###Error, Ingrese una opcion valida###")


        
    

    
            
