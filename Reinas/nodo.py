import numpy as np
class Nodo:
    __costo=0# cantidad de reinas chocadas
    __arreglo=None
    __tamano=0
    __posicion=0
    __sigD=None
    __sigI=None
    def __init__(self,n,pos=-1):
        self.__costo=0
        self.__arreglo=np.full(n,-1)
        self.__tamano=0
        self.__posicion=pos
        self.__sigD=None
        self.__sigI=None
    def setDer(self,nodo):
        self.__sigD=nodo
    def setIzq(self,nodo):
        self.__sigI=nodo
    def getArray(self):
        return self.__arreglo
    def getX(self):
        return self.__posicion
    def getY(self):
        return self.__arreglo[self.__posicion]
    def getCosto(self):
        return self.__costo
    def setCosto(self,costo):
        self.__costo=costo
    def Costo(self,nivel,x,y):
        colision=0
        if nivel > 1:
            for i in range(self.__tamano):
                if self.__arreglo[i]!=-1:
                    j=self.__arreglo[i]
                    if abs(x+y) != abs(i+j) and abs(x-y) != abs(i-j) and y != self.__arreglo[i]  and x!= i: #diagonal positiva, diagonal negativa, fila, columna
                        pass
                    else:
                        colision+=1
        return colision

