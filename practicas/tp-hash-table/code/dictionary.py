class LinkedList:
  head = None

class Node:
  value = None
  nextnode = None
  key = None

def insert(D,key,value):
  h = indice(key)
  if D[h]==None:
    NewNode = Node()
    NewNode.key = key
    NewNode.value = value
    D[h] = NewNode
  else:
    if type(D[h])==LinkedList:
      add(D[h],value,key)
    else:
      value2 = D[h].value
      key2 = D[h].key
      D[h] = LinkedList()
      add(D[h],value2,key2)
      add(D[h],value,key)

def indice(k):
  return(k%9)

def add(L,value,key):
  NewNode  = Node()
  NewNode.value = value
  NewNode.key = key
  currentNode = L.head
  if L.head==None:
    L.head = NewNode
  else:
    while currentNode.nextnode!=None:
      currentNode = currentNode.nextnode
    currentNode.nextnode = NewNode

def search(D,key):
  h = indice(key)
  if D[h]==None:
    return None
  else:
    if D[h]==LinkedList:
      currentNode = D[h]
      while currentNode.nextnode!=None:
        if currentNode.key ==key:
          return currentNode.value
        else:
          currentNode = currentNode.nextnode
      return None
    else:
      if D[h].key==key:
        return D[h].value  
        
def deletekey(L,key):
  if L.head.key == key:
    L.head = L.head.nextnode
  else:
    currentNode = L.head 
    flag = False
    while flag==False:
      if currentNode.nextnode.key==key:
        if currentNode.nextnode.nextnode!=None:
          currentNode.nextnode = currentNode.nextnode.nextnode
          flag = True
        else:
          currentNode.nextnode = None
          flag = True
      else:
        currentNode = currentNode.nextNode

def Delete(D,key):
  h = indice(key)
  if D[h]==None:
    return D
  else:
    if D[h]==LinkedList:
      deletekey(D[h],key)
    else:
      D[h] = None







