"""
https://www.hackerrank.com/challenges/queens-attack-2
5 3
4 3
5 5
4 2
2 3

4 0
4 4

88587 9
20001 20003
20001 20002
20001 20004
20000 20003
20002 20003
20000 20004
20000 20002
20002 20004
20002 20002
564 323

"""

populate_input = lambda: list(map(int,input().split()))

dimension,number_of_obstacles = populate_input()
row_q, col_q = populate_input()
number_of_moves = [
        dimension-row_q, # 
        dimension-col_q, 
        row_q-1, 
        col_q-1,
        min(dimension-row_q, dimension-col_q), 
        min(row_q-1, col_q-1),
        min(dimension-row_q, col_q-1), 
        min(row_q-1, dimension-col_q)
    ]
for obst_cntr in range(number_of_obstacles):
    row_o, col_o = populate_input()
    if col_o == col_q:
        if row_o < row_q:
            number_of_moves[2] = min(number_of_moves[2], row_q - row_o - 1)
        else:
            number_of_moves[0] = min(number_of_moves[0], row_o - row_q - 1)
    elif row_o == row_q:
        if col_o < col_q:
            number_of_moves[3] = min(number_of_moves[3], col_q - col_o - 1)
        else:
            number_of_moves[1] = min(number_of_moves[1], col_o - col_q - 1)
    elif row_o - row_q == col_o - col_q:
        if row_o - row_q < 0:
            number_of_moves[5] = min(number_of_moves[5], row_q - row_o - 1)
        else:
            number_of_moves[4] = min(number_of_moves[4], row_o - row_q - 1)
    elif row_o - row_q == col_q - col_o:
        if row_o - row_q < 0:
            number_of_moves[7] = min(number_of_moves[7], row_q - row_o - 1)
        else:
            number_of_moves[6] = min(number_of_moves[6], row_o - row_q - 1)

print(sum(number_of_moves))