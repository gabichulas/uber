from graph import *
import pickle as pk
import json

class GraphNode:
    vertex = None
    adjlist = None

class Street:
    adjlist = None
    long = None

def strToList(string):
    string = string.replace("{","")
    string = string.replace("}","")
    string = string.split(",")
    return string

    
map = open('uber\mapExample.txt')
E = map.readline()
A = map.readline()

#newA = eval(A)

#graph = createGraphUber(E,A)

print(strToList(E))