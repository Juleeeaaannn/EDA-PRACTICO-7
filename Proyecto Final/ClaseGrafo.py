import numpy as np

N=4

class Nodo:
    __arreglo = None #arreglo posee la reina
    __dimension = None #dimension del arreglo
    __pos = None #coordenadas reina
    __ult=0 #ulitma reina
    __cota=999
    __sig=None

    def __init__ (self, cant, x=None, y=None):
        self.__dimension = cant
        self.__arreglo = np.full(cant, -1)
        self.__pos=[]
        self.__sig=None
        self.__cota=999
        if x != None and y != None:
            self.__pos.append(x)
            self.__arreglo[x]=y
    def setCota(self,cota):
        self.__cota=cota
    def getCota(self):
        return self.__cota
    def setArray(self,a):
        self.__arreglo=a
    def getArray(self):
        return self.__arreglo
    def setSig(self,elemento):
        self.__sig=elemento
    def setReina(self,x,y):
        self.__pos.append(x)
        self.__arreglo[x]=y
        self.__ult+=1
    def setReinas(self,a):
        self.__pos=a
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

class Grafo: #grafo conexo
    __raiz=None
    __LNV=None #LISTA DE NODOS VIVOS

    def __init__(self):
        self.__LNV=[]
        self.__raiz=None

    def Buscar(self, elemento):
        bandera = True
        i = 0
        while bandera and i < len(self.__vertices):
            if self.__vertices[i] == elemento:
                bandera = False
            else:
                i += 1
        if bandera == False:
            return i
        else:
            return None

    def CrearNodoInicial(self):
        new=Nodo(N,0,0)
        new1=Nodo(N,0,1)
        nuevo=Nodo(N,0,2)
        new3=Nodo(N,0,3)
        self.__LNV.append(new)
        self.__LNV.append(new1)
        self.__LNV.append(nuevo)
        self.__LNV.append(new3)


    def Genera(self,nivel):
        lista=[]
        i=0
        for i in range(N):
                new=Nodo(N,i,nivel)
                lista.append(new)
        return lista

    def BuscarHijo(self,nivel):
        lista=self.Genera(nivel)
        print(lista)
        return lista

    def BuscarLNV(self,elemento):
        i=0
        while(i<len(self.__LNV) and elemento!=self.__LNV[i]):
            i+=1
        if i<len(self.__LNV) and elemento==self.__LNV[i]:
            return i
        else:
            print("No se encontro el elemento en la LNV")

    def Arbol(self):
        k=0
        for nivel in range(1,4):
            for j in self.__LNV:
                    listah=[]
                    print("-------------") 
                    print("nivel:",nivel)
                    print("padre:",j.getX(),j.getY())
                    listaHijos=self.BuscarHijo(nivel)
                    listah.append(self.Asociar(listaHijos,j))
            self.__LNV.pop(self.BuscarLNV(j))
            self.__LNV+=listah

    def Asociar(self,hijos,padre):
        for i in hijos:
            print("hijo;x y:",i.getX(),i.getY(),"colision:",padre.choca(i))
            if i.choca(padre)==0 and i.choca(padre)<=padre.getCota():
                print("nodos vivos",i.getX(),i.getY())
                padre.setReina(i.getX(),i.getY())
                a=Nodo(N)
                nuevo=self.Copiar(a,i)
                return padre
    def Copiar(self,A,B):
        A.setArray(B.getArray())
        A.setReinas(B.getReinas)
    def Mostrar(self):
        for i in self.__LNV:
            print("lista de nodos vivos----------")
            print("(",i.getX(),",",i.getY(),")")
            print("---------------")
        
        
'''
repetir
 elegir el nodo mas prometedor como nodo_E;
 generar todos sus hijos;
 matar el nodo_E;
 para cada hijo hacer
    si colision(hijo) > colision(mejor_solucion_en_curso) 
        entonces se mata
    sino
        si no es solucion 
            entonces se pasa a la lista_de_nodos_vivos
        sino 
            {es solucion: el coste no es estimado sino real}
            es la mejor_solucion_en_curso y se revisa la lista_de_nodos_vivos,
            eliminando los que prometen algo peor
        fsi
    fsi
 fpara
hasta que la lista esta vacia
 '''

if __name__ == '__main__':
    grafo=Grafo()
    grafo.CrearNodoInicial()
    grafo.Arbol()
    