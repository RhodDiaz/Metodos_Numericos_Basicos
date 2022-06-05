import numpy as np
from pandas import DataFrame

class curva:
    tabla = None
    Si = None
    Matriz = None
    cabecera = ["xi","yi","hi","f[xi,xi+1]","f[i+1]-f[i]","ai","bi","ci","di","Si"]
    #cabecera = [0,1,2,3,4,5,6,7,8,9]
    '''
    n = número de puntos
    xi[i][0]    = Datos
    yi[i][1]    = Datos
    hi[i][2]    = Datos
    f[i][3]     = ([i][1]+[i+1][1])/[i][2]
    Df[i+1][4]  = 6*(f[i]-f[i-1])         hasta n-2
    ai[]....

    '''
    def __init__(self,puntos):
        tamaño = len(puntos)
        # Crea la tabla de datos
        self.tabla = np.zeros((tamaño,10))
        #self.tabla = [[None]*(10) for i in range(tamaño)]
        # Vacía los puntos en la tabla
        self.Matriz = np.zeros((tamaño - 2,tamaño - 2))
        for i in range(tamaño):
            for j in range(2):
                self.tabla[i][j] = puntos[i][j]
        # Rellena las hi
        for i in range(tamaño - 1):
            self.tabla[i][2] =  self.tabla[i+1][0] - self.tabla[i][0]
        # Rellena f[xi,xi+1]
        for i in range(tamaño - 1):
            self.tabla[i][3] = (self.tabla[i+1][1] - self.tabla[i][1])/self.tabla[i][2]
        # Rellena fi[i+1]-fi[i]
        for i in range(tamaño - 2):
            self.tabla[i+1][4] = 6*(self.tabla[i+1][3] - self.tabla[i][3])
        #Obtiene los Si
        if(tamaño != 3):
            self.Matriz[0][0] = 2*(self.tabla[0][2] + self.tabla[1][2])
            self.Matriz[0][1] = self.tabla[1][2]
            #
            self.Matriz[tamaño - 3][tamaño - 4] = self.tabla[tamaño - 3][2]
            self.Matriz[tamaño - 3][tamaño - 3] = 2 * (self.tabla[tamaño - 3][2] + self.tabla[tamaño - 2][2])
        
            for i in range (tamaño-4):
                self.Matriz[i+1][i] = self.tabla[i+1][2]
                self.Matriz[i+1][i+1] = 2 * (self.tabla[i+1][2] + self.tabla[i+2][2])
                self.Matriz[i+1][i+2] = self.tabla[i+2][2]
        else:
            self.Matriz[0][0] = 2*(self.tabla[0][2] + self.tabla[1][2])
        DeltaF = np.zeros((tamaño-2,1))
        for i in range(tamaño-2):
            DeltaF[i]= self.tabla[i+1,4]
        Si = np.matmul(np.linalg.inv(self.Matriz),DeltaF)
        for i in range(tamaño-2):
            self.tabla[i+1][9] = Si[i]
        #Captura ai, bi, ci, di
        for i in range(tamaño-1):
            self.tabla[i][5] = (self.tabla[i+1][9] - self.tabla[i][9])/(6*self.tabla[i][2])
            self.tabla[i][6] = self.tabla[i][9]/2
            self.tabla[i][7] = self.tabla[i][3] - (self.tabla[i+1][9] + 2*self.tabla[i][9])/6 * self.tabla[i][2]
            self.tabla[i][8] = self.tabla[i][1]
        #Regresa polinomios
        polinomios = [None]*(tamaño-1)
        redondeo = 5

        for i in range(tamaño-1):
            # 5             6           7           8   0           0
            # ai(x-xi)^3 + bi(x-xi)^2 + ci(x-xi) + di , xi<= x <= xi+1
            #print("{0} {4} {1} {4} {2} {4} {3} {4}".format(self.tabla[i][5], self.tabla[i][6], self.tabla[i][7], self.tabla[i][8], self.tabla[i][0]), self.tabla[i+1][0] )
            polinomios [i] = str("{0}(x-{4})^3+{1}(x-{4})^2+{2}(x-{4})+{3},{4}<=x<={5}".format(round(self.tabla[i][5],redondeo), round(self.tabla[i][6],redondeo), round(self.tabla[i][7],redondeo), round(self.tabla[i][8],redondeo), round(self.tabla[i][0],redondeo), round(self.tabla[i+1][0],redondeo)))

        nombre = "Eb2"
        for i in range(tamaño-1):
            print(str(nombre+str(i)+"(x)="+polinomios[i]),end='\n')
            #print(polinomioscorrectos[i])

        print(DataFrame(self.tabla,columns=self.cabecera))
        #print("-16.25397(x-3.97)^3+0(x-3.97)^2+-0.87915(x-3.97)+4.16\n 47.51304(x-4.1)^3+-6.33905(x-4.1)^2+-1.70323(x-4.1)+4.01\n-81.41516(x-4.19)^3+6.48947(x-4.19)^2+-1.68969(x-4.19)+3.84\n108.66659(x-4.31)^3+-22.81998(x-4.31)^2+-3.64935(x-4.31)+3.59")
        #,[10.53,1.61]

x = curva([[10.15,.18],[10.19,0.29],[10.2,0.3399]])