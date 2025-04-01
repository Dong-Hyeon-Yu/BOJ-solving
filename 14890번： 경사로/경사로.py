#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14890                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14890                          #+#        #+#      #+#     #
#    Solved: 2025/04/01 16:59:44 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline
n, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def check_path(path):
    global L
    left, right = 0, 1
    len_path = len(path)
    slide = [False] * len_path
    while right < len_path:
        dist = path[left]-path[right]
        if dist == 0:
            left += 1
            right += 1
        elif abs(dist) > 1:
            return False
        else:
            if dist == 1:
                if right+L <= len_path:
                    for i in range(right, right+L):
                        if slide[i] or path[i] != path[right]:  # 경사로 구간은 동일 높이.
                            return False
                        slide[i] = True
                    left = right + L -1
                    right += L
                else:  # 길이 초과; 경사로 못 놈.
                    return False
            elif dist == -1:
                if right - L >= 0:
                    for i in range(right-L, right):
                        if slide[i] or path[i] != path[left]:
                            return False
                        slide[i] = True
                    left += 1
                    right += 1
                else:  # 인덱스가 음수가 있어야 경사로를 놓을 수 있음.
                    return False
    return True
                
ans = sum([1 for row in graph if check_path(row)])
ans += sum([1 for col in zip(*graph) if check_path(col)])

print(ans)



        

