from os import system
from pandas import DataFrame
#Clase diferencias de Newton
class dif:

#region Variables
    table = None
    data_size = None
    column_header = ["x","f(x)"]
    h = None
    sp = None
    sr = None
    point = None
    polynomial = None
#endregion

    # Constructor
    def __init__(self,data):
        self.table = data
        self.data_size = len(self.table)

    def showTable(self):
        print(DataFrame(self.table))

    # Método para corregir datos
    def dataCorrection(self):
        row = int(input("Seleccione la fila a corregir: "))
        self.table[row][0] = float(input("Ingrese el valor de x: "))
        self.table[row][1] = float(input("Ingrese el valor de f(x): "))

    # Método que ordena los datos
    def bubble(self):
        for i in range(self.data_size):
            for j in range(self.data_size - 1):
                k = j + 1
                if self.table[j] > self.table[k]:
                    self.table[k], self.table[j] = self.table[j], self.table[k]
        return self.table

    # Método que verifica la distancia entre puntos
    def distanceCheck(self):
        self.h = self.table[self.data_size-1][0] - self.table[self.data_size-2][0]
        for i in range(self.data_size-1):
            if self.table[i+1][0] - self.table[i][0] != self.h:
                print("Las distancias entre puntos son diferentes!")
                return

    # Método que obtiene la tablas de diferencias a partir de datos introducidos
    def setData(self):
        self.table = self.bubble()
        self.distanceCheck()
        # Crea un arreglo para la tabla de diferencias. Al ser una matriz cuadrada se desperdicia memoria
        #self.table = [[None]*(data_size+1) for i in range(data_size)]

        # Crea un arreglo para la tabla, no desperdicia memoria
        data = [None]*(self.data_size)
        k = self.data_size+1
        for i in range(self.data_size):
            if (i>0): k -= 1
            data[i] = [None]*k

        # Vacía los datos en la tabla.
        for j in range(2):
            for i in range(self.data_size):
                data[i][j] = self.table[i][j]
        self.table = data

        # Rellena la tabla de diferencias
        k = self.data_size-1
        for j in range(self.data_size-1):
            for i in range(k):
                self.table [i][j+2] = self.table[i+1][j+1] - self.table[i][j+1]
            k = k-1

    # Método que muestra la tabla
    def showTab(self):
        print(DataFrame(self.table,columns=self.column_header))

    # Método que pregunta por el valor a interpolar
    def getValue(self,point):
        self.setData()
        while self.point == None:
            if ((self.table[0][0] < point) and (point < self.table[self.data_size-1][0])):
                self.point = point
                self.sp = (self.point - self.table[0][0])/self.h
                self.sr = (self.point - self.table[self.data_size-1][0])/self.h
            else:
                point = float(input("¡El punto a interpolar esta fuera del rago de datos!\nElija otro: "))
                self.point = None

    # Método que interpola el valor deseado.
    def getPolynomialValue(self,grad):
        if self.point == None:
            return "Tas mal"
        if self.data_size-1 < grad:
            return "¡Grado imposible de obtener! Pruebe con otro."
        else:
            position = 0
            for i in range(self.data_size):
                if (self.table[i][0] < self.point): 
                    position += 1
            print("Con los datos ordenados, su punto a interpolar esta entre las fila",position,"y",str(position+1))
            if (position*2 < self.data_size):
                self.polynomial = self.table[0][grad+1]*(self.sp-(grad)+1)/(grad)
                for i in reversed(range(grad)):
                    if i==0:
                        self.polynomial=self.table[0][1]+self.polynomial
                        return self.polynomial
                    self.polynomial = (self.polynomial+self.table[0][i+1])*(self.sp-i+1)/i
            else:
                self.polynomial = self.table[self.data_size-1-grad][grad+1]*(self.sr+(grad)-1)/(grad)
                for i in reversed(range(grad)):
                    if i==0:
                        self.polynomial=self.table[self.data_size - 1][1]+self.polynomial
                        return self.polynomial
                    self.polynomial = (self.polynomial+self.table[self.data_size-1-i][i+1])*(self.sr+i-1)/i

def lecturaDatos():
    # datos = [[1,5],[2,6],[3,5]]
    tamaño = int(input("Número de puntos: "))
    datos = [[None for y in range(2)]
             for x in range(tamaño)]
    for i in range(tamaño):
        print(" x",i,': ',sep='',end='')
        datos[i][0] = float(input())
        print(' f(x',i,'): ',sep='',end='')
        datos[i][1] = float(input())
    del tamaño
    return datos

def interMenú():
    resp = "s"
    while (resp=="s"):
        system('cls')
        x = None
        a = lecturaDatos()
        x = dif(a)
        print("Sus datos son")
        x.showTab()
        resp = input("¿Desea corregir algún dato? (s/n): ")
        if(resp == "s"):
            x.dataCorrection()
        resp = 's'
        while(resp == "s"):
            x = dif(a)
            x.getValue(float(input("Ingrese el punto a interpolar: ")))
            x.showTable()
            print("El resultado interpolado es: ",x.getPolynomialValue(int(input("Ingrese el grado del polinomio deseado: "))))
            resp = input("¿Desea interpolar otro punto en la tabla? (s/n): ")
            system('cls')
        resp = input("¿Desea insertar otra tabla? (s/n): ")