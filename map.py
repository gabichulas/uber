from graph import *
import pickle as pk
import sys
import ast

def changeLines(file):
    with open(file, "r") as f:
        E = f.readline()
        A = f.readline()
    if '{' in E and '{' in A:
        E = E.replace("{", "[")
        E = E.replace("}", "]")
        E = E.replace("e", "")
        A = A.replace("[", "(")
        A = A.replace("]", ")")
        A = A.replace("{", "[")
        A = A.replace("}", "]")
        A = A.replace("e", "")
        with open(file, 'w') as fl:
            fl.write(E)
            fl.write(A)


def createMap(archivo):
    print("Tu mapa está siendo creado...")
    changeLines(archivo)
    with open(archivo, "rb") as pickle_f:
        listaEsquinas = eval(pk.load(pickle_f))
        listaAristas = ast.literal_eval(pk.load(pickle_f))
        map = createGraphUber(listaEsquinas, listaAristas)
        print("Mapa creado correctamente.")
    return map

changeLines("uber\mapExample.txt")