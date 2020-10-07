## Esto define una clase para los estados de las listas
class Edo:
    def __init__(self,nombre,padre,g,h,f):
        self.nombre=nombre
        self.padre=padre 
        self.g=g 
        self.h=h 
        self.f=f

## Esto define a la funcion miembro
def miembro(edo,lista): 
    resp=False
    cuenta =0
    donde=-1 
    adentro=False
    for nodo in lista:
        if nodo.nombre==edo: 
            donde=cuenta 
            adentro=True
            break
        cuenta=cuenta+1 
    return adentro ,donde

## Esto define la funcion para expandir la lista Abiertos
def expandir(actual,meta,proble,dlr,Abiertos,Cerrados): 
    hijos=proble[actual.nombre]
    for hijo in hijos:
        mC,_=miembro(hijo,Cerrados) 
        mA,pA=miembro(hijo,Abiertos) 
        if not mC:
            gnue=(actual.g+dlr[actual.nombre][hijo]) 
            hnue=dlr[hijo][meta]
            fnue=gnue+hnue
            if mA: 
                fori=Abiertos[pA].f 
                if fnue<fori:
                    Abiertos[pA]=Edo(hijo,actual.nombre,gnue,hnue,fnue)
            else:
                Abiertos.append(Edo(hijo,actual.nombre,gnue,hnue,fnue))
    return Abiertos
## Esta es la funcion para extraer el siguiente estado a visitar
def siguiente(Abiertos):
    fmejor =100
    mejor=None
    donde=-1
    cuenta =0
    for nodo in Abiertos:
        if nodo.f<fmejor:
            mejor=nodo 
            fmejor=nodo.f 
            donde=cuenta
        cuenta=cuenta+1 
    del Abiertos[donde] 
    return Abiertos ,mejor
## Esto implementa la busuqeda a estrella
def astar(ini,meta,proble,dlr): 
    Abiertos=[Edo(ini,ini,0,dlr[ini][meta],dlr[ini][meta])] 
    Cerrados =[]
    listo=False
    while not listo:
        Abiertos ,actual=siguiente(Abiertos) 
        if actual.nombre==meta:
            listo=True 
            Cerrados.append(actual)
        else:
            Cerrados.append(actual) 
            Abiertos=expandir(actual,meta,proble,dlr,Abiertos,Cerrados)
    return Cerrados
## Esto forma el camino a partir de loq ue tiene Cerrados
def getCamino(ini,Cerrados): 
    resp =[]
    actual=Cerrados[-1].nombre 
    listo=False
    while not listo:
        if actual==ini:
            listo=True
            resp.insert(0,actual) 
        else:
            for nodo in Cerrados:
                if nodo.nombre==actual: 
                    resp.insert(0,actual) 
                    actual=nodo.padre 
                    break
    return resp
    
## Esta es la funcion principal del programa
def main(ini,meta): 
    proble={'A':['B','C','D'],
            'B':['A','C','E'],
            'C':['A','B','D','E','G'],
            'D':['A','C','F','G'],
            'E':['B','C','F','G'],
            'F':['D','E', 'G'],
            'G':['D','C','E','F']}

    dlr={'A':{'A':0,'B':5,'C':8,'D':7,'E':13,'F':32,'G':18},
        'B':{'A':5,'B':0,'C':9,'D':14,'E':8,'F':35,'G':19}, 
        'C':{'A':8,'B':9,'C':0,'D':6,'E':7,'F':26, 'G':8}, 
        'D':{'A':7,'B':14,'C':6,'D':0,'E':16,'F':27, 'G': 12}, 
        'E':{'A':13,'B':8,'C':7,'D':16,'E':0,'F':35,'G':15}, 
        'F':{'A':32,'B':35,'C':26,'D':27,'E':35,'F':0,'G':15},
        'G':{'A':18,'B':19,'C':8,'D':12,'E':15,'F':15,'G':0}}
    cerrados=astar(ini,meta,proble,dlr) 
    camino=getCamino(ini,cerrados)
    print('La solucion segun la busqueda A* es:') 
    print(camino)
    ## Este es el punto de entrada al programa
if __name__=="__main__": 
    print("NODO DE INICIO:")
    ini= input()
    print("NODO META:")
    fin= input()
    main(ini,fin)