import time

class Node:
    def __init__(self,data):
      self.data = data
      self.next = None

class DiscardDeck:
  def __init__(self):
    self.head = None
    self.tail = None

  def Enqueue(self,key):
    node = Node(key)
    if (self.tail == None):
      self.tail = node
      self.head = self.tail
    else:
      self.tail.next = node
      self.tail = node

  def Dequeue(self):
    item = self.head.data
    self.head = self.head.next
    return item
    
  def DeckPrint(self):
    node = self.head
    while (node.next!=None):
        print(node.data, end=" ")
        node = node.next
    print(node.data, end="")
  
  def LastCardPlayed(self):
    return self.head.data
  