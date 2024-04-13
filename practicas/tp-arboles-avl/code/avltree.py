

from binarytree import insertR


class AVLTree:
  root = None
  
class AVLNode: 
  key = None
  value = None  
  rightnode = None  
  leftnode = None
  parent = None
  bf = None

def imprimir_arbol(root, nivel=0, prefijo="Raíz: ", simbolo="■"):
  if root is not None:
    print(" " * (nivel * 4) + prefijo + simbolo, root.value)
    imprimir_arbol(root.leftnode, nivel + 1, "L--> ", "└──")
    imprimir_arbol(root.rightnode, nivel + 1, "R--> ", "└──")

def rotateLeft(Tree,avlnode):
  NewRoot = avlnode.rightnode
  avlnode.rightnode = None
  if NewRoot.leftnode!=None:
    NewLeft = NewRoot.leftnode
    NewRoot.leftnode = None
    avlnode.rightnode = NewLeft
    NewRoot.leftnode = avlnode
  else: 
    NewRoot.leftnode = avlnode
  if avlnode.parent!=None:
    Save = avlnode.parent
    avlnode.parent = NewRoot
    NewRoot.parent = Save
  else:
    NewRoot.parent = None
    avlnode.parent = NewRoot
    Tree.root = NewRoot
      
def rotateRight(Tree,avlnode):
  NewRoot = avlnode.leftnode
  avlnode.leftnode = None
  if NewRoot.rightnode!=None:
    NewLeft = NewRoot.rightnode
    NewRoot.rightnode = None
    avlnode.leftnode = NewLeft
    NewRoot.rightnode = avlnode
  else: 
    NewRoot.rightnode = avlnode
  if avlnode.parent!=None:
    Save = avlnode.parent
    avlnode.parent = NewRoot
    NewRoot.parent = Save
  else: 
    avlnode.parent = NewRoot
    NewRoot.parent = None
    Tree.root = NewRoot

def alt(Node):
  if Node.leftnode!=None and Node.rightnode!=None:
    if alt(Node.leftnode)>=alt(Node.rightnode):
      return(alt(Node.leftnode))
    elif alt(Node.leftnode)<alt(Node.rightnode):
      return(alt(Node.rightnode))
  else:
    if Node.leftnode==None and Node.rightnode==None:
      return 1
    elif Node.leftnode!=None and Node.rightnode==None:
      return(1+alt(Node.leftnode))
    else:
      return(1+alt(Node.rightnode))
  
def calculateBalance(Tree,avlnode):
  if avlnode!=None:
   if avlnode.leftnode ==None and avlnode.rightnode==None:
      avlnode.bf = 0
   if avlnode.leftnode !=None and avlnode.rightnode == None:
     avlnode.bf = 1+alt(avlnode.leftnode)
   if avlnode.leftnode ==None and avlnode.rightnode != None:
     avlnode.bf = -1-alt(avlnode.rightnode)
   if avlnode.leftnode !=None and avlnode.rightnode != None:
     avlnode.bf =  alt(avlnode.leftnode) - alt(avlnode.rightnode)
     
   if avlnode.leftnode!=None:
     calculateBalance(Tree,avlnode.leftnode)
   if avlnode.rightnode!=None:
    calculateBalance(Tree,avlnode.rightnode)
  
def reBalance(AVLTree):
  Desbalanceado = Buscador(AVLTree.root)
  if Desbalanceado!=None:
    Balanceador(Desbalanceado)
    reBalanceBF(AVLTree,Desbalanceado)
    return(AVLTree)
  else:
    return(AVLTree)
  
def Buscador(Node):
  if Node.bf==2 or Node.bf==-2:
    return(Node)
  else:
    if Node.leftnode!=None:
      return(Buscador(Node.leftnode))
    if Node.rightnode!=None:
      return(Buscador(Node.rightnode))

def Balanceador(Node):
  if Node.bf>=-2:
    if Node.rightnode.leftnode!=None:
      rotateRight(B,Node.rightnode)
      rotateLeft(B,Node)
    else:
      rotateLeft(B,Node)
  elif Node.bf>=2:
    if Node.leftnode.rightnode!=None:
      rotateLeft(B,Node.Leftnode)
      rotateRight(B,Node)
    else:
      rotateRight(B,Node)

def reBalanceBF(AVLTree,Node):
  contador = 0
  while Node.parent!=None:
    NodoAnterior = Node
    Node = Node.parent
    contador = contador + 1
  if contador!=0:
    calculateBalance(AVLTree,NodoAnterior)
    hleft = 1 + alt(Node.leftnode)
    hright = 1 + alt(Node.rightnode)
    Node.bf = hleft-hright
  else:
    calculateBalance(AVLTree,Node)
    
def insert(AVLTree,Element,Key):
  NewNode = AVLNode()
  NewNode.key = Key
  NewNode.value = Element
  CurrentNode = AVLTree.root
  if CurrentNode==None:
    AVLTree.root = NewNode
  else:
   insertR(CurrentNode,NewNode)
  reBalanceBF(AVLTree,NewNode)
  
def insertR(CurrentNode,Node):
  if CurrentNode.key==Node.key:
    return 1
  if Node.key>CurrentNode.key:
    if CurrentNode.rightnode==None:
      CurrentNode.rightnode = Node
      Node.parent = CurrentNode
    else:
      insertR(CurrentNode.rightnode,Node)
  if Node.key<CurrentNode.key:
    if CurrentNode.leftnode==None:
      CurrentNode.leftnode = Node
      Node.parent = CurrentNode
    else:
      insertR(CurrentNode.leftnode,Node)


  
def delete(AVLTree,Element):
  if AVLTree.root!=None:
    CurrentNode = AVLTree.root
    Node = searchNode(CurrentNode,Element)
    DeleteCasos(AVLTree,Node)
  else:
    return None

  

def DeleteCasos(AVLTree,Node):
  if Node.rightnode==None and Node.leftnode==None:
    if Node.parent.leftnode==Node:
      Node.parent.leftnode = None
    else:
      Node.parent.rightnode = None
      
  if Node.rightnode!=None and Node.leftnode==None:
    NodeR = Node.rightnode
    NodeR.parent = Node.parent
    Node.parent = None
  if Node.leftnode!=None and Node.rightnode==None:
    NodeR = Node.rightnode
    NodeR.parent = Node.parent
    Node.parent = None
    
    
  
  if Node.parent==None:
    if Node.rightnode!=None and Node.leftnode!=None:
      NodeR = Node.rightnode
      NewRoot = menordemayores(NodeR)
      NodeL = Node.leftnode
      NodeL.parent = NewRoot
      NodeR.parent = NewRoot
      AVLTree.root = NewRoot
      NewRoot.rightNode = NodeR
      NewRoot.leftnode = NodeL
    else:
      if Node.rightnode==None:
        NewRoot = Node.leftnode
        NewRoot.parent = None
        AVLTree.root = NewRoot
      else:
        NewRoot = Node.rightnode
        NewRoot.parent = None
        AVLTree.root = NewRoot
        
      
      

def searchNode(CurrentNode,Element):
  if CurrentNode.element==Element:
    return(CurrentNode)
  else:
    if CurrentNode.leftnode!=None:
      return(searchNode(CurrentNode.leftnode,Element))
    if CurrentNode.rightnode!=None:
      return(searchNode(CurrentNode.rightnode,Element))

def menordemayores(Node):
  Node = Node.rightnode
  while Node.leftnode!=None:
    Node = Node.leftnode
  if Node.rightnode!=None:
    Node.parent.leftnode = None
    Node.parent.leftnode = Node.rightnode
    Node.rightnode = None
  else:
    Node.parent.leftnode = None
  return(Node)
  
  
def NewAVL(AVLTreeA,AVLTreeB,key):
  hA = heightbf(AVLTreeA)
  hB = heightbf(AVLTreeA)
  


def heightbf(AVLTree):
  if AVLTree.root==None:
    return None
  else:
    return(heightbfR(AVLTree.root))

def heightbfR(Node):
  if Node.leftnode==None and Node.rightnode==None:
    return 
  if Node.bf>=1:
    return


  



def mostrarbf(Node):
  print(Node.bf)
  if Node.leftnode!=None:
    mostrarbf(Node.leftnode)
  if Node.rightnode!=None:
    mostrarbf(Node.rightnode)
  









  
    