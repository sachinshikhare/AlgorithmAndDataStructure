import algo.ds.bst.binary_search_tree as bst

bst = bst.BinarySearchTree()

def close():
    print("Exiting...") 
    exit()
    
def insert():
    try:
        data = int(input("Enter data: "))
        bst.insert(data)
    except ValueError:
        print("Invalid input, operation unsuccessful...")

def insert_multiple():
    all_values = input("Enter all values (comma(,) separated): ")
    all_values_arr = all_values.split(",")
    for value in all_values_arr:
        bst.insert(int(value))

def in_order_tree_walk():
    bst.tree_walk("IN")
    
def pre_order_tree_walk():
    bst.tree_walk("PRE")

def post_order_tree_walk():
    bst.tree_walk("POST")

def search_data():
    data = int(input("Enter data: "))
    if bst.search_data(data):
        print("data found")
    else:
        print("data not found")

def remove_data():
    data = int(input("Enter data: "))
    bst.remove_data(data)

def successor():
    data = int(input("Enter data: "))
    bst.successor(data)

def predecssor():
    data = int(input("Enter data: "))
    bst.predecssor(data)

bst.insert(25)
bst.insert(11)
bst.insert(13)
bst.insert(12)
bst.insert(51)
bst.insert(61)
bst.insert(81)
bst.insert(72)
bst.insert(99)
bst.insert(54)
bst.insert(1)
bst.insert(7)
bst.insert(14)
bst.insert(21)
bst.insert(27)
bst.insert(92)
bst.insert(9)
bst.insert(29)
bst.insert(71)
bst.insert(91)
bst.insert(94)

options = {
        0: close,
        1: insert,
        2: insert_multiple,
        3: in_order_tree_walk,
        4: pre_order_tree_walk,
        5: post_order_tree_walk,
        6: search_data,
        7: remove_data,
        8: successor,
        9: predecssor
    }

string = """            0: Exit
            1: Insert
            2: Insert Multiple
            3: In order tree walk
            4: Pre order tree walk
            5: Post order tree walk
            6: Search Data
            7: Remove Data
            8: Successor
            9: Predecessor
            \nEnter your option: """
while(True):
    try:
        operation_index = int(input(string))
        if operation_index < 0 or operation_index > 9:
            raise ValueError()
        options[operation_index]()
    except ValueError:
        print("Invalid input, please enter valid input...")
    
    