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
        self.data_string = ""
    
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
            self.data_string += str(node.data) +", " 
            self.in_order(node.right)    
        return self.data_string;
    
    def pre_order(self, node=None):
        if node != None:
            self.data_string += str(node.data) +", "
            self.pre_order(node.left)
            self.pre_order(node.right)
        return self.data_string;    

    def post_order(self, node=None):
        if node != None:
            self.post_order(node.left)
            self.post_order(node.right)
            self.data_string += str(node.data) +", "
        return self.data_string;

    def tree_walk(self, order):
        self.data_string = ""
        if order == "IN":
            return self.in_order(self.root)
        elif order == "PRE": 
            return self.pre_order(self.root)
        elif order == "POST": 
            return self.post_order(self.root)            
            
    def __transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent


    def minimum(self, node):
        while node.left != None:
            node = node.left
        return node
    
    def maximum(self, node):
        while node.right != None:
            node = node.right
        return node

    def __delete_node(self, node):
        if node.left == None and node.right == None:
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            return
        if node.left == None:
            self.__transplant(node, node.right)
        elif node.right == None:
            self.__transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            if y.parent != node:
                self.__transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.__transplant(node, y)
            y.left = node.left
            y.left.parent = y
            
    def __search_node(self, data_node):
        return_node = None
        if self.root != None:
            current = self.root
            while current != None:
                if current.data < data_node.data:
                    current = current.right
                elif current.data > data_node.data:
                    current = current.left
                else:
                    return_node = current
                    break
        return return_node
            
    def search_data(self, data):
        return self.__search_node(BSTNode(data)) != None
    
    def remove_data(self, data):
        data_node = self.__search_node(BSTNode(data))
        if data_node != None:
            self.__delete_node(data_node)
        else:
            print("Data not found")
            
    def __find_successor(self, data_node):
        if data_node.right != None:
            return self.minimum(data_node)
        y = data_node.parent
        while y != None and data_node == y.right:
            data_node = y
            y = y.parent
        return y
    
    def successor(self, data):
        data_node = self.__search_node(BSTNode(data))
        if data_node != None:
            return self.__find_successor(data_node)
        else:
            print("Data not found")

    def __find_predecessor(self, data_node):
        if data_node.left != None:
            return self.maximum(data_node)
        y = data_node.parent
        while y != None and data_node == y.left:
            data_node = y
            y = y.parent
        return y
    
    def predecessor(self, data):
        data_node = self.__search_node(BSTNode(data))
        if data_node != None:
            return self.__find_predecessor(data_node)
        else:
            print("Data not found")
