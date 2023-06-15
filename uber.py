from graph import *
import pickle as pk
import sys
import os
from map import createMap

# Hashtable Functions // https://planetmath.org/goodhashtableprimes
# Prime numbers: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61
# Powers of 2:   2  4   8     16            32                    64 

ubiPickle = "pk_ubicaciones.pkl"
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
    for i in range(0,47):
        D.append([])
    return D

def insert(D, key, value, monto):
    if D == []:
        loadHash(D)
    position = key % 47
    newElement = DictionaryElement()
    newElement.key = key
    newElement.value = value
    if monto != None:
        newElement.monto = monto
    D[position].append(newElement)
    return D

def search(D, key):
    position = key % 47
    element = D[position]
    if D[position] == None:
        return None
    else:
        for nodo in element:
            if nodo.key == key:
                return key
        return None

# Add locations to a Hashtable
def createLocations(LocationList):
    dictionary = DictionaryElement()
    return createLocationsR(LocationList, dictionary)

def createLocationsR(LL, D):
    if LL == []:
        return D
    key = ord(LL[0][0][0:1]) + LL[0][0][1:len(LL[0][0])]    # Change for better management
    value = LL[0][1]                                        # '' '' '' '' '' '' '' '' '' ''
    insert(D, key, value)
    LL = LL.pop(0)
    createLocationsR(LL, D)

def createLocationNotExisting(L, D):
    if L == []:
        return D
    key = ord(L[0][0:1]) + int(L[0][1:len(L[0])])
    value = L[1] 
    if L[2] != None:
        monto = int(L[2])                                    
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

def emptyfile(archivo):
    with open(archivo, 'rb') as file:
        if file.readline() == None:
            return True
    return False

def createFD(nombre, direccion, hash):
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

def createMD(nombre):
    return

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
            if not os.path.exists(ubiPickle):
                with open(ubiPickle, "wb") as ubis:
                    print("")
            else:
                if not emptyfile(ubiPickle):
                    ubicaciones = deserializate(ubiPickle,ubicaciones)
            old = ubicaciones
            ubicaciones = createFD(sys.argv[2], sys.argv[3],ubicaciones)
            serializationL(ubiPickle, ubicaciones)
            print("La ubicacion ha sido agregada.")
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
            if not os.path.exists(ubiPickle):
                with open(ubiPickle, "wb") as ubis:
                    print("")
            else:
                if not emptyfile(ubiPickle):
                    ubicaciones = deserializate(ubiPickle,ubicaciones)
            old = ubicaciones
            ubicaciones = createFD(sys.argv[2], sys.argv[3],ubicaciones)
            serializationL(ubiPickle, ubicaciones)
            print("La ubicacion ha sido agregada.")
    except IOError:
        print("Parametro no permitido")
        print("CREACIÓN DE DIRECCION FALLIDA")
    except SyntaxError:
        print("El archivo no está permitido. Intente de nuevo.")
        print("CREACIÓN DE DIRECCION FALLIDA")