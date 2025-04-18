#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17779                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17779                          #+#        #+#      #+#     #
#    Solved: 2025/04/18 17:33:08 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import math

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
total = sum(map(sum, graph))

def cal_min(graph, x, y, d1, d2):
    global n, total

    population = [0 for _ in range(5)]
    temp_c = y
    for r in range(x + d1):  # 1구역 인구 합 구하기
        if r >= x:
            temp_c -= 1
        population[0] += sum(graph[r][0:temp_c + 1])

    temp_c = y - d1 - 1
    for r in range(x + d1, n):  # 3구역 인구 합 구하기
        population[2] += sum(graph[r][0:temp_c + 1])
        if r < x + d1 + d2:
            temp_c += 1

    temp_c = y + 1
    for r in range(x + d2 + 1):  # 2구역 인구 합 구하기
        if r > x:
            temp_c += 1
        population[1] += sum(graph[r][temp_c:])

    temp_c = y + d2
    for r in range(x + d2 + 1, n):  # 4구역 인구 합 구하기
        population[3] += sum(graph[r][temp_c:])
        if r <= x + d1 + d2:
            temp_c -= 1

    population[4] = total - sum(population)  # 5구역 인구 합 구하기
    return max(population) - min(population)


ans = math.inf

for x in range(n):
    for y in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if x + d1 + d2 >= n or y - d1 < 0 or y + d2 >= n:
                    continue
                else:
                    ans = min(cal_min(graph, x, y, d1, d2), ans)

print(ans)