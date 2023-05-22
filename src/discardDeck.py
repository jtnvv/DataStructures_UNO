class Node:
    def __init__(self,data):
      self.data = data
      self.next = None

class DiscardDeck:
  def __init__(self):
    self.head = None
    self.tail = None
    self.num_cards = 0

  def is_empty(self):
    return self.head == None

  def Enqueue(self,key):
      node = Node(key)
      if (self.tail == None):
        self.tail = node
        self.head = self.tail
      else:
        self.tail.next = node
        self.tail = node
      self.num_cards += 1
      self.is_full()

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
  
  def LastCardPlayed(self):
    return self.tail.data
  
  def is_full(self):
    if self.num_cards == 50:
      top = self.tail.data
      self.empty()
      self.Enqueue(top)
    
  def empty(self):
    while not self.is_empty():
        self.Dequeue()
    
  
  
