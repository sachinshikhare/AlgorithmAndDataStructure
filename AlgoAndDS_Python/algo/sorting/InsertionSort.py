'''
Created on 30-Mar-2017

@author: sachin
'''
from random import randint
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j >0 and key < arr[j-1]:
            if key < arr[j-1]:
                arr[j] = arr[j-1]
                j-=1
        arr[j] = key

arr = []
for i in range(20):
    arr.append(randint(10,100))
print(arr)
insertion_sort(arr)
print()
print(arr)