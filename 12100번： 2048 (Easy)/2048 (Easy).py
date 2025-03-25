#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 12100                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/12100                          #+#        #+#      #+#     #
#    Solved: 2025/03/21 19:21:59 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

from copy import deepcopy
import sys 

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

LEFT, RIGHT, UP, DOWN = (0,-1),(0,1),(-1,0),(1,0)
directions = [LEFT, RIGHT, UP, DOWN]

def get_max(graph)->int:
    v = -1
    for row in graph:
        for e in row:
            v= max(v, e)
    return v

def transpose(graph):
    return list([*tup] for tup in zip(*graph))

def flip(graph):
    for row in graph:
        row.reverse()

def _compress(row):
    n = len(row)
    left = 0
    right = 1

    while left < n and right < n:
        # print(row, left, right)
        if row[left] == 0:
            left += 1
            continue
        if row[right] == 0:
            right += 1
            continue
        if left >= right:
            right += 1
            continue
        

        if row[left] == row[right]:
            row[left] *= 2
            row[right] = 0
            left = right+1
            right += 2
        else:
            left = right
            right += 1

    # print(row, left, right)
    last_v = -1
    for i in range(n):
        if row[i] == 0:
            continue
        else:
            last_v += 1 
            row[last_v] = row[i]
            if i != last_v:
                row[i] = 0
    # print(row)


def _move_left(graph):
    for row in graph:
        _compress(row)

def move(graph, direction):
    if direction == LEFT:
        _move_left(graph)
    elif direction == UP:
        _move_left(graph := transpose(graph))
        graph = transpose(graph)
    elif direction == RIGHT:
        flip(graph)
        _move_left(graph)
        flip(graph)
    elif direction == DOWN:
        flip(graph:=transpose(graph))
        _move_left(graph)
        flip(graph)
        graph = transpose(graph)

    return graph

        
def dfs(graph, cnt, direction)->int:
    # print(f"{cnt}, {direction} (before)")
    # pprint(graph)
    # print()
    graph = move(graph, direction)
    # print(f"{cnt}, {direction} (after)")
    # pprint(graph, width=20)
    if cnt == 5:
        return get_max(graph)
    
    ans = -1
    for _direc in directions:
        ans = max(ans, dfs(deepcopy(graph), cnt+1, _direc))

    return ans

ans = -1
for _direc in directions:
    ans = max(ans, dfs(deepcopy(graph), 1, _direc))

print(ans)