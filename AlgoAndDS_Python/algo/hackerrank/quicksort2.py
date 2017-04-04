'''
https://www.hackerrank.com/challenges/quicksort2
Created on 01-Apr-2017

@author: sachin
7
5 8 1 3 7 9 2

2 3
1 2 3
7 8 9
1 2 3 5 7 8 9
'''
populate_input = lambda: list(map(int, input().split()))

count = populate_input()[0]
arr = populate_input()

def partition(arr, start, end):
    pivot = arr[start]
    partition_index = end - 1
    for i in reversed(range(start+1, end)):
        if arr[i] >= pivot:
            swap(arr, i, partition_index)
            partition_index -=1
    swap(arr, start, partition_index)
    return partition_index
    
def swap(arr, i, partition_index):
    temp = arr[i]
    arr[i] = arr[partition_index]
    arr[partition_index] = temp

def quick_sort(arr, start, end):
    if start < end:
        partition_index = partition(arr, start, end)
        if arr[start:end]:
            print(" ".join(map(str, arr[start:end])))
        quick_sort(arr, start, partition_index)
#         if arr[start:partition_index-1]:
#             print(" ".join(map(str, arr[start:partition_index-1])))
        quick_sort(arr, partition_index + 1, end)
#         if arr[partition_index + 1:end]:
#             print(" ".join(map(str, arr[partition_index + 1:end])))
        
quick_sort(arr, 0, count)
        
print(" ".join(map(str, arr)))