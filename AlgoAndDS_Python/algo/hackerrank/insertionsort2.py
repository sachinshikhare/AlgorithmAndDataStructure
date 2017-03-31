'''
https://www.hackerrank.com/challenges/insertionsort2
Created on 29-Mar-2017

@author: sachin
6
1 4 3 5 6 2
'''

populate_input = lambda: list(map(int, input().split()))

len_of_arr = populate_input()[0]

arr = populate_input()

def display_arr():
    print(" ".join(str(x) for x in arr))

for i in range(1, len(arr)):
    key = arr[i]
    j = i
    i += 1
    while j >0 and key < arr[j-1]:
        if key < arr[j-1]:
            arr[j] = arr[j-1]
            j-=1
    arr[j] = key
    display_arr()