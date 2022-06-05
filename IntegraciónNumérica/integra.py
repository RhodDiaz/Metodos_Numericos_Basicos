import numpy as np
from os import system

def menuIntegral():
    print("Programa de integración Numérica realizado por:\nDíaz Barriga Reyes Rodolfo\ty\nGómez Correa Gustavo Vladimir\n")
    elección = int(input("Seleccione la formula a integrar:\n1. f(x)=x^4*√(3+2x^2)/3\n2. f(x)=x^5/((x^2+4)^(1/5))\nElección: "))
    intervalo = np.array([input("Ingrese la cota inferior: "),input('Ingrese la cota superior: ')],dtype=float)
    nsubint = int(input("Ingrese el número de subintervalos: "))
    datos = tablita(elección=elección,nsubint=nsubint,intervalo=intervalo)
    print(integra(datos=datos,numIntervalos=nsubint))

    return True if int(input("¿Desea probar con otros datos?\n1. Sí.\n2. No.\nRespuesta: ")) == 1 else False
    
def integra(datos,numIntervalos):
    if numIntervalos % 2 == 0:
        return un_tercio(datos)
    if numIntervalos == 3:
        return tres_octavos(datos)
    if int(numIntervalos) >1:
        return simpson(datos)
    else: print("El número de intervalos no es válido")

def tablita(elección,nsubint,intervalo):
    h = (intervalo[1]-intervalo[0])/nsubint
    valores = np.zeros((nsubint+1,2))
    if elección == 1:
        # Evalua la primera función: f(x)=x^4*√(3+2x^2)/3.
        valores[0,0], valores[0,1] = intervalo[0], f1(intervalo[0])
        valores[nsubint,0], valores[nsubint,1] = intervalo[1], f1(intervalo[1])
        for i in range(1,nsubint):
            valores[i,0], valores[i,1] = valores[i-1,0]+h, f1(valores[i-1,0]+h)
    if elección == 2:
        # Evalua la segunda función: f(x)=x^4*√(3+2x^2)/3.
        valores[0,0], valores[0,1] = intervalo[0], f2(intervalo[0])
        valores[nsubint,0], valores[nsubint,1] = intervalo[1], f2(intervalo[1])
        for i in range(1,nsubint):
            valores[i,0], valores[i,1] = valores[i-1,0]+h, f2(valores[i-1,0]+h)
    return valores[:,1], h

def f1(x):
    return x**4*np.sqrt(3+2*x**2)/3

def f2(x):
    return x**5/((x**2+4)**(1/5))

def un_tercio(datos):
    tablita, h = datos
    indice = np.size(tablita)-1
    valor = tablita[0]+tablita[indice]
    valor4 = 0
    valor2 = 0
    # Calcula la suma para los indices impares.
    for i in range(1,indice,2):
        valor4 += tablita[i]
        # print(i,tablita[i])
    valor4 *= 4
    # Calcula la suma para los indices pares.
    for i in range(2,indice-1,2):
        valor2 += tablita[i]
    # Calcula el valor de la integral definida
    valor2 *= 2
    valor += valor2 + valor4
    del valor2, valor4
    return valor*h/3

def tres_octavos(datos):
    tablita, h = datos
    return 3/8*h*(tablita[0]+3*tablita[1]+3*tablita[2]+tablita[3])

def simpson(datos):
    datos, h = datos
    tamaño = np.size(datos)
    tabla1 = np.zeros(tamaño-3)
    tabla2 = np.zeros(4)
    for i in range(tamaño-3):
        tabla1[i] = datos[i]
    for i in range(4):
        tabla2[i] = datos[i+tamaño-4]
    return un_tercio(datos=[tabla1,h]) + tres_octavos(datos=[tabla2,h])

def integraMain():
    system("cls")
    seguir = True
    while seguir:
        seguir = menuIntegral()
        system("cls")