# Proyecto Algoritmos II / 13996 Lopez Gabriel - 14000 Martins Ezequiel
import sys
from graph import *

class GraphNode:
    vertex = None
    adjlist = None
    inclist = None
    personDistance = None
    nearestNode = None

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