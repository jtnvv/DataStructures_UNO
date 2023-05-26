class Node:
    def __init__(self,data):
      self.data = data
      self.next = None

class DiscardDeck:
  def __init__(self):
    self.head = None
    self.tail = None
    #Variable para el número actual de cartas
    self.num_cards = 0
    #Variables para el número actual
    self.currNum = None
    #variable para el color actual
    self.currColor = None

  #Método para verificar si la cola está vacia
  def is_empty(self):
    return self.head == None

  #Este método para encolar añade un elemento, incrementa el tamaño y verifica el tamaño
  def Enqueue(self,key):
      node = Node(key)
      if (self.tail == None):
        self.tail = node
        self.head = self.tail
      else:
        self.tail.next = node
        self.tail = node
      self.num_cards += 1
      #is_full() verifica el tamaño para vaciar
      self.is_full()

  #Borra el elemento más antiguo y lo retorna. Reduce el tamaño por 1
  def Dequeue(self):
    if self.is_empty():
      return None
    if self.head == self.tail:
      self.tail = None
    item = self.head.data
    self.head = self.head.next
    self.num_cards -= 1
    return item
  
  def printDeck(self):
    if self.is_empty():
      print("Deck is empty.")
      return
    
    current_node = self.head
    while current_node:
      print(current_node.data)
      current_node = current_node.next
  
  #Coge los dos datos de la última carta que se encoló (self.tail)
  def LastCardPlayed(self):
    if "number" in self.tail.data:
      self.currNum = self.tail.data["number"]
    else:
      self.currNum = 0
    self.currColor = self.tail.data["color"]
    #self.tail.data es la carta completa, o sea, el tipo dict
    return self.tail.data
  
  #is_full() verifica si el tamaño es de 50, entonces vacia toda la cola
  def is_full(self):
    if self.num_cards == 50:
      top = self.tail.data
      self.empty()
      self.Enqueue(top)
  
  #Este empty es un ciclo para el vaciado
  def empty(self):
    while not self.is_empty():
        self.Dequeue()
    
  
  
