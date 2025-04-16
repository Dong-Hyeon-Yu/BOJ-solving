#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17142                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17142                          #+#        #+#      #+#     #
#    Solved: 2025/04/16 17:40:08 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
UNVISITED, VIRUS = -123_456_789, 2
graph = [list(map(int, input().split())) for _ in range(N)]
viruses = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            viruses.append((i,j))
        elif graph[i][j] == 0:
            graph[i][j] = UNVISITED


min_time = 123_456_789
directions = [(1,0),(-1,0),(0,1),(0,-1)]
for combo in combinations(viruses, M):
    visited = [row[:] for row in graph] 
    max_dist = 0
    queue = deque()

    for virus in combo:
        queue.append((virus, 0))
        visited[virus[0]][virus[1]] = UNVISITED
        
    while queue:
        cur, dist = queue.popleft()

        if -dist >= min_time: break
        if visited[cur[0]][cur[1]] not in (UNVISITED, VIRUS): continue
        if visited[cur[0]][cur[1]] == UNVISITED:  # 바이러스는 최대 값으로 안침.
            max_dist = max(max_dist, -dist)
        visited[cur[0]][cur[1]] = dist
        
        for di in directions:
            nx = cur[0]+di[0]
            ny = cur[1]+di[1]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] in (UNVISITED, VIRUS):
                queue.append(((nx,ny),dist-1))

    if any(visited[i][j] == UNVISITED and graph[i][j] == UNVISITED for i in range(N) for j in range(N)): continue
    
    min_time = min(min_time, max_dist)

if min_time == 123_456_789:
    print(-1)
else:
    print(min_time)