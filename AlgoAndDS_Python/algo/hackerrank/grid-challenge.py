"""
https://www.hackerrank.com/challenges/grid-challenge

1
5
ebacd
fghij
olmkn
trpqs
xywuv
"""

no_of_test_cases = int(input())


def is_sorted(string):
    return all(string[i] <= string[i+1] for i in range(len(string)-1))

def validate():
    size = int(input())
    arr = []
    success = True
    for _ in range(size):
        arr.append(sorted(input()))
    for row_index in range(size):
        string = ''
        for col_index in range(size):
            string += arr[col_index][row_index]
        if not is_sorted(string):
            success = False
            break
    return "YES" if success else "NO"

for _ in range(no_of_test_cases):
    print(validate())