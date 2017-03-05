''' 
    W: remaining capacity
    wt: array of weights of all elements
    val: array of values of all elements
    n: total count of values
'''

def zero_one_knapsack_buttom_up(W, wt, val, n):
    
    arr = [[0]*(W+1) for _ in range(n+1)]
    
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                arr[i][w] = 0
            elif wt[i-1] > w:
                arr[i][w] = arr[i-1][w]
            else:
                arr[i][w] = max(arr[i-1][w], val[i-1] + arr[i-1][w-wt[i-1]])
    return arr[n][W]

    
wt = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
val = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
W = 165
n = len(wt)
 
print(zero_one_knapsack_buttom_up(W, wt, val, n))

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(zero_one_knapsack_buttom_up(W, wt, val, n));