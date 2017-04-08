'''
https://www.hackerrank.com/challenges/hackerland-radio-transmitters
Created on 04-Apr-2017

@author: sachin

5 1
1 2 3 4 5

8 2
7 2 4 6 5 9 12 11 
'''

pi = lambda: list(map(int, input().split()))
                  
no_of_houses, trans_range = pi()
house_locations = pi()

max_locn = max(house_locations) + 1













arr = [False] * max_locn
 
for locn in house_locations:
    arr[locn] = True
     
trans_cnt = 0
i = 0
while i < max_locn:
    if arr[i]:
        for j in reversed(range(i, trans_range+1)):
            if arr[j]:
                i = j + trans_range + 1
        trans_cnt += 1
    else:
        i += 1
         
print(trans_cnt)
