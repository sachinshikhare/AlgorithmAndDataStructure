import algo.ads.b_tree.b_tree_implementation as b_tree

b_tree = b_tree.BTree()

def close():
    print("Exiting...") 
    exit()
    
def b_tree_insert():
    try:
        data = int(input("Enter data: "))
        b_tree.b_tree_insert(data)
    except ValueError:
        print("Invalid input, operation unsuccessful...")

def b_tree_insert_multiple():
    all_values = input("Enter all values (comma(,) separated): ")
    all_values_arr = all_values.split(",")
    for value in all_values_arr:
        b_tree.b_tree_insert(int(value))
        
def search_element():
    try:
        data = int(input("Enter data to search: "))
        if b_tree.search_element(data):
            print("Data found")
        else:
            print("Data not found")
    except ValueError:
        print("Invalid input, operation unsuccessful...")
        
def tree_traversel():
    print("Traversal result: ", b_tree.tree_traversel())
    
b_tree.b_tree_insert(25)
b_tree.b_tree_insert(11)
b_tree.b_tree_insert(13)
b_tree.b_tree_insert(12)
b_tree.b_tree_insert(51)
b_tree.b_tree_insert(61)
b_tree.b_tree_insert(81)
b_tree.b_tree_insert(72)
b_tree.b_tree_insert(99)
b_tree.b_tree_insert(54)
b_tree.b_tree_insert(1)
b_tree.b_tree_insert(7)
b_tree.b_tree_insert(14)
b_tree.b_tree_insert(21)
b_tree.b_tree_insert(27)
b_tree.b_tree_insert(92)
b_tree.b_tree_insert(9)
b_tree.b_tree_insert(29)
b_tree.b_tree_insert(71)
b_tree.b_tree_insert(91)
b_tree.b_tree_insert(94)

print("Data inserted: 25,11,13,12,51,61,81,72,99,54,1,7,14,21,27,92,9,29,71,91,94")

options = {
        0: close,
        1: b_tree_insert,
        2: b_tree_insert_multiple,
        3: search_element,
        4: tree_traversel
#         3: in_order_tree_walk,
#         4: pre_order_tree_walk,
#         5: post_order_tree_walk,
#         6: search_data,
#         7: remove_data,
#         8: successor,
#         9: predecssor
    }

string = """            0: Exit
            1: Insert
            2: Insert Multiple
            3: Search data
            4: Tree traversal
            \nEnter your option: """
while(True):
    try:
        operation_index = int(input(string))
        if operation_index < 0 or operation_index > 4:
            raise ValueError()
        options[operation_index]()
    except ValueError:
        print("Invalid input, please enter valid input...")
    
