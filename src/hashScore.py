import time
class Scoreboard:
    def __init__(self):
        self.names = []
        self.victory = [None]*31
    
    def polyHash(self,attribute):
        p=31
        x = 8
        hash = 0
        for i in range(len(attribute)-1,-1, -1):
            hash = (hash*x+ord(attribute[i]))%p
        return hash

    def win(self,nombre):
        if nombre not in self.names:
            self.names.append(nombre)
        hashValue = self.polyHash(nombre)
        if self.victory[hashValue] == None:
            self.victory[hashValue] = 1
        else:
            self.victory[hashValue] = self.victory[hashValue] + 1
    
    def listPrint(self):
        for i in self.names:
            name = i
            count = self.victory[self.polyHash(i)]
            print(name, count, sep=" ")


"""
score.win("Francisco")
score.win("Gabriel")
score.win("Juan")
score.win("Juan")
score.listPrint()
"""

    