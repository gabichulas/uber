# Proyecto Algoritmos II / 13996 Lopez Gabriel - 14000 Martins Ezequiel
# Graph Functions
import sys
from graph import *

class GraphNode:
    vertex = None
    adjlist = None
    inclist = None
    personDistance = None
    nearestNode = None

# Dijkstra uber
# https://docs.python.org/3/tutorial/datastructures.html
# https://docs.google.com/presentation/d/17RmIqIXapr5MT4IAtGogUHTNDhalCNlFpQBBlJBlICc/edit?usp=sharing
# https://youtu.be/nlY-ITslQOg // https://youtu.be/TuANaQb2_Gc // https://youtu.be/ClO1hGrA2UY
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
def chooseVertex(G, value):
    v = value[0]    # [vertex1, distance1]
    u = value[1]    # [vertex2, distance2]
    useV = None
    useU = None
    for n in G:
        if n.vertex == v[0]:
            if searchKeyAdjList(n, u[0]):
                useV = n
        if n.vertex == u[0]:
            if searchKeyAdjList(n, v[0]):
                useU = n
    if useV != None and useU != None:
        if v[1] > u[1]:
            return useU
        else:
            return useV
    elif useV != None:
        return useV
    else:
        return useU
###########################################################
######################### PRUEBAS #########################
###########################################################
node1 = GraphNode()
node1.vertex = 1
node2 = GraphNode()
node2.vertex = 2
node3 = GraphNode()
node3.vertex = 3
node4 = GraphNode()
node4.vertex = 4
node5 = GraphNode()
node5.vertex = 5
node6 = GraphNode()
node6.vertex = 6
graph = []
graph.append(node1) # Añadir nodos al grafo
graph.append(node2)
graph.append(node3)
graph.append(node4)
graph.append(node5)
graph.append(node6)
for v in graph:
    v.adjlist = []
    v.inclist = []
node1.adjlist.append([2, 8])
node2.inclist.append([1, 8])

node2.adjlist.append([1, 8])
node1.inclist.append([2, 8])

node2.adjlist.append([3, 4])
node3.inclist.append([2, 4])

node2.adjlist.append([6, 6])
node6.inclist.append([2, 6])

node2.adjlist.append([4, 6])
node4.inclist.append([2, 6])

node3.adjlist.append([6, 3])
node6.inclist.append([3, 3])

node4.adjlist.append([5, 8])
node5.inclist.append([4, 8])

node5.adjlist.append([6, 4])
node6.inclist.append([5, 4])

node6.adjlist.append([2, 6])
node2.inclist.append([6, 6])

print("----------------------------------------------------------------")
# https://drive.google.com/file/d/1dHKOu7D2CIBiNQBIlEqHl_dGt6Q5J2pN/view?usp=sharing
dijkstra(graph, node3)
print("Distancia al nodo1: ", node1.personDistance)
print("Distancia al nodo2: ", node2.personDistance)
print("Distancia al nodo3: ", node3.personDistance)
print("Distancia al nodo4: ", node4.personDistance)
print("Distancia al nodo5: ", node5.personDistance)
print("Distancia al nodo6: ", node6.personDistance)

# Node1 y Node2, tienen distancia 8
print(chooseVertex(graph, [[1, 2],[2, 6]]).vertex)
print(chooseVertex(graph, [[1, 4],[2, 4]]).vertex)
print(chooseVertex(graph, [[1, 6],[2, 2]]).vertex)