'''
Created on 14-Apr-2017

@author: sachin
'''

amount = int(input("Enter Amount: "))
coins = map(int, input("enter space separated coins available: ").split())

# amount = 89
# coins = [1,2,3,5,10,20,50]
coins = sorted(coins, reverse=True)
def calc_number_of_coins_reqd(amount, coin_index):
    if amount < 1 or coin_index >= len(coins):
        return 0
    while amount < coins[coin_index]:
        coin_index += 1
    return 1 + calc_number_of_coins_reqd(amount-coins[coin_index], coin_index)

print(calc_number_of_coins_reqd(amount, 0))