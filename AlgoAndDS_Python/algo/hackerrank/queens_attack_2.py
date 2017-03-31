"""
https://www.hackerrank.com/challenges/queens-attack-2
5 3
4 3
5 5
4 2
2 3

4 0
4 4

ll = lambda: list(map(int,input().split()))
"""

dimension, no_of_obstacles = input().strip().split(" ")
dimension, no_of_obstacles = [int(dimension), int(no_of_obstacles)]

row_q, col_q = input().strip().split(" ")
row_q, col_q = [int(row_q)-1, int(col_q)-1]

obstacles_arr = []
for _ in range(no_of_obstacles):
    obst = [int(x)-1 for x in input().strip().split(" ")]
    obstacles_arr.append(obst)
    
allowed_positions = []
allowed_positions_cntr = 0

row_cntr = row_q + 1
while row_cntr < dimension:
    if [row_cntr, col_q] in obstacles_arr: break
    allowed_positions.append([row_cntr, col_q])
    allowed_positions_cntr += 1
    row_cntr += 1

col_cntr = col_q + 1
while col_cntr < dimension:
    if [row_q, col_cntr] in obstacles_arr: break
    allowed_positions.append([row_q, col_cntr])
    allowed_positions_cntr += 1
    col_cntr += 1

row_cntr = row_q - 1 
while row_cntr >= 0:
    if [row_cntr, col_q] in obstacles_arr: break
    allowed_positions.append([row_cntr, col_q])
    allowed_positions_cntr += 1
    row_cntr -= 1

col_cntr = col_q - 1
while col_cntr >= 0:
    if [row_q, col_cntr] in obstacles_arr: break
    allowed_positions.append([row_q, col_cntr])
    allowed_positions_cntr += 1
    col_cntr -= 1

row_cntr = row_q + 1
col_cntr = col_q + 1
while row_cntr < dimension and col_cntr < dimension:
    if [row_cntr, col_cntr] in obstacles_arr:
        break
    allowed_positions.append([row_cntr, col_cntr])
    allowed_positions_cntr += 1
    row_cntr += 1
    col_cntr += 1
    
row_cntr = row_q - 1
col_cntr = col_q - 1
while row_cntr >= 0 and col_cntr >= 0:
    if [row_cntr, col_cntr] in obstacles_arr:
        break
    allowed_positions.append([row_cntr, col_cntr])
    allowed_positions_cntr += 1
    row_cntr -= 1
    col_cntr -= 1

row_cntr = row_q - 1
col_cntr = col_q + 1
while row_cntr >= 0 and col_cntr < dimension:
    if [row_cntr, col_cntr] in obstacles_arr:
        break
    allowed_positions.append([row_cntr, col_cntr])
    allowed_positions_cntr += 1
    row_cntr -= 1
    col_cntr += 1

row_cntr = row_q + 1
col_cntr = col_q - 1
while row_cntr < dimension and col_cntr >= 0:
    if [row_cntr, col_cntr] in obstacles_arr:
        break
    allowed_positions.append([row_cntr, col_cntr])
    allowed_positions_cntr += 1
    row_cntr += 1
    col_cntr -= 1

print(allowed_positions_cntr)
# print(allowed_positions)


# for row_cntr in range(dimension):
#     if row_cntr == row_q:
#         continue
#     allowed_positions.append(str(row_cntr)+":"+str(col_q))
# for col_cntr in range(dimension):
#     if col_cntr == col_q:
#         continue
#     allowed_positions.append(str(row_q) +":"+str(col_cntr))
# 
# row_cntr = 0 if row_q < col_q else row_q - col_q    
# col_cntr = 0 if row_q > col_q else col_q - row_q
# 
# while row_cntr < dimension and col_cntr < dimension:
#     if row_cntr == row_q and col_cntr == col_q:
#         row_cntr += 1
#         col_cntr += 1
#         continue
#     allowed_positions.append(str(row_cntr)+":"+str(col_cntr))
#     row_cntr += 1
#     col_cntr += 1
#     
# row_cntr = 0
# col_cntr = row_q + col_q
# 
# while row_cntr < dimension and col_cntr >= 0:
#     if row_cntr == row_q and col_cntr == col_q:
#         row_cntr += 1
#         col_cntr -= 1
#         continue
#     allowed_positions.append(str(row_cntr)+":"+str(col_cntr))
#     row_cntr += 1
#     col_cntr -= 1
#     
# for obst in obstacles_arr:
#     if obst in allowed_positions:
#         