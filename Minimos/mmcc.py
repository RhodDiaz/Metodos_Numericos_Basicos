import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import colorama as co

class lessSquare:
    def __init__(self,datos):
        table = datos
        tabSize = int(np.size(table[:,0]))
        if tabSize <= 1:
            print("¡Necesito más de un puntos!")
            return
        elección = 1
        #Pide el grado del polinomio
        while elección == 1:
            grado = int(input("Inserte el grado del polinomio: "))
            while grado >= tabSize:
                grado = int(input(str("Su tabla de datos es demasiado pequeña para el polinomio de grado "+str(grado)+'. Pruebe con uno de grado menor que '+str(tabSize)+'.\nNuevo grado: ')))
            ''' 
            #------------------------Código Original------------------------
            tamaño = np.size(table[0])
            sumas = np.zeros((grado*3+2))
            
            #Calcula suma de xi^0
            sumas[0] = tamaño
            
            #suma de yix^0
            for i in range(tamaño):
                sumas[grado*2+1] += table[columna][i]
            
            #Calcula el resto de las sumas de xi^(j+k) y sumas de yi^*xi^(j+k)
            for j in range(grado):
                for i in range(tamaño):
                    xPotencia = np.float_power(table[0][i],(j+1))
                    sumas[j+1] += xPotencia
                    sumas[j+1+grado] += np.float_power(table[0][i],(j+1+grado))
                    sumas[grado*2+j+2] += np.multiply(xPotencia,table[1][i])'''    
            
            # Cálculo de sumas (Edición Numpy)
            sumas = np.zeros((grado*3+2))
            sumas[0] = tabSize
            sumas[grado*2+1] = np.sum(table[:,1])
            potenciaGrado = np.float_power(table[:,0],grado)
            for i in range(grado):
                potencia = np.float_power(table[:,0],i+1)
                sumas[i+1] = np.sum(potencia)
                sumas[i+grado+1] = np.sum(np.multiply(potencia,potenciaGrado))
                sumas[grado*2+i+2] = np.sum(np.multiply(potencia,table[:,1]))
            del potenciaGrado, potencia
            
            # Crea las matrices
            sistema = np.zeros((grado+1,grado+1))
            solución = np.zeros((grado+1))
            for j in range(grado+1):
                for i in range(grado+1):
                    sistema[j][i] = sumas[i+j]
                solución[j] = sumas[grado*2+1+j]
            del sumas
            
            # Da los coefieientes
            coeficientes = np.linalg.solve(sistema,solución)
            del sistema, solución
            polinomio = ''
            for i in range(grado+1):
                polinomio = polinomio + str(coeficientes[i]) + "*x^"+str(i) + '+'
            polinomio=polinomio[:-1]
            
            # Inicia la gráfica según los puntos dados y el polinomio obtenido
            fig, ax = plt.subplots()
            max = int(np.max(table[:,0]))
            min = int(np.min(table[:,0]))
            x = np.linspace(min, max, np.abs(max + min)*grado)
            polinomio = polinomio.replace("+-","-")
            polinomio = polinomio.replace("*x^0","")
            polinomio = polinomio.replace("*x^1+","*x+")
            poligraf = polinomio.replace("^","**")
            # eval("ax.plot(x,"+poligraf+')')
            ax.plot(x,eval(poligraf))
            
            del grado
            
            # Calcula el error
            error = np.zeros(tabSize)
            for i in range(tabSize):
                a = eval(poligraf.replace("x",str(table[i][0])))
                error[i] = (table[i][1] - a)**2
            errorNumerico = np.sum(error)

            print("El polinomio, con un error de "+co.Fore.YELLOW+str(np.round(errorNumerico,5))+co.Fore.WHITE+", es:\n"+co.Fore.GREEN+polinomio+co.Style.RESET_ALL)

            del polinomio, poligraf, error, errorNumerico, a, i
            
            # Puntos
            plt.scatter(table[:,0],table[:,1], color = 'red', s = 14)
            
            # Leyendas en los ejes
            plt.xlabel('x')
            plt.ylabel('y')
            
            titulo = "Gráfica"
            # Nombre de la gráfica
            plt.title(titulo)
            del titulo
            plt.show()

            elección =  int(input("¿Desea probar con el grado de otro polinomio?\n1. Repetir proceso.\n2. Regresar.\nRespuesta (1\\2): "))
        del elección, tabSize