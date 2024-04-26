class Trie:
  root = None

class TrieNode:
  parent = None
  children = None 
  key = None
  isEndOfWord = False

def Insert(T,element):
  Children = T.root
  n = len(element)
  k = 0
  while n!=k:
    if Children.children==None:
      Lista = []
      Children.children = Lista
      NewTrieNode = TrieNode()
      NewTrieNode.key = element[k]
      Lista.append(NewTrieNode)
      Padre = Children
      Children = NewTrieNode
      Children.parent = Padre
    else:
      VoF = False
      i = 0
      while VoF == False:
        if i==len(Children.children):
          NewTrieNode = TrieNode()
          NewTrieNode.key = element[k]
          Children.children.append(NewTrieNode)
          Padre = Children
          Children = NewTrieNode
          Children.parent = Padre
          VoF = True
        else:
          if Children.children[i].key == element[k]:
            Children = Children.children[i]
            VoF = True
          else:
            i = i + 1
          
    k = k + 1
  Children.isEndOfWord = True


def Search(T,element):
  Children = T.root
  n = len(element)
  k = 0
  i = 0
  while True:
    if i==len(Children.children):
      return False
    else:
      if Children.children[i].key==element[k]:
        Children = Children.children[i]
        k = k + 1
        i = 0
        if k==n or Children.children==None:
          if Children.isEndOfWord==True and k==n:
            return True
          else:
            return False
      else: 
        i = i + 1

def Delete(T,element):
  Children = T.root
  ListaActual = Children.children
  Eliminar = Children.children[0]
  n = len(element)
  k = 0
  i = 0
  while True:
    if i==len(Children.children):
      return False
    else:
      if Children.children[i].key==element[k]:
        if len(Children.children)>1:
          ListaActual = Children.children
          Eliminar = Children.children[i]
        k = k + 1
        if k==n:
          if Children.children[i].isEndOfWord==True:
            if Children.children[i].children==None:
              ListaActual.remove(Eliminar)
              return True
            else:
              Children.children[i].isEndOfWord = False
              return True
          else:
            return False
        else:
          Children = Children.children[i]
          i = 0
      else:
        i = i + 1

def Prefix(T,prefijo,n):
  ListaPalabras = []
  Children = T.root
  t = len(prefijo)
  i = 0
  k = 0
  while True:
    if i==len(Children.children):
      return None
    else:
      if Children.children[i].key==prefijo[k]:
        Children = Children.children[i]
        i = 0
        k = k + 1
        if k==t:
          break
      else:
        i = i + 1
  palabra = prefijo
  contador = t
  if Children.children ==None:
    return None
  else:

    PrefixR(ListaPalabras,Children,contador,n,palabra)
    return ListaPalabras







def PrefixR(ListaPalabras,Children,contador,n,palabra):
  if Children.isEndOfWord==True and contador==n:
    ListaPalabras.append(palabra)
  if Children.children!=None:
    q = len(Children.children)
    i = 0
    vieja = palabra
    contadorviejo = contador
    while q!=i:
      if Children.children!=None and contador!=n:
        palabra = palabra + Children.children[i].key
        contador = contador + 1
        PrefixR(ListaPalabras,Children.children[i],contador,n,palabra)
      if Children.isEndOfWord==True and contador==n:
        palabra = palabra + Children.children[i].key
        ListaPalabras.append(palabra)
      i = i + 1
      palabra = vieja
      contador = contadorviejo

























