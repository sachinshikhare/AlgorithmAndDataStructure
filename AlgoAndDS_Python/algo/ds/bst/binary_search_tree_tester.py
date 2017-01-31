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

options = {
        0: close,
        1: insert,
        2: in_order_tree_walk,
        3: pre_order_tree_walk,
        4: post_order_tree_walk
    }

# string = "0: Exit\n1: Insert at start\n2: Insert at end\n3: Remove first\n4: Remove last\n5: Print content\n\nEnter your option: "
string = "0: Exit\n1: Insert\n2: In order tree walk\n3: Pre order tree walk\n4: Post order tree walk\n\nEnter your option: "
while(True):
    operation_index = int(input(string))
    options[operation_index]()
    