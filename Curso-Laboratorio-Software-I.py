import os
def Mostrar(file,o):
    with open(file,o)as file:
        for linea in file:
            print(linea)
def Escribir(file,o):
   with open(file,o)as file:
        texto=str(input("ingrese texto: "))
        file.write("\n"+texto)
def Aumentar(file,o):
   with open(file,o)as file:
        texto=str(input("ingrese texto: "))
        file.write("\n"+texto)
# Módulo Menu
def Menu():
    print('OPERACIONES')
    print('===========')
    print('1.- Mostrar ')
    print('2.- Escribir ')
    print('3.- Agregar ')
    print('4.- Salir ')

# Módulo procesar números racionales
def Procesar():
    file="E:\datos.txt"
    Existe=os.path.isfile(file)
    Opcion = 0
    if Existe:
        while (Opcion != 4):
            Menu()
            Opcion = int(input('Ingrese opción: '))
            if (Opcion == 1):
                Mostrar(file,"r")
            elif (Opcion == 2):
                Escribir(file,"w")
            elif (Opcion == 3):
                Aumentar(file,"a")
    else:
        print("el archivo no existe")
# Programa principal
Procesar()
