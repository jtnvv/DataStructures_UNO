import random
class MainDeck:
  def __init__(self,capacity):
    self.capacity = capacity
    self.lista = [None]*capacity
    self.list_size = 0

  def Full(self):
    return self.capacity == self.list_size

  def Empty(self):
    return self.list_size==0

  def PushBack(self,key):
    if self.Full():
      return print("Baraja Completa")
    else:
      self.lista[self.list_size] = key
      self.list_size += 1

  def PopBack(self):
    self.lista[self.list_size-1]=None
    self.list_size -=1
    if self.list_size < 0:
      self.list_size=0
  def PushFront(self,key):
    if self.Full():
      return print("Baraja Completa")
    else :
      for i in range(self.list_size,0,-1):
        self.lista[i] = self.lista[i-1]
      self.lista[0] = key
      self.list_size += 1

  def DeckShuffle(self):
    for i in range(self.list_size):
      index = random.randint(0,self.list_size-1)
      self.lista[i], self.lista[index] = self.lista[index], self.lista[i]

  def DeckPrint(self):
    for i in range(self.list_size):
      print(self.lista[i], end=" ")
