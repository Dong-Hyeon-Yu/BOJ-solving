#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14500                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14500                          #+#        #+#      #+#     #
#    Solved: 2025/03/26 21:11:04 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
_input = sys.stdin.read

data = _input().split()
n, m = int(data[0]), int(data[1])
graph = [list(map(int, data[i * m + 2:(i + 1) * m + 2])) for i in range(n)]

tetrominos = (
    ((0,0), (0,1), (0,2), (0,3)),
    ((0,0), (1,0), (2,0), (3,0)),

    ((0,0), (0,1), (1,0), (1,1)),

    ((0,0), (1,0), (2,0), (2,1)),
    ((0,0), (0,1), (0,2), (1,0)),
    ((0,0), (0,1), (1,1), (2,1)),
    ((1,0), (1,1), (1,2), (0,2)),
    ((0,1), (1,1), (2,1), (2,0)),  # flip
    ((0,0), (1,0), (1,1), (1,2)),
    ((0,0), (0,1), (1,0), (2,0)),
    ((0,0), (0,1), (0,2), (1,2)),

    ((0,0), (1,0), (1,1), (2,1)),
    ((1,0), (1,1), (0,1), (0,2)),
    ((0,1), (1,1), (1,0), (2,0)),  # flip
    ((0,0), (0,1), (1,1), (1,2)),

    ((0,0), (0,1), (0,2), (1,1)),
    ((0,1), (1,1), (2,1), (1,0)),
    ((1,0), (1,1), (1,2), (0,1)),
    ((0,0), (1,0), (2,0), (1,1)),
)


def check_boundary(x, y, tetromino):
    for i, j in tetromino:
        row, col = i+x, j+y
        if 0>row or 0>col or row>=n or col>=m:
            return False
    return True

ans = 0
for row in range(n):
    for col in range(m):
        for tetromino in tetrominos:
            if check_boundary(row, col, tetromino):
                ans = max(ans, sum([graph[row+i][col+j] for i, j in tetromino]))

print(ans)