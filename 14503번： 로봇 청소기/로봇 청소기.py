#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14503                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14503                          #+#        #+#      #+#     #
#    Solved: 2025/03/28 18:35:28 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
i, j, di = tuple(map(int, input().split()))
graph = [list(map(int,input().split())) for _ in range(n)]

direction = [(-1,0),(0,1),(1,0),(0,-1)]
WALL = 1
CLEANED = 2
NOT_CLEANED = 0


def check_boundary(i, j):
    return i>=0 and j>=0 and i<n and j<m


num_of_uncleaned = len([cell==NOT_CLEANED for row in graph for cell in row])
clean_count = 0
while num_of_uncleaned >= clean_count:
    # 1.
    if graph[i][j] == NOT_CLEANED:
        graph[i][j] = CLEANED
        clean_count += 1

    # 3.
    if any(
        graph[i+_i][j+_j] == NOT_CLEANED
        for _i, _j in direction
        if check_boundary(i+_i, j+_j)
    ):
        di = (di-1)%4 # 3-1.
        
        ni, nj = i+direction[di][0], j+direction[di][1]
        if check_boundary(ni, nj) and graph[ni][nj] == NOT_CLEANED: # 3-2.
            i,j = ni,nj
        else:
            continue  # 3-3.

    else: # 2.
        ni, nj = i-direction[di][0], j-direction[di][1]
        if check_boundary(ni, nj) and graph[ni][nj] != WALL: # 2-1.
            i,j = ni,nj
        else:
            break  # 2-2.


print(clean_count)