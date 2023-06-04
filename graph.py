from random import *
from linkedlist import *
from myqueue import *

class GraphNode:
    vertex = None
    adjacentvertex = None
    color = None
    parent = None
    distance = None
    time = None


def createGraph(V,A):
    graph = []
    if len(V)>0 and len(A)>0:
        for i in range(0,len(V)):
            newNode = GraphNode()
            newNode.vertex = V[i]
            newNode.adjacentvertex = []
            graph.append(newNode)
        
        for j in range(len(A)):
            for k in range(len(graph)):
                if A[j][0] == graph[k].vertex:
                    graph[k].adjacentvertex.append(A[j][1])
                elif A[j][1] == graph[k].vertex:
                    graph[k].adjacentvertex.append(A[j][0]) 
    return graph

def createGraphUber(V,A):
    graph = []
    if len(V)>0 and len(A)>0:
        for i in range(0,len(V)):
            newNode = GraphNode()
            newNode.vertex = V[i]
            newNode.adjlist = []
            graph.append(newNode)
        
        for j in range(len(A)):
            for k in range(len(graph)):
                if A[j][0] == graph[k].vertex:
                    graph[k].adjlist.append(A[j][1])
                elif A[j][1] == graph[k].vertex:
                    graph[k].adjlist.append(A[j][0]) 
    return graph

def searchVertex(graph,v):
    for i in range(len(graph)):
        if graph[i].vertex == v:
            return graph[i]
    return None

def searchVertexIndex(graph,v):
    for i in range(len(graph)):
        if graph[i].vertex == v:
            return i
    return None

def numberOfEdges(graph):
    grades = 0
    for i in range(len(graph)):
        grades += len(graph[i].adjacentvertex)
    return grades/2

def isInList(list,object):
    for node in range(len(list)):
        if list[node] == object:
            return True
        
############################################################

def existPath(v1,v2,graph):
    vertex1 = searchVertex(graph,v1)
    vertex2 = searchVertex(graph,v2)
    visited = []
    queue = LinkedList()
    return existPathR(vertex2,graph,vertex1,visited,queue)

def existPathR(v2,graph,pivot,list,q):
    if len(pivot.adjacentvertex) > 0:
        list.append(pivot.vertex)
        for adj in range(len(pivot.adjacentvertex)):
            if pivot.adjacentvertex[adj] == v2.vertex:
                return True
            elif not isInList(list,pivot.adjacentvertex[adj]):
                enqueue(q,pivot.adjacentvertex[adj])
        while q.head != None:
            newPivot = searchVertex(graph,dequeue(q))
            newQueue = LinkedList()
            return existPathR(v2,graph,newPivot,list,newQueue)
    return False


def isConnected(graph):
    for i in range(len(graph)):
        for j in range(len(graph)):
            if i==j:
                continue
            elif not existPath(graph[i].vertex,graph[j].vertex,graph):
                return False
    return True

def isTree(graph):
    if isConnected(graph):
        if numberOfEdges(graph) == len(graph) - 1:
            return True
    return False

def isComplete(graph):
    if isConnected(graph):
        for v in graph:
            if not (len(v.adjacentvertex) == len(graph) - 1):
                return False
        return True
    return False

def convertTree(graph):
    tree_edges = []
    visited = []
    cola = LinkedList()
    for i in range(0,len(graph)):
        visited.append(graph[i].vertex)
        enqueue(cola,graph[i])
        while cola != None:
            currentnode = dequeue(cola)
            for j in range(0,len(currentnode.adjacentvertex)):
                if len(currentnode.adjacentvertex) > 0:
                    if currentnode.adjacentvertex[j] not in visited:
                        vecino = graph[searchVertexIndex(graph,currentnode.adjacentvertex[j])]
                        visited.append(currentnode.adjacentvertex[j])
                        enqueue(cola,vecino)
                    else:
                        if searchinq(cola,currentnode.adjacentvertex[j]) == False:
                            graphcopy = graph
                            indexvecino = searchVertexIndex(graph,currentnode.adjacentvertex[j])
                            indexcurrentnode = searchVertexIndex(graph,currentnode.vertex)
                            graphcopy[indexcurrentnode].adjacentvertex.remove(currentnode.adjacentvertex[j])
                            graphcopy[indexvecino].adjacentvertex.remove(currentnode.vertex)
                            if isTree(graphcopy) == True:
                                tree_edges.append([currentnode.vertex,vecino.vertex])
    return tree_edges    

def searchinq(q,value):
    currentnode = q.head
    while currentnode != None:
        if currentnode.value == value:
            return True
        currentnode = currentnode.nextNode
    return False  

def countConnections(graph):
    visited = []
    comps = 0
    for node in graph:
        if node.vertex not in visited:
            BFS(graph,node,visited)
            comps += 1
    return comps

def BFS(graph,node,visited):
    visited.append(node.vertex)
    for j in range(0,len(node.adjacentvertex)):
        if node.adjacentvertex[j] not in visited:
            vecino = searchVertex(graph,node.adjacentvertex[j])
            BFS(graph,vecino,visited)

def convertToBFSTree(graph, v):
    if not isConnected(graph):
        return print("El grafo no es conexo, no se puede aplicar la operacion.")
    for node in graph:
        node.color = "White"
        node.distance = 0
    bfslist = []
    v.parent = None
    v.color = "Grey"
    q = LinkedList()
    enqueue(q,v)
    while q.head != None:
        current = dequeue(q)
        adjlist = []
        for i in current.adjacentvertex:
            neighbor = searchVertex(graph,i)
            if neighbor.color == "White":
                adjlist.append(neighbor.vertex)
                neighbor.color = "Grey"
                neighbor.distance = current.distance + 1
                neighbor.parent = current
                enqueue(q,neighbor)
        newNode = GraphNode()
        newNode.vertex = current.vertex
        newNode.adjacentvertex = adjlist
        bfslist.append(newNode)
        current.color = "Black"
    return bfslist

def convertToDFSTree(graph,v):
    for node in graph:
        node.color = "White"
    dfslist = []
    time = 0
    DFSR(graph,v,dfslist,time)
    for vert in graph:
        if vert.color == "White":
            DFSR(graph,vert,dfslist,time)
    return list(reversed(dfslist))



def DFSR(graph,v,dfslist,time):
    adjlist = []
    node = GraphNode()
    node.vertex = v.vertex
    node.adjacentvertex = adjlist
    if v.parent != None:
        adjlist.append(v.parent.vertex)
    time += 1
    v.color = "Grey"
    v.distance = time
    for i in v.adjacentvertex:
        neighbor = searchVertex(graph, i)
        if neighbor.color == "White":
            neighbor.parent = v
            adjlist.append(neighbor.vertex)
            DFSR(graph,neighbor,dfslist,time)
    time += 1
    v.time = time
    v.color = "Black"
    node.adjacentvertex = adjlist
    dfslist.append(node)

def bestRoad(graph,v1,v2):
    for i in range(0,len(graph)):
        graph[i].color = "White"
        graph[i].distance = 0
    v1.color = "Grey"
    queue = LinkedList()
    enqueue(queue,v1)
    road = []
    while queue.head != None:
        currentnode = dequeue(queue)
        road.append(currentnode.vertex)
        for j in currentnode.adjacentvertex:
            neighbor = searchVertex(graph,j)
            if neighbor.vertex == v2.vertex:
                road.append(v2.vertex)
                return road
            if neighbor.color == "White":
                neighbor.color = "Grey"
                neighbor.distance = currentnode.distance + 1
                neighbor.parent = currentnode
                enqueue(queue,neighbor)
        currentnode.color = "Black"
    return road

