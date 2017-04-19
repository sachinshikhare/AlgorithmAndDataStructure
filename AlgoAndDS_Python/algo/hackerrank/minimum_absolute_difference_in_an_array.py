'''
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array
Created on 14-Apr-2017

@author: sachin
3
3 -7 0
'''

pi = lambda: list(map(int, input().split()))

no_of_elem = pi()[0]

arr = pi()
arr = sorted(arr)

min_val = abs(arr[0]-arr[1])
for cntr in range(len(arr) -1):
    val = abs(arr[cntr]-arr[cntr + 1])
    if val < min_val:
        min_val = val 

print(min_val)