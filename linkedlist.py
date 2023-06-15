from algo1 import *
from mylib import *

class LinkedList:
  head = None

class Node:
  value = None
  nextNode = None

def add(l,element):
  node = Node()
  current = l.head
  node.value = element
  l.head = node
  node.nextNode = current

def search(l,element):
  current = l.head
  pos = 0
  while current != None:
    if current.value == element:
      return pos
    pos += 1
    current = current.nextNode
  return None

def length(L):
  current = L.head
  len = 0
  while current != None:
    len += 1
    current = current.nextNode
  return len

def insert(l,element,position):
    current = l.head
    if position > length(l) or position < 0:
        return None
    elif position == 0:
        add(l, element)
        l.head.nextNode = current
        return 0

    else:
        for i in range(1, position + 1):
            if (i == position):
                node = Node()
                node.value = element
                node.nextNode = current.nextNode
                current.nextNode = node
                position = i
            current = current.nextNode
        return position

def delete(l,element):
  current = l.head
  pos = search(l,element)
  if pos != None:
    if current.value == element:
      l.head = current.nextNode
      return pos
    while current != None:
      if current.nextNode.value == element:
        current.nextNode = current.nextNode.nextNode
        return pos
      current = current.nextNode    
  else:
    return None

def access(l,position):
  current = l.head
  if position >= 0 and position < length(l):
    for i in range(0,position+1):
      valor = current.value
      current = current.nextNode
    return valor
  elif position == 0:
      return current.value   
  else:
    return None
  
def update(l,element,position):
  current = l.head
  if position >= 0 and position < length(l):  
    for i in range(0,position):
      current = current.nextNode
    current.value = element
    return position
  else:
    return None

def revert(L):
	newL = LinkedList()
	len = length(L)
	current = L.head

	for i in range(len):
		len -= 1
		add(newL, current.value)
		current = current.nextNode
	return newL

def areEqual(L,T):
  len1 = length(L)
  len2 = length(T)
  v1 = Array(len1,0)
  v2 = Array(len2,0)
  cont1 = 0
  cont2 = 0
  contEqual = 0
  current1 = L.head
  current2 = T.head
  if len1 == 0 and len2 == 0:
    return False
  elif len1 == len2:
    while current1 != None:
      v1[cont1] = current1.value
      cont1 += 1
      current1 = current1.nextNode
  
    while current2 != None:
      v2[cont2] = current2.value
      cont2 += 1
      current2 = current2.nextNode
  
    for i in range(len1):
      if v1[i] == v2[i]:
        contEqual += 1

    if contEqual == len1:
      return True
    else:
      return False
  else:
    return False