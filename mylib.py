import algo1
from random import *
from math import *

def arr_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
      
        if not swapped:
            return

def vect_random(arr):
  n = len(arr)
  for i in range(0,n):
    arr[i] = randint(-9,9)

def matr_random(arr,m,n):

  for i in range(0,m):
    for j in range(0,n):
      arr[i][j] = randint(0,3)

def print_matrix(matriz):
  for i in matriz:
        for j in i:
            print(j, end=" ")
        print()

def multipMatrVect(matriz,m,n,vector):
  long = len(vector)
  matrizFinal = algo1.Array(m,algo1.Array(long,0))
  for i in range(0,m):
    for j in range(0,long):
      for k in range(0,n):
        matrizFinal[i][j] = matriz[i][k]*vector[j] 
  
  print_matrix(matrizFinal)

def diagDom(matriz):
  if(matriz.size == matriz[0].size):
      for i in range(0, matriz.size):
        sumaFila = 0
        for j in range(0, matriz[0].size):
          if(i == j):
            diagonal = abs(matriz[i][j])
          else:
            sumaFila += abs(matriz[i][j])
            
        if(not(diagonal > sumaFila)):
          return False
          
      return True      

def multipMatrices(mat1,m1,n1,mat2,m2,n2):
  if n1==m2:
    print("La matriz resultado de la multiplicación es: ")
    matrizFinal = algo1.Array(m1,algo1.Array(n2,0))
    for i in range(0, mat1.size):
      for j in range(0, matrizFinal[0].size):
        matrizFinal[i][j] = 0
    for i in range(0,m1):
      for j in range(0,n2):
        for k in range(0,m2):
          matrizFinal[i][j] += mat1[i][k]*mat2[k][j] 
    
    print_matrix(matrizFinal)
  else:
    print("La multiplicación no es posible, intente de nuevo.")
  if diagDom(matrizFinal):
    print("La matriz es estrictamente diagonal dominante por filas.")
  else:
    print("La matriz no es estrictamente diagonal dominante por filas.")

def printLinkedList(L):
  currentNode = L.head
  while currentNode != None:
    print(currentNode.value)
    currentNode = currentNode.nextNode
  