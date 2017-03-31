'''
Created on 30-Mar-2017

@author: sachin
'''
from random import randint

def swap(arr, i, p_index):
    temp = arr[i]
    arr[i] = arr[p_index]
    arr[p_index] = temp


def partition(arr, start, end):
    pivot = arr[end]
    p_index = start
    for i in range(start, end):
        if arr[i] <= pivot:
            swap(arr, i, p_index)
            p_index+=1
    swap(arr, p_index, end)
    return p_index

def quick_sort(arr, start, end):
    if start < end:
        p_index = partition(arr, start, end)
        quick_sort(arr, start, p_index-1)
        quick_sort(arr, p_index + 1, end)
        
arr = []
for i in range(20):
    arr.append(randint(10,100))
print(arr)
quick_sort(arr, 0, len(arr)-1)
print()
print(arr)