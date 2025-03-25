#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14499                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14499                          #+#        #+#      #+#     #
#    Solved: 2025/03/25 16:31:27 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n, m, x, y, k = tuple(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(n)]
cmds = list(map(int, input().split()))
# dice = [[0] * 3 for _ in range(4)]
dice = [0,0,0,0,0,0]

direction = [(-1,-1), (0,1), (0,-1), (-1,0), (1,0)]
def check_boundary(_x, _y):
    return 0 <= _x and _x < n and 0 <= _y and _y < m

def _rotate_dice_to_left():
    dice[5],dice[3],dice[2],dice[1] = dice[3],dice[2],dice[1],dice[5]

def _rotate_dice_to_right():
    dice[1],dice[2],dice[3],dice[5] = dice[2],dice[3],dice[5],dice[1]

def _rotate_dice_to_up():
    dice[0],dice[2],dice[4],dice[5] = dice[2],dice[4],dice[5],dice[0]

def _rotate_dice_to_down():
    dice[0],dice[2],dice[4],dice[5] = dice[5],dice[0],dice[2],dice[4]

_rotate_dice = [None, _rotate_dice_to_right, _rotate_dice_to_left, _rotate_dice_to_up, _rotate_dice_to_down]

def rotate_dice(_x, _y, di):
    _rotate_dice[di]()

    if graph[_x][_y] == 0:
        # copy downside number to the cell
        graph[_x][_y] = dice[5]
    else:
        # copy the cell to the downside of the dice
        dice[5] = graph[_x][_y]
        graph[_x][_y] = 0


for cmd in cmds:
    di = direction[cmd]
    if check_boundary(x + di[0], y + di[1]) == False:
        continue

    x += di[0]
    y += di[1]

    rotate_dice(x, y, cmd)

    print(dice[2])