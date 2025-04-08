#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 16235                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/16235                          #+#        #+#      #+#     #
#    Solved: 2025/04/08 18:34:51 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import defaultdict

input = sys.stdin.readline
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]  # 추가되는 양분의 양
graph = [[5] * N for _ in range(N)]

tree_map = defaultdict(lambda: defaultdict(int))
for _ in range(M):
    x, y, z = map(int, input().split())
    tree_map[(x-1,y-1)][z] += 1


def process_spring():
    global tree_map, graph
    dead_tree_map = defaultdict(lambda: defaultdict(int))

    for (r,c), trees in tree_map.items():
        tmp = defaultdict(int)
        for age in sorted(list(trees)):
            # print(f"({r},{c})", age, trees[age])
            if graph[r][c] >= age:
                cnt = min(trees[age], graph[r][c]//age)
                graph[r][c] -= cnt*age
                
                tmp[age+1] += cnt
                if cnt < trees[age]:
                    dead_tree_map[(r,c)][age] += trees[age]-cnt
            else:
                dead_tree_map[(r,c)][age] += trees[age]

            del trees[age]
        
        for age, cnt in tmp.items():
            if cnt:
                trees[age] += cnt


    return dead_tree_map

def process_summer(dead_tree_map):
    global graph
    for (r,c), trees in dead_tree_map.items():
        for age, cnt in trees.items():
            graph[r][c] += (age//2)*cnt

adjacent = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
def process_fall():
    global tree_map, graph

    for r,c in list(tree_map):  
        num_of_multiples_of_five = sum([cnt for age, cnt in tree_map[(r,c)].items() if age%5==0])

        if num_of_multiples_of_five == 0: continue

        for dr, dc in adjacent:
            nr, nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<N:
                tree_map[(nr,nc)][1] += num_of_multiples_of_five

def process_winter():
    global graph, A
    for i in range(N):
        for j in range(N):
            graph[i][j] += A[i][j]


## sol 2: deque를 활용한 풀이법
# from collections import deque
# tree_map = defaultdict(lambda: deque())
# for _ in range(M):
#     x, y, z = map(int, input().split())
#     tree_map[(x-1,y-1)].append(z)

# def process_spring():
#     global tree_map, graph
#     dead_tree_map = {}

#     for (r,c), trees in tree_map.items():
#         for i in range(len(trees)):
#             if graph[r][c] >= trees[i]:
#                 graph[r][c] -= trees[i] 
#                 trees[i] += 1
#             else:
#                 tmp = list(trees)
#                 dead_tree_map[(r,c)] = tmp[i:]
#                 tree_map[(r,c)] = deque(tmp[:i])
#                 break

#     return dead_tree_map

# def process_summer(dead_tree_map):
#     global graph
#     for (r,c), trees in dead_tree_map.items():
#         for tree_age in trees:
#             graph[r][c] += tree_age // 2

# adjacent = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
# def process_fall():
#     global tree_map, graph

#     for r,c in list(tree_map):  
#         num_of_multiples_of_five = len([True for tree in tree_map[(r,c)] if tree%5==0])

#         if num_of_multiples_of_five == 0: continue

#         for dr, dc in adjacent:
#             nr, nc = r+dr, c+dc
#             if 0<=nr<N and 0<=nc<N:
#                 tree_map[(nr,nc)].extendleft([1]*num_of_multiples_of_five)

# def process_winter():
#     global graph, A
#     for i in range(N):
#         for j in range(N):
#             graph[i][j] += A[i][j]

import pprint


DEBUG=False#True

while K:
    if DEBUG:
        print(K, "year left!")

    dead_tree_map = process_spring()
    if DEBUG:
        print("Dead trees after spring:" )
        pprint.pp(dead_tree_map)
        print("Living trees after spring:",)
        pprint.pp(tree_map)
    if dead_tree_map:
        process_summer(dead_tree_map)
    if DEBUG:
        print("nutrition after summer: ")
        pprint.pp(graph)
    process_fall()
    if DEBUG:
        print("trees after fall:")
        pprint.pp(tree_map)
    process_winter()
    if DEBUG:
        print("trees after winter:")
        pprint.pp(graph)
        print("totol num of trees:",sum([sum(trees.values()) for trees in tree_map.values()]))
        print("")
    K -= 1

print(sum([sum(trees.values()) for trees in tree_map.values()]))