N=4
def RyP(lista=[],nivel=0):
    if nivel < N:
        if Valido(lista,nivel):
            RyP(lista,nivel+1)
        else:
            if lista[nivel]<N-1:
                lista[nivel]+=1
                RyP(lista,nivel)
            else:
                cereo(lista)
                lista[0]+=1
                RyP(lista,0)
    else:
        print(lista)
        Mostrar(lista)

def cereo(lista):
    for i in range(N-1):
        lista[i+1]=0

def Valido(lista,nivel):
    retorna=True
    for i in range(nivel):
        if(lista[i] == lista[nivel]) or (ValAbs(lista[i],lista[nivel])==ValAbs(i,nivel)):
            retorna=False
    return retorna

def ValAbs(x,y):
	if x>y:
		return x - y
	else:
		return y - x
def Mostrar(lista):
    s=""
    for i in range(N):
        for j in range(N):
            if lista[i]==j:
                s+="X"
                s+="\t"
            else:
                s+="-"
                s+="\t"
        s+="\n"
    print(s)
                
print ("#"*24)
print ("LAS N - REINAS")
print ("#"*24)
lista = []
for i in range(N):
	lista.append(0)
nivel = 0
RyP(lista, nivel)