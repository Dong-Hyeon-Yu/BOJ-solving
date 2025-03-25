#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13458                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13458                          #+#        #+#      #+#     #
#    Solved: 2025/03/25 16:18:21 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

import math
import sys

n = int(sys.stdin.readline())
testers = list(map(int, sys.stdin.readline().split()))
b, c = tuple(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(n):
    if testers[i] > 0:
        testers[i] = max(0, testers[i]-b)
        cnt += 1
    # print(f"i={i}, after checking main {cnt}")
    if testers[i] > 0:
        cnt += math.ceil(testers[i] / c)
        testers[i] = 0
    # print(f"i={i}, after checking sub {cnt}")
print(cnt)


    




