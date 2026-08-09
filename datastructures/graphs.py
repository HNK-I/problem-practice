

class Node:
    def __init__(self, var):
        self.var = var
        self.neighbours = []
    

class Graphs:
    def __init__(self, nodes):
        self.nodes = nodes
        
    def createNodes(self):
        node = Node(variable)