'''
Created on 15-Apr-2017

@author: sachin
3
1 3 2
'''

pi = lambda: list(map(int, input().split()))
 
no = pi()[0]
arr = sorted(pi(), reverse=True)
res = 0
for cntr in range(len(arr)):
    res += (arr[cntr] * 2 ** cntr)
 
print(res)

# _ = input()
# print(sum((1 << j) * c for j,c in enumerate(sorted((int(s) for s in input().split()), reverse = True))))

