import csv
import os
import msvcrt
#Para random de letras
#import random as rd
#DATOS = ("A","B","C","D")
#print(rd.choice(DATOS))

#c para almacenar prods
autos = []


############################################### DISEÑO
def limpiar():
    print("<<press any>>")
    msvcrt.getch()
    os.system("cls")
    
def printR(texto):
    print(f"\033[31m{texto}\033[0m")

def printV(texto):
    print(f"\033[32m{texto}\033[0m")

def printA(texto):
    print(f"\033[34m{texto}\033[0m")

def menu():
    printA("Sistema gestión de Vehículos")
    printA("-----------------------------")
    printA("1) Agregar vehículo")
    printA("2) Listar vehículo")
    printA("3) Eliminar vehículo")
    printA("4) Modificar vehículo")
    printA("5) Filtrar vehículos por marca")
    printA("6) Imprimir reporte de vehículos")
    printA("0) SALIR")
    printA("-----------------------------")

marcas = ("KIA","CHEVROTLET","AUDI","NISSAN","OTRO") 
tipoauto= ("Automóvil", "Camión", "Autobús","Motocicleta")   
def seleccionmarca():
    for i in range (len(marcas)): #recorrer tupla, mostrar tipos prod
        print(f"{i+1}.-{marcas[i]}")
    seleccion = int(input("Seleccione: "))-1 # seleccionar posición en tupla
    if seleccion >= 0 and seleccion<len(marcas): #validar que sea posición válida
        return marcas[seleccion] #si es válido retorna tipo
    else:
        return None #si no es válido retorna vacío
def selecciontipo():
    for i in range (len(tipoauto)): #recorrer tupla, mostrar tipos prod
        print(f"{i+1}.-{tipoauto[i]}")
    seleccion = int(input("Seleccione: "))-1 # seleccionar posición en tupla
    if seleccion >= 0 and seleccion<len(tipoauto): #validar que sea posición válida
        return tipoauto[seleccion] #si es válido retorna tipo
    else:
        return None #si no es válido retorna vacío
    
def validcode(patente):
    for i in range(len(autos)):
        if autos[i][0] == patente: # i recorre productos, 0 recorre el primer dato de tupla (id prod)
            return i #retornando la posición del producto 
    return -1 #retorna valor negativo que indica que no existe

def guardaraut(patente, marca, tipo, precio, stock):
    if validcode(patente) ==-1:
        if tipo  != None:
            autos.append([patente, marca, tipo, precio, stock])
            printV(f"Vehículo registrado")
        else:
            printR("Tipo no valido") 
    else:
        printR("Código repetido")

def listarprod():
    if len(autos)>0:
        for i in range(len(autos)):
            printA(f"{i+1}.-{autos [i][0]} {autos[i][1]} {autos[i][2]} ${autos[i][3]} {autos[i][4]}")
    else:
        printR("No hay vehículos registrados")

def elimnprod(id):
    pos = validcode(id)
    if pos >=0:
        autos.remove(autos[pos])
        printV("Vehículo eliminado")
    else:
        printR("La patente no existe")
def modau(patente):
        for i in range(len(autos)):
            if autos[i][0] == patente:
                nueva_marca = seleccionmarca()
                nuevo_tipo = selecciontipo()
                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                if nuevo_precio >0:
                    nuevo_stock = int(input("Ingrese el nuevo stock: "))
                    if nuevo_stock >0:
                        autos[i][1] = nueva_marca
                        autos[i][2] = nuevo_tipo
                        autos[i][3] = nuevo_precio
                        autos[i][4] = nuevo_stock
                        return printV("Datos modificados!")
                    else:
                        printR("no hay stock disponible")
                else:
                    printR("Precio incorrecto")
            else:
                printR("La patente no existe")

def listfilt():
    if len(autos)>0:
        ms = seleccionmarca()
        for i in range(len(autos)):
            if ms == autos[i][1]:
                printA(f"{i+1}.- {autos[i][1]} {autos[i][0]} {autos[i][2]} ${autos[i][3]} {autos[i][4]}")
    else:
        printR("No hay vehículos registrados")


def imprep(nombrereporte): #esto hace que al pedir nombre, se genere con ese nombre el archivo.
    if len(autos)>0:
        with open(f'{nombrereporte}.csv','w',newline='', encoding='utf-8') as a:
            escribir = csv.writer(a, delimiter=",")
            escribir.writerows(autos)
            printV(f"Reporte {nombrereporte}.csv Generado")
    else:
        printR(" No hay productos registrados")
