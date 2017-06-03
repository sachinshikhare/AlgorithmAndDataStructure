"""
https://www.hackerrank.com/challenges/big-sorting
"""

count = int(input())

bucket = {}

for _ in range(count):
    number = input().strip()
    length = len(number)

    if length not in bucket:
        bucket[length] = []
    bucket[length].append(number)

for key in sorted(bucket):
    for val in sorted(bucket[key]):
        print(val)
