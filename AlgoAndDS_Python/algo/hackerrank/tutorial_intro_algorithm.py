'''
https://www.hackerrank.com/challenges/tutorial-intro
Created on 29-Mar-2017

@author: sachin
4
6
1 4 5 7 9 12
'''

populate_input = lambda: list(map(int,input().split()))

number_to_search = populate_input()[0]
number_Of_elements = populate_input()[0]
arr = populate_input()

first = 0
last = len(arr) - 1
found = False
while not found and first <= last:
    mid = (first + last) // 2
    if arr[mid] == number_to_search:
        print(mid)
        break
    else:
        if arr[mid] < number_to_search:
            first = mid+1
        else:
            last = mid-1