#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 19238                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/19238                          #+#        #+#      #+#     #
#    Solved: 2025/05/13 12:43:07 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import deque
from heapq import heappop, heappush
input = sys.stdin.readline

N,M,FUEL = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
adjust_index = lambda x: int(x)-1
cur_i, cur_j = map(adjust_index, input().split())
customers = [list(map(adjust_index, input().split())) for _ in range(M)]
for i, customer in enumerate(customers):
    r,c,_,_ = customer
    graph[r][c] = i+2
    

directions = ((-1,0), (0,-1), (1,0), (0,1))
def bfs(start, dest=None):
    visited = [[False]*N for _ in range(N)]
    visited[start[0]][start[1]] = True
    que = []
    heappush(que, (0, start))

    while que:
        dist, (i, j) = heappop(que)

        if dest is None and graph[i][j] > 1:
            return (graph[i][j], dist)
        elif dest and dest == (i,j):
            return (-1, dist)

        for di, dj in directions:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and graph[ni][nj]!=1 and not visited[ni][nj]:
                visited[ni][nj] = True
                heappush(que, (dist+1,(ni,nj)))


while FUEL>0 and M>0:
    
    # 1) find shortest customer
    if res := bfs((cur_i, cur_j)):  
        # print(f"cur taxi waits ({cur_i}, {cur_j})")
        next_customer, dist1 = res
    else:
        break  # unreachable customer

    if FUEL-dist1 < 0: break
    FUEL -= dist1
    cur_i, cur_j, dest_i, dest_j = customers[next_customer-2]
    graph[cur_i][cur_j]=0

    # 2) take the customer to the destination
    if res := bfs((cur_i, cur_j), (dest_i, dest_j)):  
        _, dist2 = res
    else:
        break  # unreachable destination

    if FUEL-dist2 < 0: break
    cur_i, cur_j = dest_i, dest_j

    M -= 1
    FUEL += dist2
    

print(FUEL if M==0 else -1)


