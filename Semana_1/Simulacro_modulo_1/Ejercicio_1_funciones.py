Cajero = {}
Total = 0
Cont = 1

def Depositar():
    valor = float(input("\nIngrese el monto a depositar"))
    Total = Total + 

def menu():
    while True:
        print("\n-----Bienvenido al cajero elija la opcion que desea realizar-----")
        print("1. Ver saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Ver historial de movimientos")
        print("5. Salir")
        
        opcion = int(input("\nIngrese la ocion que desea: "))
        
        if opcion == 1:
            Saldo()
        elif opcion == 2:
            Retirar()
        elif opcion == 3:
            Depositar()
        elif opcion == 4:
            Historial()
        elif opcion == 5:
            print("\n-----Gracias por visitarnos-----")
            break
menu()
    
