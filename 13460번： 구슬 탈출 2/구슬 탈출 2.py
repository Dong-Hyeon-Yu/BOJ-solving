#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13460                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13460                          #+#        #+#      #+#     #
#    Solved: 2025/03/21 01:01:26 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from queue import deque
from collections import namedtuple
import sys

Point = namedtuple('Point', 'x y')
Direction = namedtuple('Direction', 'x y')

n, m = map(int, sys.stdin.readline().split())
graph = [sys.stdin.readline() for _ in range(n)]
LEFT, RIGHT, UP, DOWN = Direction(0,-1),Direction(0,1),Direction(-1,0),Direction(1,0)
direction = [LEFT, RIGHT, UP, DOWN] # l, r, u, d
red, blue, hole = Point(0,0), Point(0,0), Point(0,0)


def check(i, j):
    return 0<=i and i<n and 0<=i and i<m and graph[i][j] != "#"


def adjust(red:Point, blue:Point, r_cnt, b_cnt, _direc:Direction):
    if blue == hole: # do nothing
        return red, blue
    
    if r_cnt < b_cnt:
        blue = blue.x - _direc.x, blue.y - _direc.y
    else:
        red = red.x - _direc.x, red.y - _direc.y

    return red, blue

visited = set() # red와 blue가 이전에 있던 상태와 동일할 경우로는 가지 않음.
def move(red, blue):
    '''input: current red point and blue point'''

    def _move(ball: Point, direction: Direction):
        # 갈 수 있는 데까지 직진
        final_i, final_j = i,j = ball
        for move in range(max(n, m)): 
            di = move * direction.x
            dj = move * direction.y
            if check(i+di, j+dj):
                if (i+di, j+dj) == hole:
                    return hole, -1
                final_i, final_j = i+di, j+dj
            else:
                return Point(final_i, final_j), move-1

    ans = []
    # 4가지 방향 모두 탐색
    for _direc in direction:

        new_red, r_cnt = _move(red, _direc)
        new_blue, b_cnt = _move(blue, _direc) 
        if new_blue == hole:
            continue

        if new_red == new_blue:
            new_red, new_blue = adjust(new_red, new_blue, r_cnt, b_cnt, _direc)

        if (new_red, new_blue) not in visited:
            ans.append((new_red, new_blue))

    return ans

for i in range(n):
    for j in range(m):
        if graph[i][j] == "R":
            red = (i, j)
        elif graph[i][j] == "B":
            blue = (i, j)
        elif graph[i][j] == "O":
            hole = (i, j)
        
            
que = deque()
que.append((red, blue, 0))
ans = -1
while que:
    c_red, c_blue, cnt = que.popleft()
    visited.add((c_red, c_blue))
    
    possible_moves = move(c_red, c_blue)

    cnt += 1
    for n_red, n_blue in possible_moves:
        r_success = (n_red == hole)
        b_success = (n_blue == hole)
        if b_success:
            continue # fail
        elif r_success:
            # print(f"{cnt} move: red{n_red}, blue{n_blue} (success)")
            ans = cnt
            break
        elif cnt < 10: # no one success
            # print(f"{cnt} move: red{c_red}, blue{c_blue}")
            que.append((n_red, n_blue, cnt))

    if ans > -1:
        break
print(ans)