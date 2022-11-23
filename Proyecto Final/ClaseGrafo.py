import numpy as np
from claseNodo import Nodo
N=4
class Grafo: #grafo conexo
    __vertices = None
    __matriz = None
    __LNV=None #LISTA DE NODOS VIVOS

    def __init__(self,vertices=[]):
        self.__vertices=vertices
        self.__LNV=[]
        self.__matriz=np.full(len(vertices),-1)

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
            
    def NodoPrometedor(self,nivel,padre):
        min=99
        for i in self.__vertices:
            if i.getY()==nivel:
                if i.choca(padre) < min: 
                    min = i.Colision(self.__LNV)
                    nodo=i
        return nodo
        
    def BuscarHijo(self,nivel):
        lista=[]
        print("-------hijos--------")
        for i in self.__vertices:
            if i.getY()==nivel:
                print("x:",i.getX(),"y:",i.getY())
                lista.append(i)
        print("--------------")
        return lista

    '''
    def Arbol(self,nivel):
        if nivel < N:
            for j in self.__LNV:
                print("nivel:",nivel)
                listaHijos=self.BuscarHijo(nivel)
                listah=[]
                for i in listaHijos:
                    print("Nodo Hijo",i.choca(j))
                    if i.choca(j) == 0:
                        i.setReina(j.getX(),j.getY())
                        listah.append(i)
            self.__LNV+=listah
            self.Arbol(nivel+1)
        else:
            print(self.Mostrar())
    '''
    def BuscarLNV(self,elemento):
        i=0
        while(i<len(self.__LNV) and elemento!=self.__LNV[i]):
            i+=1
        if i<len(self.__LNV):
            print("i:",i)
            return i
        else:
            print("No se encontro el elemento en la LNV")

    def Arbol(self):
        k=0
        for nivel in range(1,4,+1):
            while k < len(self.__LNV):
                self.__LNV
                j=self.__LNV[0]    
                print("LNV :",self.__LNV)
                print("nivel:",nivel)
                print(j)
                print("padre:",j.getX(),j.getY())
                listaHijos=self.BuscarHijo(nivel)
                listah=[]
                for i in listaHijos:
                    print("grado:",i.choca(j))
                    if i.choca(j)==0:
                        aux=i
                        aux.setReina(j.getX(),j.getY())
                        listah.append(aux)
                self.__LNV.pop(0)
                self.__LNV+=listah

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
    lista=[]
    for i in range(N):
        for j in range(N):
            new=Nodo(N,i,j)
            lista.append(new)
    grafo=Grafo(lista)
    grafo.CrearNodoInicial()
    grafo.Arbol()
    