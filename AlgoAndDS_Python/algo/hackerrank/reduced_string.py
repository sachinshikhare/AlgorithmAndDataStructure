'''
https://www.hackerrank.com/challenges/reduced-string
Created on 29-Mar-2017

@author: sachin

aaabccddd --> abd

baab ---> Empty String
'''

string = input().strip()

i = 0
reduced = True
while True:
    if len(string) > 0 and string[i] == string[i+1]:
        string = string[:i] + string[i+2:]
        reduced = True
    if i < len(string)-2:
        i = i + 1
    else:
        if not reduced:
            break
        i = 0
        reduced = False
    
if len(string) != 0:
    print(string)
else:
    print("Empty String")