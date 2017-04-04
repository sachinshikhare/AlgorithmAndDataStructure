'''
https://www.hackerrank.com/contests/hourrank-19/challenges/recover-the-array
Created on 03-Apr-2017

@author: sachin
11
5 4 5 4 3 3 2 1 4 1 4
26
3 1 4 2 5 1 2 5 2 6 8 1 2 5 3 6 8 4 6 1 4 4 5 3 1 6
'''

pi = lambda: list(map(int, input().split()))

total_no = pi()[0]

arr = pi()

cntr = 0
index = 0
while index < total_no:
    val = arr[index]
    cntr += 1
    index += val + 1
    
print(cntr)