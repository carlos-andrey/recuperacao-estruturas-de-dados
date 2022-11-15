from node import Node

class minPilha:
    def __init__(self):
        self.__top = None
        self.__size = 0
        self.data = []

    def top(self):
        if self.__size > 0:
            return self.__top

    def push(self, elemento):
        node = Node(elemento)
        node.next = self.__top
        self.__top = node
        self.__size =+1
        self.data.append(elemento)
        self.data.sort()

    def pop(self):
        if self.__size > 0:
            node = self.__top
            self.__top = self.__top.next
            self.__size =-1
            self.data.pop()
            return node
        
        
    
    def getMin(self):
        return self.data[0]