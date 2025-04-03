#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 5373                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/5373                           #+#        #+#      #+#     #
#    Solved: 2025/04/03 18:41:31 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

"""          U
          0  1  2
          3  4  5
          6  7  8
L        __________    R            B
36 37 38|F18 19 20 | 45 46 47 | 27 28 29
39 40 41| 21 22 23 | 48 49 50 | 30 31 32
42 43 44| 24 25 26 | 51 52 53 | 33 34 35
        -----------
          9  10 11
          12 13 14
          15 16 17
          D
"""
encode = {
    "U":0, "D":1, "F":2, "B":3, "L":4, "R":5, "+":1, "-":3
}
color = ["w", "y", "r", "o", "g", "b"]
cube = [[[9*f+3*j+i for i in range(3)] for j in range(3)] for f in range(6)]
arr = [""]*55


side_lotation = [
    [36,37,38,18,19,20,45,46,47,27,28,29],        # U
    [33,34,35,51,52,53,24,25,26,42,43,44],        # D
    [6,7,8,44,41,38,11,10,9,45,48,51],            # F
    [2,1,0,53,50,47,15,16,17,36,39,42],           # B
    [0,3,6,35,32,29,9,12,15,18,21,24],            # L
    [8,5,2,26,23,20,17,14,11,27,30,33]            # R
]

def rotate(face, cnt):
    global arr, cube
    def _rotate_face(face):
        tmp = [["" for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                tmp[c][2-r] = arr[cube[face][r][c]]

        for r in range(3):
            for c in range(3):
                arr[cube[face][r][c]] = tmp[r][c]

    def _rotate_side(face):
        tmp = [arr[side_lotation[face][i]] for i in range(12)]
        for i in range(12):
            arr[side_lotation[face][i]] = tmp[(i+3)%12]
        cube[face]
        
    for _ in range(cnt):
        _rotate_face(face)
        _rotate_side(face)

    

t = int(input())
while t:

    # init 
    for f in range(6):
        for j in range(9):
            arr[9*f+j] = color[f]

    _ = int(input())
    cmds = input().split()
    for cmd in cmds:
        f = encode[cmd[0]]
        cnt = encode[cmd[1]]
        rotate(f, cnt)

    print(''.join(arr[0:3]))
    print(''.join(arr[3:6]))
    print(''.join(arr[6:9]))

    t -= 1

