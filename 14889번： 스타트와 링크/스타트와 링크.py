#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14889                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14889                          #+#        #+#      #+#     #
#    Solved: 2025/03/28 19:18:08 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def compute_team_power(team):
    global graph
    return sum(graph[i][j] + graph[j][i] for i, j in combinations(team, 2))

players = set(i for i in range(n))
ans = 10000000
for team_a in combinations(players, n//2):
    power_a = compute_team_power(team_a)
    team_b = players.difference(team_a)
    power_b = compute_team_power(team_b)
    ans = min(ans, abs(power_a - power_b))

print(ans)
