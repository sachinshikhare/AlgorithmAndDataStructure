import random;
prices = [0]
for i in range(1, 100):
    prices.append(prices[i-1] + random.randint(5,20))
    
# print(*prices, sep=",")

def cut_rod(prices, length = 6):
    if length == 0:
        return 0
    q = -1
    for cntr in range(1, length+1):
        q = max(q, prices[cntr] + cut_rod(prices, length - cntr))
    print(q)
    return q
    
print("Max profit: " + str(cut_rod(prices, 10)))