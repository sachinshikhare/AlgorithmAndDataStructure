'''
https://www.hackerrank.com/challenges/insertionsort1
Created on 29-Mar-2017

@author: sachin
5
2 4 6 8 3

101
2 4 8 12 15 19 21 24 26 29 30 32 35 36 41 44 49 52 57 58 59 64 65 68 73 77 80 82 85 88 93 97 101 105 108 111 115 118 122 127 130 131 132 134 135 136 138 141 144 146 151 153 158 160 165 169 171 176 179 184 187 190 194 197 200 205 210 215 217 222 225 230 231 236 239 243 244 246 248 253 254 256 258 262 263 267 272 274 277 280 284 285 289 291 295 297 301 305 310 312 279

10
2 3 4 5 6 7 8 9 10 1
'''

populate_input = lambda: list(map(int, input().split()))

no_of_elements = populate_input()[0]

arr = populate_input()

cntr = len(arr) - 1

key = arr[cntr]
cntr -= 1


def display_arr():
    print(" ".join(str(x) for x in arr))

while cntr >= 0:
    if arr[cntr] > key:
        arr[cntr+1] = arr[cntr]
        display_arr()
    else:
        arr[cntr+1] = key
        display_arr()
        break
    cntr-=1
else:
    arr[0] = key
    display_arr()

"""
2 3 4 5 6 7 8 9 10 10
2 3 4 5 6 7 8 9 9 10
2 3 4 5 6 7 8 8 9 10
2 3 4 5 6 7 7 8 9 10
2 3 4 5 6 6 7 8 9 10
2 3 4 5 5 6 7 8 9 10
2 3 4 4 5 6 7 8 9 10
2 3 3 4 5 6 7 8 9 10
2 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
"""