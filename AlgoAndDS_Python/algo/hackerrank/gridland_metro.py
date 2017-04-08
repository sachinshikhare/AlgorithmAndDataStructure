'''
https://www.hackerrank.com/challenges/gridland-metro
Created on 06-Apr-2017

@author: sachin

4 4 5
1 1 3
1 2 4
2 2 3
3 1 4
4 4 4

4 5 7
1 1 2
1 4 4
2 1 2
2 2 3
2 4 5
4 1 2
4 4 5
'''
from collections import defaultdict

pi = lambda: list(map(int, input().split()))

rows, cols, tracks = pi()

def check_allowed_positions():
    alllowed_positions = rows*cols
    if tracks == 0:
        return alllowed_positions
    d = defaultdict(list)
    for _ in range(tracks):
        r, c1, c2 = pi()
        d[r].append([c1,c2])
    for key in d:
        arr = d.get(key)
        arr.sort()
        cntr = 0    
        while cntr < len(arr):
            if cntr < len(arr) - 1 and arr[cntr][1] >= arr[cntr+1][0]:
                arr[cntr+1][0] = arr[cntr][0]
                arr[cntr+1][1] = max(arr[cntr+1][1], arr[cntr][1])
            else:
                alllowed_positions -= arr[cntr][1] - arr[cntr][0] + 1
            cntr += 1 
    return alllowed_positions

print(check_allowed_positions()) 
# grid_land = [[True]*rows for _ in range(cols)]
# for _ in range(tracks):
#     r, c1, c2 = pi()
#     for ci in range(c1-1, c2):
#         if grid_land[r-1][ci]:
#             alllowed_positions -= 1
#             grid_land[r-1][ci] = False
#             
# print(alllowed_positions)
