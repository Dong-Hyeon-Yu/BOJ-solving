#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17144                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17144                          #+#        #+#      #+#     #
#    Solved: 2025/04/10 17:56:03 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

R,C,T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
robot = []
for r in range(R):
    if A[r][0] == -1:
        robot.append((r,0))
        A[r][0] = 0


directions = [(1,0),(-1,0),(0,1),(0,-1)]
def disperse_dust():
    global A, R, C
    delta = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if A[r][c] == 0: continue

            candidates = []
            for di in directions:
                nr, nc = r+di[0], c+di[1]
                if 0<=nr<R and 0<=nc<C and (nr,nc) not in robot:
                    candidates.append((nr,nc))

            dust_delta = A[r][c] // 5
            for cr, cc in candidates:
                delta[cr][cc] += dust_delta
            A[r][c] -= dust_delta * len(candidates)

    for r in range(R):
        for c in range(C):
            A[r][c] += delta[r][c]

def clean_air(upper_line, lower_line):
    global A,R,C

    for r in reversed(range(0, upper_line)):
        A[r+1][0] = A[r][0]
    A[upper_line][0] = 0
    for c in range(C-1):
        A[0][c] = A[0][c+1]
    for r in range(upper_line):
        A[r][C-1] = A[r+1][C-1]
    for c in reversed(range(1,C)):
        A[upper_line][c]=A[upper_line][c-1]

    for r in range(lower_line, R-1):
        A[r][0] = A[r+1][0]
    A[lower_line][0] = 0
    for c in range(C-1):
        A[R-1][c] = A[R-1][c+1]
    for r in reversed(range(lower_line+1, R)):
        A[r][C-1] = A[r-1][C-1]
    for c in reversed(range(1, C)):
        A[lower_line][c] = A[lower_line][c-1]

high = min([r for r, _ in robot])
low = max([r for r, _ in robot])
time = 0
DEBUG = False#True
import pprint
    
while T > time:
    disperse_dust()
    if DEBUG:
        pprint.pp(A)
        print()
    clean_air(high, low)
    if DEBUG:
        pprint.pp(A)
    time += 1

print(sum([dust for row in A for dust in row ]))

