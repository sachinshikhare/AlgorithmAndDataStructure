'''
https://www.hackerrank.com/challenges/maximum-subarray-sum
Created on 08-Apr-2017

@author: sachin
1
5 7
3 3 9 9 5
'''

pi = lambda: list(map(int, input().split()))
 
def max_sub_arr_sum():
    arr_len, mod = pi()
    arr = pi()
    if mod == 1:
        return 0
    maximum = 0
    for i in range(arr_len):
        for j in range(i+1, arr_len):
            maximum = max(maximum, sum(arr[i:j]) % mod)
            if maximum == mod - 1:
                return maximum
    return maximum

q = pi()[0]
for _ in range(q):
    arr_len, mod = pi()
    arr = pi()
    arr2 = [[sum(arr[i:j])%7 for i in range(len(arr)+1)] for j in range(len(arr)+1)]
    print(max(max(arr2)))
#     print(max_sub_arr_sum())