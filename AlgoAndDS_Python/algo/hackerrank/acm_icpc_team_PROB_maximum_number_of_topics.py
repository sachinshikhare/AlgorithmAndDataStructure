'''
https://www.hackerrank.com/challenges/acm-icpc-team

4 5
10101
11100
11010
00101

IN PROGRESS
'''
populate_input = lambda: list(map(int,input().split()))
max_topics = 0
smart_teams = 0
persons, topics = populate_input()
arr = []
for _ in range(persons):
    arr.append(list(input().split()))
print(arr)
for i in range(persons):
    for j in range(i+1, persons):
        known_topics = 0
        for k in range(topics):
            print(i,j,k)
            if arr[i][k] or arr[j][k]:
                known_topics += 1
        if known_topics > max_topics:
            max_topics = known_topics
            smart_teams = 1
        else:
            smart_teams += 1
            
print(max_topics)
print(smart_teams)