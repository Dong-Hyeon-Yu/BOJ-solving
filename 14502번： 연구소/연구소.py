#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14502                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14502                          #+#        #+#      #+#     #
#    Solved: 2025/03/28 17:02:46 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

direction = ((0,1),(0,-1),(1,0),(-1,0))
def dfs(x, y, _graph):
    num_of_infection = 0

    for di in direction:
        nx, ny = x+di[0], y+di[1]
        if nx >=0 and ny>=0 and nx < n and ny < m:
            if _graph[nx][ny] == 0: 
                _graph[nx][ny] = 2
                # print(nx, ny, "found a virus!")
                num_of_infection += dfs(nx,ny,_graph) + 1

    return num_of_infection

blanks = tuple((x, y) for x in range(n) for y in range(m) if graph[x][y]==0)
num_of_safe = len(blanks)
ans = 0


for combo in combinations(blanks, 3):
    _graph = [row[:] for row in graph]  # more efficient than deepcopy !
    _graph[combo[0][0]][combo[0][1]] = 1
    _graph[combo[1][0]][combo[1][1]] = 1
    _graph[combo[2][0]][combo[2][1]] = 1

    tmp = 0
    for i in range(n):
        for j in range(m):
            if _graph[i][j] == 2:
                tmp += dfs(i, j, _graph)

    ans = max(ans, num_of_safe-tmp)

print(ans-3)