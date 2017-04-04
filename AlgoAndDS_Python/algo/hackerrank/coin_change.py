'''
https://www.hackerrank.com/challenges/coin-change
Created on 03-Apr-2017

@author: sachin

4 3
1 2 3

10 4
2 5 3 6 
'''
populate_input = lambda: list(map(int, input().split()))

money, types_of_coins = populate_input()
memoized = {}
coins_arr = populate_input()
def calculate_ways(money, coins_arr, coin_number, memoized):
    key = str(money) + "-" + str(coin_number)
    if memoized.get(key):
        return memoized.get(key)
    if money == 0:
        return 1
    if coin_number == len(coins_arr)-1:
        if money % coins_arr[coin_number] == 0 :
            return 1
        else: 
            return 0
    
    i = 0
    ways = 0
    while i <= money:
        ways += calculate_ways(money-i, coins_arr, coin_number+1, memoized)
        i+=coins_arr[coin_number]
    memoized[key] = ways
    return memoized.get(key)
    
print(calculate_ways(money, coins_arr, 0, memoized))