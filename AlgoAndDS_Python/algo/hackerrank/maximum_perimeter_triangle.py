'''
https://www.hackerrank.com/challenges/maximum-perimeter-triangle
Created on 15-Apr-2017

@author: sachin
5
1 1 1 3 3

3
1 2 3
'''

pi = lambda: list(map(int, input().split()))

_ = pi()[0]

lines = sorted(pi())

cntr = len(lines) - 3

while cntr >= 0 and lines[cntr] + lines[cntr+1] <= lines[cntr+2]:
    cntr -=1
    
if cntr == -1:
    print(-1)
else:
    print(lines[cntr], lines[cntr+1], lines[cntr+2])