'''
https://www.hackerrank.com/challenges/runningtime
Created on 30-Mar-2017

@author: sachin
5
2 1 3 1 2
'''

populate_input = lambda: list(map(int, input().split()))

len_of_arr = populate_input()[0]

arr = populate_input()

def insertion_sort(arr):
    shift_count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j >0 and key < arr[j-1]:
            if key < arr[j-1]:
                arr[j] = arr[j-1]
                shift_count += 1
                j-=1
        arr[j] = key
    return shift_count

print(insertion_sort(arr))
