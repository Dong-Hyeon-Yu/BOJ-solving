#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17140                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17140                          #+#        #+#      #+#     #
#    Solved: 2025/04/15 17:09:16 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
from collections import defaultdict
input = sys.stdin.readline

r,c,k = map(int, input().split())
r-=1
c-=1

A=[list(map(int, input().split())) for _ in range(3)]

def compare(a, b):
    a_key, a_value = a
    b_key, b_value = b
    if a_value == b_value:
        return a_key < b_key
    else:
        return a_value < b_value

def sort_row(array):
    tmp = []
    max_row = 0
    for row in array:
        counter = defaultdict(int)
        for item in row:
            counter[item] += 1
        if counter.get(0): del counter[0]

        new_row = [v for tup in sorted(counter.items(), key=lambda x: (x[1],x[0])) for v in tup]
        max_row = max(max_row,len(new_row))
        if len(new_row) > 100:
            new_row = new_row[:100]
        tmp.append(new_row)
    
    for row_idx in range(len(tmp)):
        if len(tmp[row_idx]) < max_row:
            tmp[row_idx] += [0]*(max_row-len(tmp[row_idx]))

    return tmp

def transpose(array):
    return [list(new_row) for new_row in zip(*array)]

def sort_col(array):
    return transpose(sort_row(transpose(array)))

# import pprint
time = 0
while time < 100:
    if r<len(A) and c<len(A[0]) and A[r][c] == k:
        print(time)
        break

    if len(A) >= len(A[0]):
        A = sort_row(A)
        # pprint.pp(A)
    else:
        A = sort_col(A)
        # pprint.pp(A)

    time += 1

if time == 100:
    print(-1)