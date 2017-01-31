import algo.ds.linked_list.my_linked_list as linked_list

linked_list = linked_list.LinkedList()

def close():
    print("Exiting...") 
    exit()
    
def add_at_start():
    data = input("Enter data: ")
    linked_list.add_at_start(data)

def add_at_end():
    data = input("Enter data: ")
    linked_list.add_at_end(data)

def remove_first():
    data = linked_list.remove_first()
    print("Removed data: " + data)

def remove_last():
    data = linked_list.remove_last()
    print("Removed data: " + data)
    
def print_list():
    linked_list.print_linked_list()

options = {
        0: close,
        1: add_at_start,
        2: add_at_end,
        3: remove_first,
        4: remove_last,
        5: print_list,
    }

string = "0: Exit\n1: Insert at start\n2: Insert at end\n3: Remove first\n4: Remove last\n5: Print content\n\nEnter your option: "

while(True):
    operation_index = int(input(string))
    options[operation_index]()
    