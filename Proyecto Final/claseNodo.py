import numpy as np

class Nodo:
    __arreglo = None #arreglo posee la reina
    __dimension = None #dimension del arreglo
    __pos = None #coordenadas reina
    __ult=0

    def __init__ (self, cant, x=None, y=None):
        self.__dimension = cant
        self.__arreglo = np.full(cant, -1)
        self.__pos=[]
        if x != None and y != None:
            self.__pos.append(x)
            self.__arreglo[x]=y

    def setReina(self,x,y):
        self.__pos.append(x)
        self.__arreglo[x]=y
        self.__ult+=1
    def getReinas(self):
        return self.__pos
    def getX(self):
        if self.__pos != None:
            return self.__pos[self.__ult]
    
    def getY(self):
        if self.__pos!= None:
            return self.__arreglo[self.__pos[self.__ult]]
    def choca(self,reina): #trae solo una reina
        choca=0
        if len(reina.getReinas()) >= 1:
            for x in self.__pos:
                if abs(x+self.__arreglo[x]) != abs (reina.getX()+reina.getY()) and abs(x-self.__arreglo[x]) != abs(reina.getX()-reina.getY()):#diagonales
                            if x != reina.getX() and self.__arreglo[x] != reina.getY():#vertical y horizontal
                                pass
                            else:
                                choca+=1
                else:
                    choca +=1
            return choca
        else:
            return choca

  

    def Colision(self,reina):
        if self.__pos != None and len(reina) > 1:    
            choca=0
            for x in self.__pos:
                for i in range(0,3): #recorro la lista de reinas
                    if reina[i].getX() != None and reina[i].getY() != None:
                        if abs(x+self.__arreglo[x]) != abs (reina[i].getX()+reina[i].getY()) and abs(x-self.__arreglo[x]) != abs(reina[i].getX()-reina[i].getY()):#diagonales
                            if x != reina[i].getX() and self.__arreglo[x] != reina[i].getY():#vertical y horizontal
                                pass
                            else:
                                choca+=1
                        else:
                            choca +=1
            return choca
        else:
            retorna=0
            return retorna