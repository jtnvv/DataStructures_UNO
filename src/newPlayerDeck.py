import sys
import os
ruta_carpeta1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
sys.path.append(ruta_carpeta1)
import DatosDePrueba
#Clase para las cartas como nodos de un AVL
#El parámetro "card" debe ser una tupla del json de cartas
#NO ES UN NÚMERO
class cardNode:
    def __init__(self, card):
        self.card = card
        self.left = None
        self.right = None
        self.height = 1
        #El compID es un identificador claro, el ID de la carta
        #Esto para lograr comparar pesos entre las cartas y balancear el arbol
        self.compID = card["id"]

#Este ya es un AVL clásico
class PlayerDeck:
    def __init__(self):
      self.root = None
      self.deckSize = 0
    
    def nodeHeight(self, node):
        if not node:
            return 0
        return node.height
    
    def nodeBalance(self, node):
        if not node:
            return 0
        return self.nodeHeight(node.left) - self.nodeHeight(node.right)
    
    def leftRotate(self, node):
        nRight = node.right
        T2 = nRight.left
        nRight.left = node
        node.right = T2
        node.height = 1 + max(self.nodeHeight(node.left), self.nodeHeight(node.right))
        nRight.height = 1 + max(self.nodeHeight(nRight.left), self.nodeHeight(nRight.right))
        return nRight
 
    def rightRotate(self, node):
        nLeft = node.left
        T3 = nLeft.right
        nLeft.right = node
        node.left = T3
        node.height = 1 + max(self.nodeHeight(node.left), self.nodeHeight(node.right))
        nLeft.height = 1 + max(self.nodeHeight(nLeft.left), self.nodeHeight(nLeft.right))
        return nLeft

    #Insert de forma recursiva
    def insert(self,card):
      self.root = self.recInsert(self.root,card)
      self.deckSize += 1

    def recInsert(self, root, card):
        if not root:
            return cardNode(card)
        elif card["id"] < root.compID:
            root.left = self.recInsert(root.left, card)
        else:
            root.right = self.recInsert(root.right, card)

        root.height = 1 + max(self.nodeHeight(root.left), self.nodeHeight(root.right))

        balance = self.nodeBalance(root)
 
        if balance > 1 and card["id"] < root.left.compID:
            return self.rightRotate(root)
 
        if balance < -1 and card["id"] > root.right.compID:
            return self.leftRotate(root)
 
        if balance > 1 and card["id"] > root.left.compID:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        if balance < -1 and card["id"] < root.right.compID:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def delete(self, card):
        self.root = self.recDelete(self.root, card)
        self.deckSize -= 1

    def recDelete(self, root, card):
        if not root:
            return root

        elif card.compID < root.compID:
            root.left = self.recDelete(root.left, card)

        elif card.compID > root.compID:
            root.right = self.recDelete(root.right, card)

        else:
            if not root.left:
                temp = root.right
                root = None
                return temp

            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.compID = temp.compID
            root.card = temp.card
            root.right = self.recDelete(root.right, temp)

        if not root:
            return root

        root.height = 1 + max(self.nodeHeight(root.left), self.nodeHeight(root.right))
        balance = self.nodeBalance(root)

        if balance > 1 and self.nodeBalance(root.left) >= 0:
            return self.rightRotate(root)

        if balance < -1 and self.nodeBalance(root.right) <= 0:
            return self.leftRotate(root)

        if balance > 1 and self.nodeBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and self.nodeBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def getMinValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inOrderTraversal(self):
        interfaceArray = []
        self.recInOrderTraversal(self.root, interfaceArray)
        return interfaceArray


    def recInOrderTraversal(self, node, arr):
        if node:
            self.recInOrderTraversal(node.left, arr)
            arr.append(node)
            self.recInOrderTraversal(node.right, arr)
"""
playerTest = PlayerDeck()
cards = DatosDePrueba.data_array
for i in cards:
    playerTest.insert(i)
testCard = cardNode(cards[1])
print(playerTest.deckSize)
testArr = playerTest.inOrderTraversal()
for i in testArr:
    print(i.compID, end=" ")
print()
print(testCard.compID)
print()
print(playerTest.delete(testCard).compID)
print(playerTest.deckSize)
testArr = playerTest.inOrderTraversal()
for i in testArr:
    print(i.compID, end=" ")
"""
