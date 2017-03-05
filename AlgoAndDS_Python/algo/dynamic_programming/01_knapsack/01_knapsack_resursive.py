''' 
    W: remaining capacity
    wt: array of weights of all elements
    val: array of values of all elements
    n: total count of values
'''

def zero_one_knapsack_recursive(W, wt, val, n):
    if n == 0 or W == 0:
        return 0;
    elif wt[n - 1] > W:
        return zero_one_knapsack_recursive(W, wt, val, n - 1)
    else:
        return max((val[n - 1] 
                    + zero_one_knapsack_recursive(W - wt[n - 1], wt, val, n - 1)),
                    zero_one_knapsack_recursive(W, wt, val, n - 1))

        

    
wt = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
val = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
W = 165
n = len(wt)

print(zero_one_knapsack_recursive(W, wt, val, n))
