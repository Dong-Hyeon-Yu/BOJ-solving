#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14501                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14501                          #+#        #+#      #+#     #
#    Solved: 2025/03/27 10:32:10 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]

def solution1(schedule):
    schedule = [(day, duration, price) for day, (duration, price) in enumerate(schedule) if day + duration <= n ]

    def check(combo):
        left = combo[0]
        for right in combo[1:]:
            if left[0]+left[1] > right[0]:
                return False
            left = right

        return True

    ans = 0
    for i in range(1, len(schedule)+1):
        for combo in combinations(schedule, i):
            if check(combo):
                ans = max(ans, sum([price for (_,_,price) in combo]))

    return ans


def solution2(schedule):
    dp = [0] * (n+1)  # dp[i]: i일까지 상담했을 때 얻을 수 있는 최대 이익
    for i in range(0, n):
        if i + schedule[i][0] <= n:
            dp[i + schedule[i][0]] = max(dp[i + schedule[i][0]], dp[i] + schedule[i][1])

        dp[i+1] = max(dp[i], dp[i+1])

    return dp[-1]


# print(solution1(schedule))
print(solution2(schedule))
