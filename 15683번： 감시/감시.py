#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15683                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15683                          #+#        #+#      #+#     #
#    Solved: 2025/04/01 16:59:59 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from itertools import product
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

LEFT, RIGHT, UP, DOWN = (0,-1), (0,1), (-1,0),(1,0)
directions = (LEFT, UP, RIGHT, DOWN)

unit_vectors = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}
cctvs = [(graph[i][j], (i,j)) for j in range(m) for i in range(n) if 0<graph[i][j] and graph[i][j]<6]

cctv_types=[unit_vectors[type] for type, _ in cctvs]


def paint_graph(_graph, cctv_location, dirs):
    def _go_forth(i, j, unit_vector):
        while i>=0 and i<n and j>=0 and j<m and _graph[i][j] != 6:
            _graph[i][j] = -1
            i = i + unit_vector[0]
            j = j + unit_vector[1]

    i, j = cctv_location
    for di in dirs:
        _go_forth(i,j,directions[di])


def count_blank(cctvs, directions):
    global graph
    _graph = [row[:] for row in graph]
    for (_, cctv_location), direction in zip(cctvs, directions):
        paint_graph(_graph, cctv_location, direction)
        # print(cctv_type, cctv_location, direction)

    return sum([row.count(0) for row in _graph])

print(min(count_blank(cctvs, combo) for combo in product(*cctv_types)))