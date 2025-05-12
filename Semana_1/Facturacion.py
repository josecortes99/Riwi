while True:
    
    print ("\n**Ingrese los datos del producto**")
    NombreProdcuto = input("\nIngrese nombre del producto: ")
    PrecioUnitario = float (input ("\nIngrese el precio unitario en pesos del producto ej (7.800): "))
    CantidadProductos = int (input ("\nIngrese cantidad adquirida del producto: "))
    PorcentajeDescuento = int (input ("\nIngrese el porcentaje del descuento del producto ej (50): "))
    
    if NombreProdcuto.isalpha():

        if PrecioUnitario > 0 and CantidadProductos > 0:
    
            if 0 <= PorcentajeDescuento <= 100:
        
                CostoTotalCompra = CantidadProductos * PrecioUnitario
                print (f"\nCosto total de la compra es {CostoTotalCompra:.3f} con el producto", NombreProdcuto)
        
                MontoFinal = CostoTotalCompra * (1 - PorcentajeDescuento / 100)
                print (f"\nMonto final con descuento es: {MontoFinal:.3f}")
        
            else:
                print ("\n## Error, ingrese un porcentaje entre 0 y 100##")
        
        else:
            print ("\n## Error, ingrese un numero positivo##")
    else:
        print("\n## Error, El nombre solo debe contener letras##")
    
    

