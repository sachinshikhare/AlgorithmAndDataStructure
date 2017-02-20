# import random;
# prices = [0]
# for i in range(1, 100):
#     prices.append(prices[i-1] + random.randint(5,20))
# from algo.dynamic_programming.rod_cut_dynamic_programming import prices
    
# print(*prices, sep=",")

prices = [0,1,5,8,9,10,17,17,20]
size = len(prices)

INT_MIN = -32767
def cut_rod(prices, length = 6):
    if length == 0:
        return 0
    q = INT_MIN
    for cntr in range(1, length+1):
        q = max(q, prices[cntr] + cut_rod(prices, length - cntr))
    print(q)
    return q
    
print("\nMax profit: " + str(cut_rod(prices, 4)))