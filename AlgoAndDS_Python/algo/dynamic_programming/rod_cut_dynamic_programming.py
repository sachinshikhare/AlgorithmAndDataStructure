import random

class RodCutDynamicProgramming:

    def memoized_cut_rod(self, prices, size_of_rod):
        r = [];
        for _ in range(len(prices)):
            r.append(-1)
            
        return self.__memoized_cut_rod_aux(prices, size_of_rod, r)  
        
    def __memoized_cut_rod_aux(self, prices, size_of_rod, r):
        if r[size_of_rod] != -1:
            return r[size_of_rod]
        q = 0;
        if size_of_rod != 0:
            q = -1
            for i in range(1, size_of_rod + 1):
                q = max(q, prices[i] + self.__memoized_cut_rod_aux(prices, size_of_rod-i, r))
        r[size_of_rod] = q
        return q


MAX = 100
prices = [0]
for i in range(1, MAX):
    prices.append(prices[i-1] + random.randint(2,10))
    
print(*prices, sep=",")
print("\n\n")
    
rcdp = RodCutDynamicProgramming()
print(rcdp.memoized_cut_rod(prices, 5))