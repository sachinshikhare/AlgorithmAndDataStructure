# import random

class RodCutDynamicProgramming:

    def __init__(self):
        self.MIN_VALUE = -32767
    
    def memoized_cut_rod(self, prices, size):
        values = [self.MIN_VALUE for _ in range(size+1)];
        return self.__memoized_cut_rod_aux(prices, size, values)  
        
    def __memoized_cut_rod_aux(self, prices, size, values):
        
        if values[size] != self.MIN_VALUE:
            return values[size]
        max_value = 0;
        if size == 0:
            max_value = 0
        else:
            max_value = self.MIN_VALUE
            for i in range(1, size+1):
                print(size)
                max_value = max(max_value, prices[i] + self.__memoized_cut_rod_aux(prices, size-i, values))
        values[size] = max_value
        return max_value
    
    def buttom_up_cut_rod(self, prices, ize):
        
        temp = [0] * (size + 1)
        for i in range(1, size):
            max_val = self.MIN_VALUE
            for j in range(i):
                max_val = max(max_val, prices[j+1] + temp[i - j - 1])
            print(max_val)
            temp[i] = max_val
        return temp[size-1]
        

# MAX = 100
# prices = [0]
# for i in range(1, MAX):
#     prices.append(prices[i-1] + random.randint(2,10))
#     
# print(*prices, sep=",")
# print("\n\n")

prices = [0,1,5,8,9,10,17,17,20]
size = len(prices)
    
rcdp = RodCutDynamicProgramming()
print("Memoized: " + str(rcdp.memoized_cut_rod(prices, size-1)))
print("Bottom up: " + str(rcdp.buttom_up_cut_rod(prices, size)))

""" TODO: this may require some modifications. Have to look later. """