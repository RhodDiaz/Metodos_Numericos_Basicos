import tkinter as tk     # from tkinter import Tk for Python 3.x
from os import system
from Minimos.data import*
from Minimos.mmcc import*
from NewtonRaphson.Jacobi import*
from IntegraciónNumérica.integra import*
from DiferenciasDeNewton.InterpolacionNewton import*
from tkinter import filedialog


def main():
    system('cls')
    print("Paquete Final.\nDíaz Barriga Reyes Rodolfo\ty\nGómez Correa Gustavo Vladimir\n")
    eleccion = int(input("Seleccione una opción:\n 1. Newton Multivariable.\n 2. Diferencias de Newton.\n 3. Mínimos Cuadrados.\n 4. Integración Numérica.\n 0. Salir.\nRespuesta: "))
    if   eleccion == 1:
        newtonMain()
    elif eleccion == 2:
        interMenú()
    elif eleccion == 3:
        repetir = 1
        while repetir == 1:
            system('cls')
            print("Programa de minímos cuadrados realizado por:\n Díaz Barriga Reyes Rodolfo\ty\n Gómez Correa Gustavo Vladimir\n")
            print(co.Fore.YELLOW+"ADVERTENCIA"+co.Style.RESET_ALL+": el CSV debe tener una fila cabecera al inicio.\n")
            if int(input("Elija una opción:\n 1. Leer arcihivo CSV.\n 2. Leer por consola.\nRespuesta (1\\2): ")) == 1:
                raiz = tk.Tk()
                raiz.title('Seleccionar CSV')
                raiz.attributes("-topmost", True)
                raiz.withdraw()
                directorio = filedialog.askopenfilename(filetypes=(("Valores separados por comas","*.csv"),("all files","*.*")))
                x = Table(csv=directorio)
            else:
                x = Table()
            x.showTab()
            genericLessSquare = lessSquare(x.getTab())
            repetir = int(input('¿Desea probar con otra tabla de datos?\n1. Sí.\n2. No.\nRespuesta (1\\2): '))
    elif eleccion == 4:
        integraMain()
    elif eleccion == 0:
        print('¡Fue un gusto atenderle!\n')
        system('pase')
        return False
    else: 
        print("Opción no válida, intente nuevamente.\n")
        system('pause')
    return True

system('cls')
print('\tUNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO\n\tFACULTAD DE ESTUDIOS SUPERIORES ACATLÁN\n\n\tMATEMÁTICAS APLICADAS Y COMPUTACIÓN\n\n\tMÉTODOS NUMÉRICOS 2 | GRUPO: 2403\n\tPROFESORA: TERESA CARRILLO RAMÍREZ\n\tPAQUETE FINAL\n\n')
system("pause")
system('cls')

resp=True
while resp:
    resp=main()