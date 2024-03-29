import sys
sys.setrecursionlimit(10**4)

class Node:
    def __init__(self):
        self.root = None
        self.leftNode = None
        self.rightNode = None

    def put_data(self, value):
        if self.root == None:
            self.root = value
            return
        else:
            if value < self.root:
                if self.leftNode == None:
                    self.leftNode = Node()
                
                self.leftNode.put_data(value)
            else:
                if self.rightNode == None:
                    self.rightNode = Node()
                
                self.rightNode.put_data(value)

    def print_node(self):
        if self.leftNode != None:
            self.leftNode.print_node()
        if self.rightNode != None:
            self.rightNode.print_node()
        
        print(self.root)

node = Node()
while True:
    try:
        n = int(input())
        node.put_data(n)
    except:break

node.print_node()