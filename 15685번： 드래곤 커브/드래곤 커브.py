#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15685                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15685                          #+#        #+#      #+#     #
#    Solved: 2025/04/03 18:41:15 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
arr = [[False] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    arr[x][y] = True

    move = [d]
    for _ in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i - 1] + 1) % 4)
        move.extend(tmp)

    for i in move:
        nx = x + dx[i]
        ny = y + dy[i]
        arr[nx][ny] = True
        x, y = nx, ny

# 모든 꼭짓점이 드래곤 커브의 일부인 정사각형 개수 구하기
ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i + 1][j] and arr[i][j + 1] and arr[i + 1][j + 1]:
            ans += 1

print(ans)