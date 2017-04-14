class Node:
    def __init__(self, data):
        self.data = data
        self.rank = 0
        self.parent = self
        

class DisjointSet:
    def __init__(self):
        self.ds = {}
        
    def make_set(self, data):
        node = Node(data)
        self.ds[data] = node
        
    def find_set_for_node(self, node):
        if node.parent == node:
            return node
        return self.find_set_for_node(node.parent)
    
    def find_set(self, data):
        node = self.ds[data]
        if node:
            result_node = self.find_set_for_node(node)
            return result_node.data
        else:
            return None
        
    def union(self, data1, data2):
        node1 = self.ds[data1]
        node2 = self.ds[data2]
        
        set_1 = self.find_set_for_node(node1)
        set_2 = self.find_set_for_node(node2)
        
        if set_1.data == set_2.data:
            return
        if set_1.rank > set_2.rank:
            set_2.parent = set_1
            set_1.rank = set_1.rank + 1
        else:
            set_1.parent = set_2
            set_2.rank = set_2.rank + 1 

# TESTER
# ds = DisjointSet()
# ds.make_set(1)
# ds.make_set(2)
# ds.make_set(3)
# ds.make_set(4)
# ds.make_set(5)
# ds.make_set(6)
# ds.make_set(7)
# 
# ds.union(1, 2)
# ds.union(2, 3)
# ds.union(4, 5)
# ds.union(6, 7)
# ds.union(5, 6)
# ds.union(3, 7)

