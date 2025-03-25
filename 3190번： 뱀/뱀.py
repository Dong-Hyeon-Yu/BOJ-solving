#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 3190                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/3190                           #+#        #+#      #+#     #
#    Solved: 2025/03/24 15:18:25 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from queue import deque
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apples = set(tuple(map(int, sys.stdin.readline().split())) for _ in range(k))
tmp = int(sys.stdin.readline())
movement = deque()
for _ in range(tmp):
    t, move_type = sys.stdin.readline().split()
    t = int(t)
    movement.append((t, move_type))

graph = [[0] * (n+1) for _ in range(n+1)]  # for snake location

head = (1,1)
tail = (1,1)
di = 3
t=1

def check_boundary(head):
    return 1 > head[0] or head[0] > n or 1 > head[1] or head[1] > n

def check_snake_body(head):
    return graph[head[0]][head[1]] != 0

direction = ((1,0), (0,-1), (-1,0), (0,1))  # D, L, U, R
def decide_new_direction(cur_di, turning_info):
    if turning_info == "L":
        return (cur_di - 1) % 4
    else:  # right
        return (cur_di + 1) % 4
    

def get_new_tail(tail):
    unique_value_of_cur_tail = graph[tail[0]][tail[1]]
    for uv in direction:
        next_tail = uv[0] + tail[0], uv[1] + tail[1]
        if not check_boundary(next_tail) \
            and unique_value_of_cur_tail+1 == graph[next_tail[0]][next_tail[1]]:
            return next_tail  


while True:
    # 1. normal move 
    #  (1) get next point (consider apple)
    #  (2) check graph boundary
    #  (3) check snake body
    unit_vector = direction[di]
    next_head = (head[0] + unit_vector[0], head[1] + unit_vector[1])
    # print(next_head)
    if check_boundary(next_head):
        break

    if check_snake_body(next_head):
        break

    head = next_head

    graph[head[0]][head[1]] = t

    if head in apples:
        apples.discard(head)
    else:
        new_tail = get_new_tail(tail)
        graph[tail[0]][tail[1]] = 0
        tail = new_tail

    # 2. turning after move
    if movement and movement[0][0] == t:
        _, new_di_info = movement.popleft()
        di = decide_new_direction(di, new_di_info)

    # pprint.pp(graph)
    t += 1


print(t)