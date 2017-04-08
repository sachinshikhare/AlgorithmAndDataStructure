'''
https://www.hackerrank.com/challenges/2d-array
Created on 03-Apr-2017

@author: sachin
'''

pi = lambda: arr(map(int, input().split()))

arr = [[0]*6]*6

for i in range(6):
    arr[i] = pi()
    
sums = []
for i in range(4):
    for j in range(4):
        sums.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+
                            arr[i+1][j+1]+
                    arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
print(max(sums))