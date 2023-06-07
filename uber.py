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
    if '{' in E and '{' in A:      # Cambio del formato de los datos en caso de que sean incompatibles con el algoritmo
        E = E.replace("{", "[")    # Esto garantiza que los datos sean manipulables de forma fácil en caso de que
        E = E.replace("}", "]")    # los datos estén estructurados de la forma indicada en el PDF.
        E = E.replace("e", "")
        A = A.replace("[", "(")
        A = A.replace("]", ")")
        A = A.replace("{", "[")
        A = A.replace("}", "]")
        A = A.replace("e", "")
    with open(archivo, 'w') as fl:
        fl.write(E)
        fl.write(A) 
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
