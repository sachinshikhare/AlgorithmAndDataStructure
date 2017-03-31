'''
https://www.hackerrank.com/challenges/non-divisible-subset
input:
4 3
1 7 2 4
'''

n,k = input().strip().split(" ")
n,k = [int(n), int(k)]

arr = [int(x) for x in input().strip().split(" ")]

d = {x:[] for x in range(k)}

for i in range(n):
    d[arr[i]%k].append(arr[i])
    
count = 0
if len(d[0]) > 0:
    count += 1
    
s = set([(x, k-x) for x in range(1, k//2+1)])

for i,j in s:
    if i != j:
        count += len(d[i]) if len(d[i]) > len(d[j]) else len(d[j])
    elif len(d[i]) > 0:
        count += 1

print(count)