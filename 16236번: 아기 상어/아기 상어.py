#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16236                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16236                          #+#        #+#      #+#     #
#    Solved: 2025/04/09 14:06:14 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

directions = [(-1,0),(0,-1),(0,1),(1,0)]
shark = [(i, j) for i in range(N) for j in range(N) if graph[i][j]==9][0]

MAX=100_000_000
def bfs(shark, shark_value):
    global directions, graph, N
    visited = [[MAX]*N for _ in range(N)]
    min_val = MAX
    que = []
    que.append((0, shark))
    visited[shark[0]][shark[1]] = 0
    while que:
        sec, cur = heappop(que)
        sec *= -1
        nsec = sec + 1
        
        if sec > min_val: 
            continue
        
        if 0 < graph[cur[0]][cur[1]] < shark_value:
            min_val = min(min_val, sec)
                
        for di in directions:
            nr = cur[0] + di[0]
            nc = cur[1] + di[1]
            if 0<=nr<N and 0<=nc<N and shark_value >= graph[nr][nc]:
                if visited[nr][nc] > nsec:
                    visited[nr][nc] = nsec
                    heappush(que, (-nsec,(nr,nc)))

    for i in range(N): 
        for j in range(N):
            if visited[i][j] == min_val < MAX and 0 < graph[i][j] < shark_value:
                return (i, j), min_val
    
    return None, -1

seconds = 0
graph[shark[0]][shark[1]] = 0
shark_value = 2
num_of_eating = 0
i = 0
while True:
    i+=1
    new_feed, sec = bfs(shark, shark_value)
    if new_feed is None: break

    # print(i, "new_feed", new_feed ,"cur shark:", shark_value)
    graph[new_feed[0]][new_feed[1]] = 0
    shark = new_feed
    num_of_eating += 1
    if num_of_eating == shark_value:
        shark_value += 1
        num_of_eating = 0

    seconds += sec

print(seconds)


