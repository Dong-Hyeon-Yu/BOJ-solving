#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16234                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16234                          #+#        #+#      #+#     #
#    Solved: 2025/04/07 16:26:46 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]


dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dfs(r, c):
    global L, R, visited, graph

    c_sum = graph[r][c]
    visited.add((r,c))
    countries = [(r,c)]
    
    for i in range(4):
        dr = r + dx[i]
        dc = c + dy[i]
        if 0<=dr<N and 0<=dc<N and (dr,dc) not in visited:
            if L <= abs(graph[r][c] - graph[dr][dc]) <= R:
                _c_sum, _countries = dfs(dr, dc)
                countries += _countries
                c_sum += _c_sum

    return c_sum, countries


day = 0
while True:
    visited = set()
    flag = False
    for r in range(N):
        for c in range(N):
            if (r,c) in visited:
                continue

            c_sum, countries = dfs(r,c)
            if len(countries) > 1:
                flag = True
                c_sum //= len(countries)
                for i,j in countries:
                    graph[i][j] = c_sum
    if flag:
        day += 1
    else:
        break

print(day)
