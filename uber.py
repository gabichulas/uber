from graph import *
import pickle as pk
import sys
from map import createMap

class GraphNode:
    vertex = None
    adjlist = None

class Street:
    adjlist = None
    long = None

def serializationEA(archivo):
    with open(archivo) as file:
        E = file.readline()
        A = file.readline()  
    with open('uber\mapapk.pkl', "wb") as pickle_file:
        pk.dump(E, pickle_file)
        pk.dump(A, pickle_file)
    mapa_creado = createMap('uber\mapapk.pkl')
    return mapa_creado

if sys.argv[1] == "-create_map":
    try:
        map_resultado = serializationEA(sys.argv[2])
    except IndexError:
        print("Parametro no permitido")
