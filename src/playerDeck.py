class Node:
    def __init__(self, card=None, next=None):
        self.card = card
        self.next = next

class playerDeck:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add_card(self, card):
        node = Node(card)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def remove_card(self, card):
        if self.is_empty():
            return None
        if self.head.card == card:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return card
        curr_node = self.head
        while curr_node.next is not None and curr_node.next.card != card:
            curr_node = curr_node.next
        if curr_node.next is not None:
            card = curr_node.next.card
            curr_node.next = curr_node.next.next
            if curr_node.next is None:
                self.tail = curr_node
            return card
        return None
