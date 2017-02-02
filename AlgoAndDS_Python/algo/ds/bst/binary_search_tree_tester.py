import algo.ds.bst.binary_search_tree as bst

bst = bst.BinarySearchTree()

def close():
    print("Exiting...") 
    exit()
    
def insert():
    data = int(input("Enter data: "))
    bst.insert(data)

def in_order_tree_walk():
    bst.tree_walk("IN")
    
def pre_order_tree_walk():
    bst.tree_walk("PRE")

def post_order_tree_walk():
    bst.tree_walk("POST")

def search_data():
    data = int(input("Enter data: "))
    bst.search_data(data)

def remove_data():
    data = int(input("Enter data: "))
    bst.remove_data(data)

def successor():
    data = int(input("Enter data: "))
    bst.successor(data)

def predecssor():
    data = int(input("Enter data: "))
    bst.predecssor(data)

bst.insert(21)
bst.insert(13)
bst.insert(52)
bst.insert(5)
bst.insert(17)
bst.insert(22)
bst.insert(15)
bst.insert(12)
bst.insert(1)
bst.insert(3)
bst.insert(99)
bst.insert(97)
bst.insert(44)
bst.insert(40)
bst.insert(14)
bst.insert(19)
bst.insert(2)

options = {
        0: close,
        1: insert,
        2: in_order_tree_walk,
        3: pre_order_tree_walk,
        4: post_order_tree_walk,
        5: search_data,
        6: remove_data,
        7: successor,
        8: predecssor
    }

string = """            0: Exit
            1: Insert
            2: In order tree walk
            3: Pre order tree walk
            4: Post order tree walk
            5: Search Data
            6: Remove Data
            7: Successor
            8: Predecessor
            \nEnter your option: """
while(True):
    operation_index = int(input(string))
    options[operation_index]()
    