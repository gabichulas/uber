from graph import *
import pickle as pk
import sys
import ast

def createMap(archivo):
    with open(archivo, "rb") as pickle_f:
        listaEsquinas = eval(pk.load(pickle_f))
        listaAristas = ast.literal_eval(pk.load(pickle_f))
        map = createGraphUber(listaEsquinas, listaAristas)
    return map
