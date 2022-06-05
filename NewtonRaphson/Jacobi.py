import numpy as np
import pandas as pd
from os import system

# ¿...y si hacemos que esta función tambien regrese la jacobiana?
def F1(x):
    Fx = np.array([x[0]**2+x[0]*x[1]-10,x[1]+3*x[0]*x[1]**2-50])
    jacobi = np.array([[2*x[0]+x[1], x[0]], 
                       [3*x[1]**2,   1+6*x[0]*x[1]]])
    multi = np.dot(np.linalg.inv(jacobi),Fx)
    punto = x - multi
    error = np.max(np.abs(Fx))
    return Fx, jacobi, multi, error, punto

def F2(x):
    Fx = np.array([x[0]**2+x[1]**2-9,np.exp(x[0])-2*x[1]-3])
    jacobi = np.array([[2*x[0],         2*x[1]], 
                       [-np.exp(x[0]),  -2]])
    multi = np.dot(np.linalg.inv(jacobi),Fx)
    punto = x - multi
    error = np.max(np.abs(Fx))
    return Fx, jacobi, multi, error, punto

def F3(x):
    Fx = np.array([2*x[0]**2-4*x[0]+x[1]**2+3*x[2]**2+6*x[2]+2, x[0]**2+x[1]**2-2*x[1]+2*x[2]**2-5, 3*x[0]**2-12*x[0]+x[1]**2-3*x[2]**2+8])
    jacobi = np.array([[4*x[0]-4 , 2*x[1], 6*x[2]+6],
                       [2*x[0], 2*x[1]-2, 4*x[2]],
                       [6*x[0]-12, 2*x[1], -6*x[2]]])
    multi = np.dot(np.linalg.inv(jacobi),Fx)
    punto = x - multi
    error = np.max(np.abs(Fx))
    return Fx, jacobi, multi, error, punto

def F4(x):
    Fx = np.array([x[0]**2-4*x[0]+x[1]**2, x[0]**2-x[0]-12*x[1]+1,3*x[0]**2-12*x[0]+x[1]**2-3*x[2]**2+8])
    jacobi = np.array([[2*x[0]-4 , 2*x[1], 0],
                       [2*x[0]-1, -12, 0],
                       [6*x[0]-12, 2*x[1], -6*x[2]]])
    multi = np.dot(np.linalg.inv(jacobi),Fx)
    punto = x - multi
    error = np.max(np.abs(Fx))
    return Fx, jacobi, multi, error, punto

def MenúNewton():
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'right')
    pd.set_option('display.precision', 8)

    print('Realizado por:\n Gustavo Vladimir Gómez Correa y\n Rodolfo Díaz Barriga Reyes\n\nSistemas de Ecuaciones No Lineales por Método de Newton Raphson\n')
    print(' 1.\tF(X) = 0\n\tf1 (x,y) = x^2 + xy - 10 = 0\n\tf2 (x,y) = y + 3xy^2 - 50 = 0\n')
    print(' 2.\tF(X) = 0\n\tf1 (x,y) = x^2 + y^2 - 9 = 0\n\tf2 (x,y) = - e^x - 2y - 3 = 0\n')
    print(' 3.\tF(X) = 0\n\tf1 (x,y,z) = 2x^2 - 4x + y^2 + 3z^2 + 6z + 2 = 0\n\tf2 (x,y,z) = x^2 + y^2 - 2y + 2z^2 - 5 = 0\n\tf3 (x,y,z) = 3x^2 - 12x + y^2 - 3z^2 + 8 = 0\n')
    print(' 4.\tF(X) = 0\n\tf1 (x,y,z) = x^2 - 4x + y^2 = 0\n\tf2 (x,y,z) = x^2 - x - 12y + 1 = 0\n\tf3 (x,y,z) = 3x^2 - 12x + y^2 - 3z^2 + 8 = 0\n')

    senl = int(input('Ingrese el número del sistema que desea resolver: '))
    error = float(input('Tolerancia deseada: '))
    iteraciones = int(input('Máximo de iteraciones: '))

    # Solución para el sistema i
    if senl == 1:
        # Leemos el punto inicial
        print('Ingrese su punto incial:')
        x0, y0 = float(input(' x0: ')), float(input(' y0: '))
        fx, jacobi, multi, contadorError, punto = F1(np.array([x0,y0]))
        print('\nIteración:',str(0),'\n F(X):\n',pd.DataFrame(fx).to_string(index=False,header=False,col_space=15),'\n J(X):\n',pd.DataFrame(jacobi).to_string(index=False,header=False,col_space=15),'\n FJ^-1:\n',pd.DataFrame(multi).to_string(index=False,header=False,col_space=15),'\n Error:',contadorError,'\n Nuevo Punto: ',punto,sep='')
        contadorIteraciones = 0
        while(error < contadorError and contadorIteraciones < iteraciones):
            contadorIteraciones += 1
            fx, jacobi, multi, contadorError, punto = F1(punto)
            print('\nIteración:',str(contadorIteraciones),'\n F(X):\n',pd.DataFrame(fx).to_string(index=False,header=False,col_space=15),'\n J(X):\n',pd.DataFrame(jacobi).to_string(index=False,header=False,col_space=15),'\n FJ^-1:\n',pd.DataFrame(multi).to_string(index=False,header=False,col_space=15),'\n Error:',contadorError,'\n Nuevo Punto: ',punto,sep='')

    elif senl == 2:
        '''Código para el sistema 2'''
        print('Ingrese su punto incial:')
        x0, y0 = float(input(' x0: ')), float(input(' y0: '))
        fx, jacobi, multi, contadorError, punto = F2(np.array([x0,y0]))
        print('\nIteración:',str(0),'\n F(X):\n',pd.DataFrame(fx).to_string(index=False,header=False,col_space=15),'\n J(X):\n',pd.DataFrame(jacobi).to_string(index=False,header=False,col_space=15),'\n FJ^-1:\n',pd.DataFrame(multi).to_string(index=False,header=False,col_space=15),'\n Error:',contadorError,'\n Nuevo Punto: ',punto,sep='')
        contadorIteraciones = 0
        while(error < contadorError and contadorIteraciones < iteraciones):
            contadorIteraciones += 1
            fx, jacobi, multi, contadorError, punto = F2(punto)
            print('\nIteración:',str(contadorIteraciones),'\n F(X):\n',pd.DataFrame(fx).to_string(index=False,header=False,col_space=15),'\n J(X):\n',pd.DataFrame(jacobi).to_string(index=False,header=False,col_space=15),'\n FJ^-1:\n',pd.DataFrame(multi).to_string(index=False,header=False,col_space=15),'\n Error:',contadorError,'\n Nuevo Punto: ',punto,sep='')

    elif senl ==3:
        '''Código para el sistema 3'''
        print('Ingrese su punto incial:')
        x0, y0, z0 = float(input(' x0: ')), float(input(' y0: ')), float(input(' z0: '))
        fx, jacobi, multi, contadorError, punto = F3(np.array([x0,y0,z0]))
        print('\nIteración:',str(0),'\n F(X):\n',pd.DataFrame(fx).to_string(index=False,header=False,col_space=15),'\n J(X):\n',pd.DataFrame(jacobi).to_string(index=False,header=False,col_space=15),'\n FJ^-1:\n',pd.DataFrame(multi).to_string(index=False,header=False,col_space=15),'\n Error:',contadorError,'\n Nuevo Punto: ',punto,sep='')
        contadorIteraciones = 0
        while(error < contadorError and contadorIteraciones < iteraciones):
            contadorIteraciones += 1
            fx, jacobi, multi, contadorError, punto = F3(punto)
            print('\nIteración:',str(contadorIteraciones),'\n F(X):\n',pd.DataFrame(fx).to_string(index=False,header=False,col_space=15),'\n J(X):\n',pd.DataFrame(jacobi).to_string(index=False,header=False,col_space=15),'\n FJ^-1:\n',pd.DataFrame(multi).to_string(index=False,header=False,col_space=15),'\n Error:',contadorError,'\n Nuevo Punto: ',punto,sep='')

    elif senl == 4:
        '''Código para el sistema 4'''
        x0, y0, z0 = float(input(' x0: ')), float(input(' y0: ')), float(input(' z0: '))
        fx, jacobi, multi, contadorError, punto = F3(np.array([x0,y0,z0]))
        print('\nIteración:',str(0),'\n F(X):\n',pd.DataFrame(fx).to_string(index=False,header=False,col_space=15),'\n J(X):\n',pd.DataFrame(jacobi).to_string(index=False,header=False,col_space=15),'\n FJ^-1:\n',pd.DataFrame(multi).to_string(index=False,header=False,col_space=15),'\n Error:',contadorError,'\n Nuevo Punto: ',punto,sep='')
        contadorIteraciones = 0
        while(error < contadorError and contadorIteraciones < iteraciones):
            contadorIteraciones += 1
            fx, jacobi, multi, contadorError, punto = F4(punto)
            print('\nIteración:',str(contadorIteraciones),'\n F(X):\n',pd.DataFrame(fx).to_string(index=False,header=False,col_space=15),'\n J(X):\n',pd.DataFrame(jacobi).to_string(index=False,header=False,col_space=15),'\n FJ^-1:\n',pd.DataFrame(multi).to_string(index=False,header=False,col_space=15),'\n Error:',contadorError,'\n Nuevo Punto: ',punto,sep='')
    
    else: print('Opción no válida.')
    return True if int(input('¿Desea probar con otro sistema?\n 1. Sí\n 2. No.\nRespuesta: ')) == 1 else False

def newtonMain():
    system('cls')
    regreso = True
    while regreso:
        system('cls')
        regreso = MenúNewton()
