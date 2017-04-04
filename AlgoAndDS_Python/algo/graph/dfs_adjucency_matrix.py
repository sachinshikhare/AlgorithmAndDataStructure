'''
Created on 03-Apr-2017

@author: sachin
'''

edges = ["1,2", "2,3", "3,4","1,3","3,7","2,7","6,8"]

matrix = [[0]*9]*9

for edge in edges:
    i,j = map(int, edge.split(","))
    matrix[i][j] = 1
    
print(matrix)