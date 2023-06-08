# Proyecto Algoritmos II / 13996 Lopez Gabriel - 14000 Martins Ezequiel
# Graph Functions
class GraphNode:
    vertex = None
    adjlist = None
    color = None
    parent = None

# Hashtable Functions // https://planetmath.org/goodhashtableprimes
# Prime numbers: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61
# Powers of 2:   2  4   8     16            32                    64 
class DictionaryElement: # HashFunction (There are 9, H A T S E K I P C, use any prime higher than 9*3=27) // Example: H11 / P6 / C12
    key = None
    value = None
def insert(D, key, value):
    position = key % 47
    newElement = DictionaryElement()
    newElement.key = key
    newElement.value = value
    if D[position] == None:
        D[position] = [newElement]
    else:
        D[position].append[newElement]
    return D
def search(D, key):
    position = key % 47
    element = D[position]
    if D[position] == None:
        return None
    else:
        for nodo in element:
            if nodo.key == key:
                return key
        return None

# Add locations to a Hashtable
def createLocations(LocationList):
    dictionary = DictionaryElement()
    return createLocationsR(LocationList, dictionary)
def createLocationsR(LL, D):
    if LL == []:
        return D
    key = ord(LL[0][0][0:1]) + LL[0][0][1:len(LL[0][0])]    # Change for better management
    value = LL[0][1]                                        # '' '' '' '' '' '' '' '' '' ''
    insert(D, key, value)
    LL = LL.pop(0)
    createLocationsR(LL, D)

# Pruebas del Hash
key = "A24"
print("La A vale en ASCII: ", ord(key[0:1]))
print("El valor del key es: ", ord(key[0:1])+int(key[1:len(key)]))
print("Tras el HashFunction: ", (ord(key[0:1])+int(key[1:len(key)]))%47)

# Basic Functions
def selectNode(node):
    a = 0