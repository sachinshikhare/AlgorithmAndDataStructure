""" It will require some modifications"""

activities = []

def recursive_activity_selector(start, finish, k, n):
    m = k + 1
    while m <= n and start[m] < finish[k]:
        m = m + 1
        
    if m <= n:
        activities.append(m)
        return recursive_activity_selector(start, finish, m, n)
        
start = [1,3,0,5,3,5,6,8,8,2,12]
finish = [4,5,6,7,9,9,10,11,12,14,16]
recursive_activity_selector(start, finish, 0, len(start)-1)
print(activities)

