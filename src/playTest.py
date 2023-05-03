import random

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == self.size:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            new_node.prev = current
            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
        self.size += 1

    def remove(self, data):
        if self.is_empty():
            raise Exception("List is empty")
        current = self.head
        while current is not None:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.size -= 1
                return True
            current = current.next
        return False

    def index_of(self, data):
        current = self.head
        index = 0
        while current is not None:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def remove_at(self, index):
        if self.head is None:
            return None

        # Si el índice es cero, el nodo a eliminar es el primero
        if index == 0:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            self.size -= 1
            return temp.data
        
        # Si el índice es igual al tamaño de la lista, el nodo a eliminar es el último
        if index == self.size - 1:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None
            self.size -= 1
            return temp.data
        
        # En cualquier otro caso, buscamos el nodo a eliminar
        curr = self.head
        for i in range(index):
            curr = curr.next
        
        temp = curr
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.size -= 1
        
        return temp.data
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
    def print_listCon(self):
        current = self.head
        i = 1
        while current:
            print(f"{i}. {current.data}")
            current = current.next
            i += 1
    
if __name__ == '__main__':
    baraja = [
            "R0","R0","R1","R1","R2","R2","R3","R3","R4","R4","R5","R5","R6","R6","R7","R7","R8","R8","R9","R9",\
                "Rr","Rr","RB","RB","R+",\
            "G0","G0","G1","G1","G2","G2","G3","G3","G4","G4","G5","G5","G6","G6","G7","G7","G8","G8","G9","G9"\
                ,"Gr","Gr","GB","GB","G+",\
            "B0","B0","B1","B1","B2","B2","B3","B3","B4","B4","B5","B5","B6","B6","B7","B7","B8","B8","B9","B9",\
                "Br","Br","BB","BB","B+",\
            "Y0","Y0","Y1","Y1","Y2","Y2","Y3","Y3","Y4","Y4","Y5","Y5","Y6","Y6","Y7","Y7","Y8","Y8","Y9","Y9"\
                ,"Yr","Yr","YB","YB","Y+",\
            "4+","4+","4+","4+","CC","CC","CC","CC"
        ]
    
    my_list = DoublyLinkedList()
    playerHand = DoublyLinkedList()
    cartaJugable = DoublyLinkedList()
    
    random.shuffle(baraja)
    
    for string in baraja:
        my_list.append(string)
        
    for i in range(7):
        randomElement = my_list.get(0)
        my_list.remove_at(0)
        playerHand.append(randomElement)
    print("---------------")
    playerHand.print_list()
    
    carta=my_list.get(0)
    my_list.remove(0)
    
    if playerHand.is_empty() == False:
        cont = 0
        for x in range(playerHand.size):
            if playerHand.get(x)[0] == carta[0] or playerHand.get(x)[1] == carta[1]:
                cartaJugable.append(playerHand.get(x))
            elif playerHand.get(x) == "CC" or playerHand.get(x) == "4+":
                cartaJugable.append(playerHand.get(x))  
            else:
                cont = cont+1
        print("-----------")  
        print("La carta en el tope es: "+str(carta))        
        print("-----------")  
        
        if cartaJugable.is_empty() == False:
            print("seleccione la carta a jugar: ")
            cartaJugable.print_listCon()
            entrada = input(":")
            select = int(float(entrada))
            
            element = cartaJugable.get(select-1)
            
            eliminate = playerHand.index_of(element)
            
            playerHand.remove_at(eliminate)
            cartaJugable.index_of(element)
            
            carta = element
            
            print("La lista en la mano del jugador es: ")
            playerHand.print_list()
            print("La carta en el tope del descarte es. ")
            print(carta)
