#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14891                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14891                          #+#        #+#      #+#     #
#    Solved: 2025/04/01 16:59:52 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from queue import deque
input = sys.stdin.readline
N = 0
S = 1
RIGHTSIDE = 2
LEFTSIDE = 6
CLOCKWISE, COUNTER_CLOCKWISE = 1, -1
wheels = [deque([S if c=="1" else N for c in input()][:-1]) for _ in range(4)]

def decide_turning_directions(wheel_no, clockwise):
    global wheels
    directions = [0] * 4

    def _decide_directions(wheel_no, clockwise):
        directions[wheel_no] = clockwise

        if wheel_no-1>=0 and directions[wheel_no-1]==0:
            if wheels[wheel_no-1][RIGHTSIDE] != wheels[wheel_no][LEFTSIDE]:
                _decide_directions(wheel_no-1, -1 * clockwise)
        if wheel_no+1<4 and directions[wheel_no+1]==0:
            if wheels[wheel_no][RIGHTSIDE] != wheels[wheel_no+1][LEFTSIDE]:
                _decide_directions(wheel_no+1, -1 * clockwise)
    
    _decide_directions(wheel_no, clockwise)
    return directions

def turn_wheel(wheel: deque, clockwise):
    if clockwise == CLOCKWISE:
        wheel.appendleft(wheel.pop())
    elif clockwise == COUNTER_CLOCKWISE:
        wheel.append(wheel.popleft())

for _ in range(int(input())):
    no, clockwise = map(int, input().split())
    no -= 1
    # print(no, clockwise)
    directions = decide_turning_directions(no, clockwise)
    # print(directions)
    for i, direction in enumerate(directions):
        turn_wheel(wheels[i], direction)
    # pprint.pp(wheels)

bias = 1
ans = 0
for wheel in wheels:
    ans += wheel[0]*bias
    bias *= 2

print(ans)
    

