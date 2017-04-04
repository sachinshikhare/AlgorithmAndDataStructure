'''
https://www.hackerrank.com/challenges/quicksort1
Created on 01-Apr-2017

@author: sachin
'''

populate_input = lambda: list(map(int, input().split()))

count = populate_input()[0]
arr = populate_input()

# DIFFERENT APPROACH: It has nothing to do with quicksort  
# print(" ".join(str(x) for x in arr if x < arr[0]), arr[0], " ".join(str(x) for x in arr if x > arr[0]))

pivot = arr[0]
start = 0
end = count
partition_index = start + 1
 
 
def swap(arr, i, partition_index):
    temp = arr[i]
    arr[i] = arr[partition_index]
    arr[partition_index] = temp
 
partition_index = end - 1
for i in reversed(range(start+1, count)):
    if arr[i] >= pivot:
        swap(arr, i, partition_index)
        partition_index -=1
swap(arr, start, partition_index)
     
print(" ".join(map(str, arr)))