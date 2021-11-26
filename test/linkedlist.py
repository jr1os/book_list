from node import Node


class Linkedlist:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self, elem):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(elem)   
        else:
            pointer = Node(elem)
        self._size += 1
    
    def __len__(self):
        return self._size

