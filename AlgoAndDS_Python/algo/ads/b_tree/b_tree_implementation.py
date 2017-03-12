class BTreeNode:
    
    def __init__(self):
        self.elements = []
        self.children = []
        self.leaf = True
        self.elements_count = 0
        
class BTree:
    
    def __init__(self):
        self.root = None
        self.minimum_degree = 2
        
    def b_tree_create(self,data):
        x = BTreeNode()
        x.leaf = True
        x.elements.insert(0, data)
        x.elements_count = 1;
        # DISK_WRITE(x)
        self.root = x
        

    def __add_or_overwrite_at(self, arr, index, value):
        if len(arr) <= index:
            arr.insert(index, value) 
        else: 
            arr[index] = value  
    
    def __b_tree_split_child(self, x, i):
        z = BTreeNode()
        y = x.children[i]
        z.leaf = y.leaf
        z.elements_count = self.minimum_degree-1
        for j in range(self.minimum_degree-1):
            self.__add_or_overwrite_at(z.elements, j, y.elements[j+self.minimum_degree])
        if not y.leaf:
            for j in range(self.minimum_degree):
                self.__add_or_overwrite_at(z.children, j, y.children[j + self.minimum_degree])
        y.elements_count = self.minimum_degree-1
        for j in reversed(range(i, x.elements_count+1)):
            self.__add_or_overwrite_at(x.children, j+1, x.children[j])
        x.children[i+1] = z
        for j in reversed(range(i, x.elements_count)):
            self.__add_or_overwrite_at(x.elements, j+1, x.elements[j])
        self.__add_or_overwrite_at(x.elements, i, y.elements[self.minimum_degree-1])
        x.elements_count = x.elements_count + 1
        y.elements = y.elements[:self.minimum_degree-1]
        y.children = y.children[:self.minimum_degree]
        #DISK_WRITE(y)
        #DISK_WRITE(z)
        #DISK_WRITE(x)
        
    def b_tree_insert(self, value):
        if self.root == None:
            self.b_tree_create(value)
            return
        r = self.root
        if r.elements_count == 2*self.minimum_degree-1:
            s = BTreeNode()
            self.root = s
            s.leaf = False
            s.elements_count = 0
            s.children.insert(0, r)
            self.__b_tree_split_child(s, 0)
            self.__b_tree_insert_non_full(s,value)
        else:
            self.__b_tree_insert_non_full(r,value)
            
    def __b_tree_insert_non_full(self, x, value):
        i = x.elements_count
        if x.leaf:
            while i > 0 and value < x.elements[i-1]:
                self.__add_or_overwrite_at(x.elements, i, x.elements[i-1])
                i-=1
            self.__add_or_overwrite_at(x.elements, i, value)
            x.elements_count += 1
            #DISK_WRITE(x)
        else:
            while i > 0 and value < x.elements[i-1]:
                i-=1
            #DISK_READ(x.children[i])
            if x.children[i].elements_count == 2*self.minimum_degree - 1:
                self.__b_tree_split_child(x, i)
                if value > x.elements[i]:
                    i += 1
            self.__b_tree_insert_non_full(x.children[i], value)
            

    def __b_tree_search(self, x, element):
        i = 0
        while i < x.elements_count and element > x.elements[i]:
            i += 1
        if i < x.elements_count and  element == x.elements[i]:
            return x,i
        elif x.leaf: 
            return None
        else:
            #DISK_READ(x.childred[i])
            return self.__b_tree_search(x.children[i], element)
        
        
    def search_element(self, element):
        data_node = self.__b_tree_search(self.root, element)
        if data_node != None:
            return True
        else:
            return False
        

    def __b_tree_traverse(self, x):
        i = 0
        if not x.leaf:
            is_read = [False] * len(x.children)
            while i <= x.elements_count-1:
                if not is_read[i]:
                    self.__b_tree_traverse(x.children[i])
                    is_read[i] = True
                self.result += str(x.elements[i]) + ","
                if not is_read[i+1]:
                    self.__b_tree_traverse(x.children[i+1])
                    is_read[i+1] = True
                i += 1
        else:
            while i <= x.elements_count-1:
                self.result += str(x.elements[i]) + ","
                i+=1
        return self.result
        
    def tree_traversel(self):
        self.result = ""
        if self.root != None:
            self.__b_tree_traverse(self.root)
        return self.result
        
        
# b_tree =  BTree()
# b_tree.b_tree_insert(25)
# b_tree.b_tree_insert(11)
# b_tree.b_tree_insert(13)
# b_tree.tree_traversel()
# b_tree.b_tree_insert(12)
# b_tree.b_tree_insert(51)
# b_tree.b_tree_insert(61)
# b_tree.b_tree_insert(81)
# b_tree.tree_traversel()
# b_tree.b_tree_insert(72)
# b_tree.b_tree_insert(99)
# b_tree.b_tree_insert(54)
# b_tree.b_tree_insert(1)
# b_tree.b_tree_insert(7)
# b_tree.tree_traversel()
# b_tree.b_tree_insert(14)
# b_tree.b_tree_insert(21)
# b_tree.b_tree_insert(27)
# b_tree.b_tree_insert(92)
# b_tree.b_tree_insert(9)
# b_tree.b_tree_insert(29)
# b_tree.tree_traversel()
# b_tree.b_tree_insert(71)
# b_tree.b_tree_insert(91)
# b_tree.b_tree_insert(94)
# b_tree.tree_traversel()
#  
# print("Data inserted: 25,11,13,12,51,61,81,72,99,54,1,7,14,21,27,92,9,29,71,91,94")
# 
# print(b_tree.search_element(51))
# print(b_tree.search_element(11))
# print(b_tree.search_element(99))
# print(b_tree.search_element(98))
# print(b_tree.search_element(32))
# print(b_tree.search_element(7))
# print(b_tree.search_element(28))