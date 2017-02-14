class TestClass:
    __privateField = 33
    def __init__(self):
#         self.__privateField = 4
        self.publicField = 5
        
    def print_all(self): 
        print(self.__privateField)
        print(self.publicField)
        
tester = TestClass()
tester.print_all()
print(tester.publicField)
print(tester.__privateField)