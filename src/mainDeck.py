import random

class MainDeck:
    def __init__(self, capacity):
        self.capacity = capacity
        self.lista = []
        self.list_size = 0

    def Full(self):
        return self.capacity == self.list_size

    def Empty(self):
        return self.list_size == 0

    def PushBack(self, key):
        if self.Full():
            return print("Baraja Completa")
        else:
            self.lista.append(key)
            self.list_size += 1

    def PopBack(self):
        if self.Empty():
            return print("Baraja Vacía")
        else:
            item = self.lista.pop()
            self.list_size -= 1
            return item

    def PushFront(self, key):
        if self.Full():
            return print("Baraja Completa")
        else:
            self.lista.insert(0, key)
            self.list_size += 1

    def AddEdge(self, key1, key2):
        if key1 in self.lista and key2 in self.lista:
            # No se implementa en esta versión del código
            pass
        else:
            return print("Cartas no encontradas en la baraja principal")

    def GetNeighbors(self, key):
        if key in self.lista:
            # No se implementa en esta versión del código
            pass
        else:
            return print("Carta no encontrada en la baraja principal")

    def RemoveEdge(self, key1, key2):
        if key1 in self.lista and key2 in self.lista:
            # No se implementa en esta versión del código
            pass
        else:
            return print("Cartas no encontradas en la baraja principal")

    def DeckShuffle(self):
        random.shuffle(self.lista)

    def DeckPrint(self):
        for key in self.lista:
            print(key, end=" ")
