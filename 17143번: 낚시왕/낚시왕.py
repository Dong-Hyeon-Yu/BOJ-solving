#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17143                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17143                          #+#        #+#      #+#     #
#    Solved: 2025/04/15 17:09:57 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
R,C,M = map(int, input().split())
directions = [(-1,-1),(-1,0),(1,0),(0,1),(0,-1)]
convert = {1:2, 2:1, 3:4, 4:3}
EMPTY = M+1

sharks = [map(int, input().split()) for _ in range(M)]
graph = [[EMPTY]*C for _ in range(R)]
for i in range(len(sharks)):
    r,c,s,d,z = sharks[i]
    r-=1
    c-=1
    sharks[i] = (r,c,s,d,z)
    graph[r][c] = i


import pprint
position=-1
total_sharks = 0
while position < C-1:
    position += 1
    print("position", position)
    # pprint.pp(graph)
    for r in range(R):
        if (idx:= graph[r][position]) < EMPTY:
            print("catch!", idx, sharks[idx])
            total_sharks += sharks[idx][-1]
            sharks[idx] = None
            graph[r][position] = EMPTY
            break
    
    for idx in range(len(sharks)):
        if sharks[idx] is None: continue

        r,c,s,d,z = sharks[idx]
        nr,nc = r+directions[d][0]*(s%(2*(R-1))),c+directions[d][1]*(s%(2*(C-1)))
        while True:
            if nr < 0:
                nr *= -1
                d = convert[d]
            elif nr >= R:
                nr = (R-1)-(nr-R+1) 
                d = convert[d]
            elif nc < 0:
                nc *= -1
                d = convert[d]
            elif nc >= C:
                nc = (C-1)-(nc-C+1)
                d = convert[d]
            else:
                break

        print("shark", idx, f"({r},{c}) ->", f"({nr},{nc})")

        if graph[r][c] >= idx:
            graph[r][c] = EMPTY

        another_idx=graph[nr][nc]
        if another_idx >= idx:  # normal case
            sharks[idx] = (nr,nc,s,d,z)
            graph[nr][nc] = idx
        elif another_idx < idx:  # 잡아먹어야 하는 상황
            if sharks[another_idx][-1] < sharks[idx][-1]: # 내가 잡아먹음
                graph[nr][nc] = idx
                sharks[another_idx] = None
                sharks[idx] = (nr,nc,s,d,z)
            else: # 내가 잡아먹힘
                sharks[idx] = None

    pprint.pp(graph)

print(total_sharks)
        