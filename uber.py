# Proyecto Algoritmos II / 13996 Lopez Gabriel - 14000 Martins Ezequiel
# Graph Functions
import sys
from graph import *

class GraphNode:
    vertex = None
    adjlist = None
    inclist = None
    personDistance = []
    nearestNode = []

# Dijkstra uber
# https://docs.python.org/3/tutorial/datastructures.html
# https://docs.google.com/presentation/d/17RmIqIXapr5MT4IAtGogUHTNDhalCNlFpQBBlJBlICc/edit?usp=sharing
# https://youtu.be/nlY-ITslQOg // https://youtu.be/TuANaQb2_Gc
def searchKeyInList(v, key):
    for list in v.inclist: 
        try:
            if isinstance(list.index(key,0,1), int):    # Devuelve el indice donde esta la key del vertice y lo convierte en valor logico
                return list
        except:
            pass
########################################################
def searchDistanceVertexInList(v, key):
    for list in v.personDistance:
        try:
            if isinstance(list.index(key,0,1), int):    
                return True
            else:
                pass
        except:
            pass
    return False
#########################################################
def initRelax(G, s):
    for v in G:
        list1 = [s.vertex, sys.maxsize]
        list2 = [s.vertex, sys.maxsize]
        v.personDistance.append(list1)
        v.nearestNode.append(list2)
    list3 = [s.vertex, 0]
    s.personDistance.append(list3)
def relax(u, v, s):
    vInu = searchKeyInList(u, v.vertex)
    if v.personDistance > (u.personDistance + u.inclist[u.inclist.index(vInu)][1]):
        v.personDistance = u.personDistance + u.inclist[u.inclist.index(vInu)][1]
        v.nearestNode = u

        # print("Peso:", v.personDistance)    ##### PRINT DE PRUEBA

def minQueue(G):
    Q = []
    for i in range(0, len(G)):
        Q.append(G[i])
    Q.sort(key=lambda x:x.personDistance)
    return Q

def dijkstra(G, snode):
    initRelax(G, snode)

    print("Nodo1", G[0].personDistance)  ##### PRINT DE PRUEBA
    print("Nodo2", G[1].personDistance)  ##### PRINT DE PRUEBA
    print("Nodo3", G[2].personDistance)  ##### PRINT DE PRUEBA
    print("Nodo4", G[3].personDistance)  ##### PRINT DE PRUEBA
    print("Nodo5", G[4].personDistance)  ##### PRINT DE PRUEBA
    print("Nodo6", G[5].personDistance)  ##### PRINT DE PRUEBA
    print(snode.personDistance,"HUHU")   ##### PRINT DE PRUEBA

    S = []
    Q = minQueue(G)
    while len(Q) > 0:
        Q = minQueue(Q)
        u = Q[0]
        Q.pop(0)
        S.append(u)
        for v in u.inclist: # Revisar para hacer más legible esto
            if v not in S:
                for node in G:
                    if v[0] == node.vertex:
                        vnode = node
                # print("Relajando el nodo:", vnode.vertex) ##### PRINT DE PRUEBA
                relax(u, vnode, snode)
        # print("-----") ##### PRINT DE PRUEBA

# Testeos grafo
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
    v.inclist = []
node1.inclist.append([2, 8])
node2.inclist.append([1, 8])
node2.inclist.append([3, 4])
node2.inclist.append([6, 6])
node2.inclist.append([4, 6])
node3.inclist.append([6, 3])
node4.inclist.append([5, 8])
node5.inclist.append([6, 4])
node6.inclist.append([2, 6])
print("----------------------------------------------------------------")
dijkstra(graph, node1)
print("Distancia nodo1 al nodo: ", node1.personDistance)
print("Distancia nodo2 al nodo: ", node2.personDistance)
print("Distancia nodo3 al nodo: ", node3.personDistance)
print("Distancia nodo4 al nodo: ", node4.personDistance)
print("Distancia nodo5 al nodo: ", node5.personDistance)
print("Distancia nodo6 al nodo: ", node6.personDistance)
# print("Distancia nodo6 al nodo6: ", node6.personDistance)
# listaBFS = convertToBFSTree(graph,node1)
# print(listaBFS)