"""
https://www.hackerrank.com/challenges/crush
5 3
1 2 100
2 5 100
3 4 100
"""
# 
# pi = lambda: arr(map(int, input().split()))
# 
# size, no_of_op = pi()
# 
# arr = [0]*size
# 
# for op_cntr in range(no_of_op):
#     start, end, number = pi()
#     for 


n, inputs = [int(n) for n in input().split(" ")]
arr = [0] * (n + 1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    arr[x - 1] += incr
    if((y) <= len(arr)): arr[y] -= incr;
maximum = x = 0
for i in arr:
    x = x + i;
    if(maximum < x): maximum = x;
print(maximum)
