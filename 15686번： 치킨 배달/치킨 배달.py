#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15686                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15686                          #+#        #+#      #+#     #
#    Solved: 2025/04/03 18:41:23 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from itertools import combinations
input = sys.stdin.readline
n,m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
houses, chickens = [], []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append((i,j))
        elif graph[i][j] == 2:
            chickens.append((i,j))

def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

ans = 100_000_000
for combo in combinations(chickens, m):
    c_sum = 0
    for house in houses:
        c_sum += min(dist(house,chicken) for chicken in combo)
        if c_sum > ans: break

    ans = min(ans, c_sum)

print(ans)