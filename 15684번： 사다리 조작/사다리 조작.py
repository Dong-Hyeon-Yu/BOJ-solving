#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15684                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15684                          #+#        #+#      #+#     #
#    Solved: 2025/04/02 19:03:29 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())

ladders = [[False] * (n+1) for _ in range(h+1)]
for _ in range(m):
    a, b = map(int, input().split())
    ladders[a][b] = True

def test():
    cnt = 0
    for i in range(1, n+1): # 처음 시작할 사다리 번호
        start_num = i   
        for j in range(1, h+1):
            if ladders[j][start_num]:
                start_num += 1
            elif ladders[j][start_num-1]:
                start_num -= 1    
        if i == start_num:
            cnt += 1
    return cnt


def dfs(cnt, x, c):
    
    global answer
    if answer <= cnt:   # 가로선을 정답보다 많이 만든 경우 확인 필요 x
        return
    if num_of_match:=test():     
        if (3-cnt)*2 < n-num_of_match:
            return
        if num_of_match == n:
            answer = min(answer, cnt)
            return
    if cnt == 3:
        return
    for i in range(x, h+1):
        nc = c if i == x else 1
        for j in range(nc, n):
            if not ladders[i][j] and not ladders[i][j+1]: 
                ladders[i][j] = True
                dfs(cnt + 1, i, j)
                ladders[i][j] = False

answer = 4
dfs(0,1,1)
print(-1 if answer>3 else answer)