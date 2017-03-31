'''
https://www.hackerrank.com/challenges/camelcase
Created on 29-Mar-2017

@author: sachin

saveChangesInTheEditor
'''

string = input().strip()
cntr = 0
if len(string) > 0 :
    cntr = 1
    for char in string:
        if char.isupper():
            cntr+=1
            
print(cntr)