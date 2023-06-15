# Proyecto Algoritmos II / 13996 Lopez Gabriel - 14000 Martins Ezequiel
# Graph Functions
import sys

class GraphNode:
    vertex = None
    adjlist = None
    inclist = None
    personDistance = None
    nearestNode = None

# Dijkstra
# https://docs.python.org/3/tutorial/datastructures.html
# https://docs.google.com/presentation/d/17RmIqIXapr5MT4IAtGogUHTNDhalCNlFpQBBlJBlICc/edit?usp=sharing
# https://youtu.be/nlY-ITslQOg // https://youtu.be/TuANaQb2_Gc
# CAMBIAR TODOS LOS ADJLIST POR INCLIST PARA QUE FUNCIONE LA BUSQUEDA DE DISTANCIA
def searchKeyInList(v, key):
    for list in v.adjlist: # Buscar en la lista adjlist
        try:
            if isinstance(list.index(key,0,1), int):    # Devuelve el indice donde esta la key del vertice y lo convierte en valor logico
                return list
        except:
            pass
def initRelax(G, s):    # Revisar que arranque
    for v in G:     # Por cada vertice del grafo
        v.personDistance = sys.maxsize
        v.nearestNode = None
    s.personDistance = 0
def relax(u, v):
    vInu = searchKeyInList(u, v.vertex)
    if v.personDistance > (u.personDistance + u.adjlist[u.adjlist.index(vInu)][1]):
        v.personDistance = u.personDistance + u.adjlist[u.adjlist.index(vInu)][1]
        v.nearestNode = u
        # print("Peso:", v.personDistance)    ##### PRINT DE PRUEBA
def minQueue(G):        # REVISAR QUE ESTA FUNCIÓN FUNCIONA // https://youtu.be/ClO1hGrA2UY
    Q = []
    for i in range(0, len(G)):
        Q.append(G[i])
    Q.sort(key=lambda x:x.personDistance)
    return Q

def dijkstra(G, snode):  # Dijkstra REVISAR Y VER SI FUNCIONA
    initRelax(G, snode)
    S = []
    Q = minQueue(G)
    while len(Q) > 0:
        Q = minQueue(Q)
        u = Q[0]
        Q.pop(0)
        S.append(u)
        for v in u.adjlist: # Revisar para hacer más legible esto
            if v not in S:
                for node in G:
                    if v[0] == node.vertex:
                        vnode = node
                # print("Relajando el nodo:", vnode.vertex) ##### PRINT DE PRUEBA
                relax(u, vnode)
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
    v.adjlist = []
node1.adjlist.append([2, 8])
node2.adjlist.append([1, 8])
node2.adjlist.append([3, 4])
node2.adjlist.append([6, 6])
node2.adjlist.append([4, 6])
node3.adjlist.append([6, 3])
node4.adjlist.append([5, 8])
node5.adjlist.append([6, 4])
node6.adjlist.append([2, 6])
dijkstra(graph, node1)
print("Distancia nodo1 al nodo: ", node1.personDistance)
print("Distancia nodo2 al nodo: ", node2.personDistance)
print("Distancia nodo3 al nodo: ", node3.personDistance)
print("Distancia nodo4 al nodo: ", node4.personDistance)
print("Distancia nodo5 al nodo: ", node5.personDistance)
print("Distancia nodo6 al nodo: ", node6.personDistance)
# print("Distancia nodo6 al nodo6: ", node6.personDistance)