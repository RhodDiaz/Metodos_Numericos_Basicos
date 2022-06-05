import numpy as np
import pandas as pd
import os

class Table:
#region Variables
    size = None
    points = None
    table = None
    column_header = ["x","f(x)"]
#endregion

#   Constructor
    def __init__(self, csv = None):
        if csv == None:
            self.size = int(input("Ingrese el número de puntos a introducir: "))
            self.table = np.zeros((self.size,2),dtype=float)
            for i in range(self.size):
                self.table[i][0] = float(input("Ingese x"+str(i)+": "))
                self.table[i][1] = float(input("Ingese y"+str(i)+": "))
        else:
            self.table = np.array(pd.read_csv(csv, header=0))
            self.size = np.size(self.table[:,0])

#   Segundo constructor (no se puede usar más de uno como en Java)
    #def __init__(self,data):
    #    self.table = data

#   Método que imprime los datos
    def showTab(self):
        corrección = '1'
        while corrección == '1':
            os.system("cls")
            corrección = '2'
            # corrección = input("Su tabla es:\n"+str(pd.DataFrame(self.table,columns=self.column_header))+"\n\n¿Desea corregir algún dato?\n 1. Si.\n 2. No.\nRespuesta: ")
            corrección = input("Su tabla es:\n"+str(pd.DataFrame(self.table))+"\n\n¿Desea corregir algún dato?\n 1. Si.\n 2. No.\nRespuesta (1\\2): ")
            if corrección == '1': self.dataCorrection()

#   Método que regresa los datos
    def getTab(self):
        return self.table

#   Método que regresa el tamaño de la tabla
    def getSize(self):
        return self.size
        
#   Método para corregir datos
    def dataCorrection(self):
        row = int(input("Seleccione la fila a corregir: "))
        while row >= self.size or row < 0: 
            print("¡Elija una fila dentro del rango!\n")
            row = int(input("Seleccione la fila a corregir: "))
        self.table[row][0] = float(input("Ingrese el valor de x"+str(row)+": "))
        self.table[row][1] = float(input("Ingrese el valor de f(x"+str(row)+"): "))

#   Método que ordena los datos
    def bubble(self):
        for i in range(self.data_size):
            for j in range(self.data_size - 1):
                k = j + 1
                if self.table[j] > self.table[k]:
                    self.table[k], self.table[j] = self.table[j], self.table[k]
        return self.table

#   Método que verifica la distancia entre puntos
    def distanceCheck(self):
        self.h = self.table[self.data_size-1][0] - self.table[self.data_size-2][0]
        for i in range(self.data_size-1):
            if self.table[i+1][0] - self.table[i][0] != self.h:
                print("¡Las distancias entre puntos son diferentes!")
                return
        print("Las distancias entre puntos son iguales")

#   Método que regresa la x máxima
    def getMaxOfx(self):
        return np.max(self.table[:,0])

#   Método que regresa la x mínima
    def getMinOfx(self):
        return np.min(self.table[:,0])