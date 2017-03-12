
def return_two_values():
    return 1,"sachin"

x = return_two_values()
print(x) 


# def print_name_iterative():
#     for i in range(10):
#         print(i + 1, ": Sachin")
#         
# 
# def print_name_recursive(cntr):
#     if cntr == 0:
#         return
#     print(abs(cntr-11), ": Sachin")
#     print_name_recursive(cntr-1)
# 
# 
#         
# print_name_iterative()
# print_name_recursive(10)

# class TestClass:
#     __privateField = 33
#     def __init__(self):
# #         self.__privateField = 4
#         self.publicField = 5
#         
#     def print_all(self): 
#         print(self.__privateField)
#         print(self.publicField)
#         
# tester = TestClass()
# tester.print_all()
# print(tester.publicField)
# print(tester.__privateField)