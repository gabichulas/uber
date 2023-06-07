from graph import *
import pickle as pk
import sys
import ast

def createMap(archivo):
    print("Tu mapa está siendo creado...")
    with open(archivo, "rb") as pickle_f:
        listaEsquinas = eval(pk.load(pickle_f))
        listaAristas = ast.literal_eval(pk.load(pickle_f))
        map = createGraphUber(listaEsquinas, listaAristas)
        print("Mapa creado correctamente.")
    return map
