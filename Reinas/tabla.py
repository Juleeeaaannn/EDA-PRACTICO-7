import numpy as np
from nodo import Nodo
class Arbol:
    __tamano=0
    __LNV=[]#lista de nodos vivos
    __raiz=None 
    def __init__(self,n):
        self.__raiz=None
        self.__tamano=n
        x=self.reinas(self.__raiz,0)
    def reinas(self, nodo, nivel):
        if nivel==0: #tabla vacia
            self.__raiz=Nodo(self.__arreglo,self.__tamano*self.__tamano)
            self.reinas(self.__raiz,nivel+1) 
                
        elif nivel < self.__tamano:
            a=self.Beneficio()
            if not self.choca(a):
                self.__arreglo[a.getX()][nivel]=1
                
    def Beneficio(self):
        max=0
        indice = 0
        for i in range(len(self.__LNV)):
            if max<self.__LNV[i].getCosto():
                max=self.__LNV[i].getCosto()
                indice = i
        self.__LNV[indice]=None
        return max