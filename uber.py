from graph import *
import pickle as pk

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
    string[len(string)-1] = string[len(string)-1].replace("\n","")
    return string

def strToListofLists(string):
    list = []
    for i in range(len(string)):
        if string[i] == "[":
            j = i
            for k in range(i,len(string)):
                if string[k] != ']':
                    j += 1
                else:
                    break
            subString = string[i+1:j]
            subString = subString.split(",")
            subString[len(subString)-1] = subString[len(subString)-1].replace("\n","")
            list.append(subString)
    return list

map = open('uber\mapExample.txt')
E = map.readline()
A = map.readline()

E = strToList(E)
A = strToListofLists(A)
