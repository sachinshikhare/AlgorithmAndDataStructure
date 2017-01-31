class BSTNode:
    data = None
    parent = None
    left = None
    right = None
    def __init__(self, data=None):
        self.data = data
        
class BinarySearchTree:
    
    def __init__(self):
        self.root = None
    
    def insert(self, data=None):
        new_node = BSTNode(data)
        y = x = self.root
        while x != None:
            y = x
            if new_node.data < x.data:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if y == None:
            self.root = new_node
        elif new_node.data < y.data:
            y.left = new_node
        else:
            y.right = new_node
    

    def in_order(self, node=None):
        if node != None:
            self.in_order(node.left)
            print(node.data + " ")
            self.in_order(node.right)    
    
    def pre_order(self, node=None):
        if node != None:
            print(node.data + " ")
            self.in_order(node.left)
            self.in_order(node.right)    

    def post_order(self, node=None):
        if node != None:
            self.in_order(node.left)
            self.in_order(node.right)
            print(node.data + " ")    

    def tree_walk(self, order):
        if order == "IN":
            self.in_order(self.root)
        elif order == "PRE": 
            self.pre_order(self.root)
        elif order == "POST": 
            self.post_order(self.root)            