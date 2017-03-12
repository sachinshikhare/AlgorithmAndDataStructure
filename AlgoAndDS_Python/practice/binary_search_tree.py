class BSTNode:
    data = None
    parent = None
    left = None
    right = None
    def __init__(self, data):
        self.data = data
        
class BinarySearchTree:
    
    def __init__(self):
        self.root = None
    
    def insert(self, data=None):
        new_node = BSTNode(data)
        y = x = self.root
        
        while x != None:
            y = x
            if x.left
