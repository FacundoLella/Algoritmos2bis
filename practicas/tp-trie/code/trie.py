class Trie:
  root = None

class TrieNode:
  parent = None
  children = None 
  key = None
  isEndOfWord = False


ListaMayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ListaMinusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

def NormalizarPalabraMay(Palabra):
  PalabraNormalizada = ""
  n = len(Palabra)
  flag = False
  i = 0
  while flag ==False and i!=27:
    if Palabra[0]==ListaMayusculas[i]:
      PalabraNormalizada = PalabraNormalizada + ListaMinusculas[i]
      flag = True
    else:
      i = i + 1
  if i==27:
    return Palabra
  else:
    for i in range(1,n):
      PalabraNormalizada = PalabraNormalizada + Palabra[i]
    return PalabraNormalizada
  
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

def PalabrasArbol(T,normalizar):
  if T.root==None or T.root.children==None:
    return None
  else:
    Children = T.root
    ListaP = []
    PalabrasArbolR(Children,"",ListaP,normalizar)
    return ListaP

def PalabrasArbolR(Children,palabra,ListaP,normalizar):
  n = len(Children.children)
  palabravieja = palabra
  i = 0
  while i!=n:
    palabra = palabra + Children.children[i].key
    if Children.children[i].isEndOfWord==True:
      if normalizar==1:
        PalabraNormalizada = NormalizarPalabraMay(palabra)
        ListaP.append(PalabraNormalizada)
      else:
        ListaP.append(palabra)
    if Children.children[i].children!=None:
      PalabrasArbolR(Children.children[i],palabra,ListaP,normalizar)
    palabra = palabravieja
    i = i + 1

def Pertenece(Ta,Tb):
  Lista = PalabrasArbol(Ta)
  n = len(Lista)
  i = 0
  while i!=n:
    VoF = Search(Tb,Lista[i])
    if VoF==False:
      return False
    else:
      i = i + 1  
  return True

def InvertirPalabra(Palabra):
  n = len(Palabra)
  NuevaPalabra = ""
  for i in range(0,n):
    NuevaPalabra = NuevaPalabra + Palabra[n-1-i]
  return NuevaPalabra 

def Invertida(T):
  Lista = PalabrasArbol(T,1)
  n = len(Lista)
  if n==0:
    return False
  else:
    i = 0
    while i!=n:
      NuevaPalabra = InvertirPalabra(Lista[i])
      if NuevaPalabra in Lista:
        return True
      else:
        i = i + 1
    return False

def autoCompletar(T,prefijo):
  ListaP = []
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
  autoCompletarR(Children,palabra,ListaP)
  if len(ListaP)==0:
    return None
  else:
    if len(ListaP)>1:
      return None
    else:
      return ListaP[0]

def autoCompletarR(Children,palabra,ListaP):
  n = len(Children.children)
  palabravieja = palabra
  i = 0
  while i!=n:
    palabra = palabra + Children.children[i].key
    if Children.children[i].isEndOfWord==True:
      ListaP.append(palabra)
    if Children.children[i].children!=None:
      autoCompletarR(Children.children[i],palabra,ListaP)
    palabra = palabravieja
    i = i + 1



















