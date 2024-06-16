from funcs_actividad import limpiar,menu,printA,printR,printV,guardaraut,seleccionmarca,selecciontipo,validcode,listarprod,elimnprod,imprep,listfilt,modau

while True:
    limpiar()
    menu()
    opc = input("Seleccione: ")
    if opc == "0":
        printR("Chado :D")
        break
    elif opc =="1":
        printA("Agregar Vehículo")
        patente = int(input("Ingrese patente: "))
        if len(str(patente))>0 and len(str(patente)) <=6 and patente > 0 and patente <999999:
            printV("Seleccione marca")
            marca = seleccionmarca()
            printV("Seleccione tipo vehículo")
            tipo = selecciontipo()
            precio =int(input("Ingrese precio: "))
            if precio >0:
                stock =int(input("Ingrese stock: "))
                if stock >=0:
                    guardaraut(patente,marca,tipo,precio,stock)
                else:
                    printR("No hay stock disponible")
            else:
                printR("Precio no valido")
        else:
            printR("Patente no válida")
    elif opc =="2":
        printA("Listar vehículo")
        listarprod()

    elif opc =="3":
        printA("Eliminar vehículo")
        pat = int(input("Ingrese patente: "))
        elimnprod(pat)

    elif opc == "4":
        printA("Modificar Vehículo")
        pat = int(input("Ingrese patente: "))
        modau(pat)

    elif opc == "5":
        printA("Filtrar Vehículo")
        printA("Seleccione filtro por marca")
        listfilt()

    elif opc =="6":
        printA("Imprimir Reporte Productos")
        nombre = input(("Ingrese nomber reporte: ")).title()
        imprep(nombre)
    else:
        printR("Opción no válida")
