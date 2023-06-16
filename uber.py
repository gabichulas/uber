from graph import *
import pickle as pk
import sys
import os
from random import *
from map import createMap

# Hashtable Functions // https://planetmath.org/goodhashtableprimes
# Prime numbers: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61
# Powers of 2:   2  4   8     16            32                    64 

ubiPickle = "pk_ubicaciones.pkl"
ubiMovPickle = "pk_ubicaciones_mov.pkl"
mapPickle = "mapapk.pkl"

class GraphNode:
    vertex = None
    adjlist = None
    inclist = None
    personDistance = None
    nearestNode = None

class DictionaryElement: # HashFunction (There are 9, H A T S E K I P C, use any prime higher than 9*3=27) // Example: H11 / P6 / C12
    key = None
    value = None
    monto = None

def loadHash(D):
    for i in range(0,7):
        D.append([])
    return D

def insert(D, key, value, monto):
    if D == []:
        loadHash(D)
    position = ord(key[0]) % 7
    newElement = DictionaryElement()
    newElement.key = key
    newElement.value = value
    if monto != None:
        newElement.monto = monto
    D[position].append(newElement)
    return D

def search(D, key):
    position = ord(key[0]) % 7
    element = D[position]
    if D[position] == None:
        return None
    else:
        for nodo in element:
            if nodo.key == key:
                return nodo
        return None

def createLocationNotExisting(L, D):
    if L == []:
        return D
    key = L[0]
    value = L[1] 
    if len(L) > 2:
        monto = int(L[2])
    else:
        monto = None                                 
    insert(D, key, value,monto)
    return D


def serializationEA(archivo):
    with open(archivo) as file:
        E = file.readline()
        A = file.readline()
    if '{' in E and '{' in A:      # Cambio del formato de los datos en caso de que sean incompatibles con el algoritmo
        E = E.replace("{", "[")    # Esto garantiza que los datos sean manipulables de forma fácil en caso de que
        E = E.replace("}", "]")    # los datos estén estructurados de la forma indicada en el PDF.
        E = E.replace("e", "")
        E = E.replace("E", "")
        E = E.replace("=", "")
        A = A.replace("<", "(")
        A = A.replace(">", ")")
        A = A.replace("{", "[")
        A = A.replace("}", "]")
        A = A.replace("e", "")
        A = A.replace("A", "")
        A = A.replace("=", "")
    with open(archivo, 'w') as fl:
        fl.write(E)
        fl.write(A) 
    with open(mapPickle, "wb") as pickle_file:
        pk.dump(E, pickle_file)
        pk.dump(A, pickle_file)
    mapa_creado = createMap(mapPickle)
    return mapa_creado

def serializationL(archivo,dict):
    with open(archivo, "wb") as file:
        pk.dump(dict,file)

def deserializate(archivo,dict):
    with open(archivo, "rb") as file:
        dict = pk.load(file)
    return dict

def existPathUber(v,u,hash1,hash2,map):
    v = search(hash1,str(v))
    u = search(hash2,str(u))
    if existPath(v.value[1][0],u.value[0][0],map): return True
    elif existPath(v.value[0][0],u.value[1][0],map): return True
    elif existPath(v.value[1][0],u.value[1][0],map): return True
    elif existPath(v.value[0][0],u.value[1][0],map): return True
    else: return False

def emptyfile(archivo):
    with open(archivo, 'rb') as file:
        if file.readline() == None:
            return True
    return False

def createFD(nombre, direccion, hash):
    if '<' in direccion:
        direccion = direccion.replace("<", "(")
        direccion = direccion.replace(">" , ")")
        direccion = direccion.replace(" ", ",")
        direccion = direccion.replace("e", "")
        direccion = eval(direccion)
    dir = []
    dir.append(str(nombre))
    dir.append(direccion)
    hash = createLocationNotExisting(dir,hash)
    return hash

def createMD(nombre, direccion, monto, hash):
    direccion = direccion.replace("<", "(")
    direccion = direccion.replace(">" , ")")
    direccion = direccion.replace(" ", ",")
    direccion = direccion.replace("e", "")
    direccion = eval(direccion)
    dir = []
    dir.append(str(nombre))
    dir.append(direccion)
    dir.append(monto)
    hash = createLocationNotExisting(dir,hash)
    return hash

# Dijkstra Uber
def searchKeyIncList(v, key):
    for list in v.inclist: 
        try:
            if isinstance(list.index(key,0,1), int):
                return list
        except:
            pass
def initRelax(G, s):
    for v in G:
        v.personDistance = sys.maxsize
        v.nearestNode = None
    s.personDistance = 0
def relax(u, v):
    vInu = searchKeyIncList(u, v.vertex)
    if v.personDistance > (u.personDistance + u.inclist[u.inclist.index(vInu)][1]):
        v.personDistance = u.personDistance + u.inclist[u.inclist.index(vInu)][1]
        v.nearestNode = u
def minQueue(G):
    Q = []
    for i in range(0, len(G)):
        Q.append(G[i])
    Q.sort(key=lambda x:x.personDistance)
    return Q
def dijkstra(G, snode):
    initRelax(G, snode)
    S = []
    Q = minQueue(G)
    while len(Q) > 0:
        Q = minQueue(Q)
        u = Q[0]
        Q.pop(0)
        S.append(u)
        for v in u.inclist:
            if v not in S:
                for node in G:
                    if v[0] == node.vertex:
                        vnode = node
                relax(u, vnode)

# Choose vertex
def searchKeyAdjList(v, key):
    for list in v.adjlist: 
        try:
            if isinstance(list.index(key,0,1), int):
                return True
        except:
            pass
    return False
def chooseVertex(G, value, variant): # variant debe ser 0 para Dijkstra o 1 para BFS
    v = value[0]    # [vertex1, distance1]
    u = value[1]    # [vertex2, distance2]
    useV = None
    useU = None
    for n in G:
        if n.vertex == v[0]:
            if searchKeyAdjList(n, u[0]): # Existe conexion de V -> U
                useV = n
        if n.vertex == u[0]:
            if searchKeyAdjList(n, v[0]): # Existe conexion de U -> V
                useU = n
    if useV != None and useU != None:
        if v[1] > u[1]:
            if variant == 0:
                return useU
            else:
                return useV
        else:
            if variant == 0:
                return useV
            else:
                return useU
    elif useV != None:
        if variant == 0:
            return useV
        else:
            return useU
    else:
        if variant == 0:
            return useU
        else:
            return useV

def calculatePrice(persona,autos,ubiM):
    persona = search(ubiM, persona)
    for node in autos:
        if (search(ubiM,node[0]).monto+node[1])/4 > persona.monto:
            autos.pop(node)
    return autos


def decision(rank,var):
    choose = str(input("Por favor, elija el auto que prefiera: ")).upper()
    for i in range(0,len(rank)):
            if rank[i][0].upper() == choose:
                var = i
                return choose, var
    return decision(rank, var)

def interface(persona, direccion, ranking, ubiF, ubiM):
    var = 0
    print("-------------------- * --------------------\n")
    print(f"---------- Bienvenido {persona}. ----------\n")
    print("------- Este es el ranking de sus autos mas cercanos: -------")
    ranking = ranking[0:3]
    for i in ranking:
        print(f"El auto {i[0]} se encuentra a {i[1]} metros de usted.")
    auto, var = decision(ranking,var)
    print(f"\nFelicidades! usted ha elegido el vehiculo {auto}.")
    choose1 = str(input("¿Acepta el viaje?\nY/N: ")).lower()
    while choose1 != "y" and choose1 != "n":
        choose1 = str(input("Respuesta invalida. Intente de nuevo.\nY/N: ")).lower()
    if choose1 == "n":
        print("Gracias por viajar con nosotros!")
    elif choose1 == "y":
        car = search(ubiM,auto)
        person = search(ubiM, persona)
        destino = search(ubiF, direccion).value
        person.value = destino
        person.monto = person.monto - (car.monto+ranking[var][1])/4
        car.value = destino
        print(f"Gracias por viajar con nosotros! Su nuevo monto es: {person.monto}")





def calculateDistance(graph, carList, person):
    distanceCarList = []
    nodeP = chooseVertex(graph, person.value, 0)
    for list in person.value:
            if list[0] == nodeP.vertex:
                distanceCar = list[1]
    for listx in carList: # list[0] key, list[1] distancia
        nodeC = chooseVertex(graph, listx.value, 0)
        for lista in listx.value:
            if lista[0] == nodeC.vertex:
                distanceCar = distanceCar + nodeC.personDistance + lista[1]
        distanceCarList.append([listx.key, distanceCar])
    return distanceCarList


if sys.argv[1] == "-create_map":
    try:
        if os.path.exists(mapPickle):
            print("Ya hay un mapa creado!. Estas seguro de que queres crear otro? Esto puede ocasionar fallas al cargar direcciones incompatibles.")
            decision = input("Y/N: ")
            if decision == "Y".lower(): 
                print("Tu mapa está siendo creado...")
                map_resultado = serializationEA(sys.argv[2])
                print("Mapa creado correctamente.")
            if decision == "N".lower(): print("Gracias. Podes intentar agregando ubicaciones nuevas.")
        else:
            print("Tu mapa está siendo creado...")
            map_resultado = serializationEA(sys.argv[2])
            print("Mapa creado correctamente.")
    except IOError:
        print("Parametro no permitido")
        print("CREACIÓN DEL MAPA FALLIDA.")
    except SyntaxError:
        print("El archivo no está permitido. Intente de nuevo.")
        print("CREACIÓN DEL MAPA FALLIDA.")

if sys.argv[1] == "-load_fix_element":
    try:
        if not os.path.exists(mapPickle):
            print("ERROR. No hay un mapa cargado. Intenta de nuevo.")
        else:
            map = createMap(mapPickle)
            ubicaciones = [] 
            if not os.path.exists(ubiPickle) :
                print("")
            else:
                if not emptyfile(ubiPickle):
                    ubicaciones = deserializate(ubiPickle,ubicaciones)
            for nodes in ubicaciones:
                for element in nodes:
                    if element.key == str(sys.argv[2]):
                        print("La ubicación ya existe. Intenta dándole otro nombre.")
                        exit()
            if sys.argv[3][0] == "<":
                ubicaciones = createFD(sys.argv[2], sys.argv[3],ubicaciones)
                serializationL(ubiPickle, ubicaciones)
                print("La ubicacion ha sido agregada.")
            else:
                print("Parametro no permitido")
                print("CREACIÓN DE DIRECCION FALLIDA")
    except IOError:
        print("Parametro no permitido")
        print("CREACIÓN DE DIRECCION FALLIDA")
    except SyntaxError:
        print("El archivo no está permitido. Intente de nuevo.")
        print("CREACIÓN DE DIRECCION FALLIDA")

if sys.argv[1] == "-load_movil_element":
    try:
        if not os.path.exists(mapPickle):
            print("ERROR. No hay un mapa cargado. Intenta de nuevo.")
        else:
            map = createMap(mapPickle)
            ubicaciones = [] 
            if not os.path.exists(ubiMovPickle):
                print("")
            else:
                if not emptyfile(ubiMovPickle):
                    ubicaciones = deserializate(ubiMovPickle,ubicaciones)
            for nodes in ubicaciones:
                for element in nodes:
                    if element.key == str(sys.argv[2]):
                        print("La ubicación ya existe. Intenta dándole otro nombre.")
                        exit()
            if sys.argv[3][0] == "<":
                ubicaciones = createMD(sys.argv[2], sys.argv[3], sys.argv[4],ubicaciones)
                serializationL(ubiMovPickle, ubicaciones)
                print("La ubicacion ha sido agregada.")
            else:
                print("Parametro no permitido")
                print("CREACIÓN DE DIRECCION FALLIDA")
    except IOError:
        print("Parametro no permitido")
        print("CREACIÓN DE DIRECCION FALLIDA")
    except SyntaxError:
        print("El archivo no está permitido. Intente de nuevo.")
        print("CREACIÓN DE DIRECCION FALLIDA")


if sys.argv[1] == "-create_trip":
    try:
        if not os.path.exists(mapPickle):
            print("ERROR. No hay un mapa cargado. Intenta de nuevo.")
        elif not os.path.exists(ubiMovPickle):
            print("ERROR. Por favor, carga ubicaciones moviles.")
        elif not os.path.exists(ubiPickle):
            print("ERROR. Por favor, carga ubicaciones fijas.")
        else:
            map = createMap(mapPickle)
            ubiF = []
            ubiM = []
            with open(ubiPickle, "rb") as ubis:
                ubiF = deserializate(ubiPickle, ubiF)
            with open(ubiMovPickle, "rb") as ubisM:
                ubiM = deserializate(ubiMovPickle, ubiM)
            if sys.argv[3][0] == "<":
                sys.argv[3] = sys.argv[3].replace("<", "(")
                sys.argv[3] = sys.argv[3].replace(">", ")")
                sys.argv[3] = sys.argv[3].replace("e", "")
                sys.argv[3] = sys.argv[3].replace(" ", ",")
                sys.argv[3] = eval(sys.argv[3])
                newDirection = createFD("X1",sys.argv[3],ubiF)
                if existPathUber(sys.argv[2],newDirection[ord("X")%7][0].key, ubiM, ubiF,map):
                    dijkstra(map, chooseVertex(map, search(ubiM, sys.argv[2]).value,0))
                    distance = calculateDistance(map, ubiM[ord("C") % 7], search(ubiM, sys.argv[2]))
                    carRanking = sorted(distance, key=lambda x:x[1])
                    carRanking = calculatePrice(sys.argv[2], carRanking, ubiM)
                    interface(sys.argv[2], "X1", carRanking,ubiF,ubiM)
            else:
                if existPathUber(sys.argv[2], sys.argv[3], ubiM, ubiF,map):
                    dijkstra(map, chooseVertex(map, search(ubiM, sys.argv[2]).value,0))
                    distance = calculateDistance(map, ubiM[ord("C") % 7], search(ubiM, sys.argv[2]))
                    carRanking = sorted(distance, key=lambda x:x[1])
                    carRanking = calculatePrice(sys.argv[2], carRanking, ubiM)
                    interface(sys.argv[2], sys.argv[3], carRanking,ubiF,ubiM)

    except IOError:
        print("Parametro no permitido")
        print("CREACIÓN DE DIRECCION FALLIDA")
    except SyntaxError:
        print("El archivo no está permitido. Intente de nuevo.")
        print("CREACIÓN DE DIRECCION FALLIDA")