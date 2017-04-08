'''
https://www.hackerrank.com/challenges/pairs
Created on 06-Apr-2017

@author: sachin
'''

pi = lambda: list(map(int, input().split()))

size, diff = pi()

arr = pi()
print(set(arr))
print(set(x + diff for x in arr))

print(len(set(arr) & set(x + diff for x in arr)))

# pair_cntr = 0
# 
# for elem in arr:
#     if elem + diff in arr or elem - diff in arr:
#         pair_cntr += 1
#         
# print(pair_cntr)