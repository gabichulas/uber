import linkedlist as link
import algo1
import array

class LinkedList:
  head = None

class Node:
  value = None
  nextNode = None


def enqueue(Q,element):
  link.add(Q,element)
  return None


def dequeue(Q):
	current = Q.head
	previous = current
	if current == None: return

	while current.nextNode != None:
		previous = current
		current = current.nextNode
	if previous == current:
		lastValue = current.value
		Q.head = None
		return lastValue
	else:
		lastValue = previous.nextNode.value
		previous.nextNode = None
		return lastValue
    