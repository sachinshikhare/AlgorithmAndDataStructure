'''
https://www.hackerrank.com/challenges/priyanka-and-toys
Created on 15-Apr-2017

@author: sachin
5
1 2 3 17 10
'''
pi = lambda: list(map(int, input().split()))

_ = input()

weights = sorted(pi())

total_units = 0
curr_wt = weights[0]
# for wt in weights:
#     if wt > 0:
#         curr_wt = wt
#         break
cntr = 0
while cntr < len(weights):
    total_units += 1
    curr_wt = weights[cntr]
    cntr += 1
    while cntr < len(weights) and weights[cntr] <= curr_wt + 4:
        cntr += 1
        
print(total_units)