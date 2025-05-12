# Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
# Pide al usuario su nombre.
# Usa if para decir si está en la lista de invitados o no.

while True:
    
    Names = ["Ana", "Luis", "Sofia"]
    Name = input ("\nIngrese un nombre: ").capitalize()

    if Name in Names:
        print ("\nSu nombre esta en la lista")
    else:
        print ("\nSu nombre no esta en la lista")
    


        
    
