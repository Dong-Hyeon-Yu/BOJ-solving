#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 17837                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/17837                          #+#        #+#      #+#     #
#    Solved: 2025/04/18 17:33:26 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# chess : 현재 말의 위치 정보를 나타내는 리스트(3차원)
chess = [[[] for _ in range(N)] for _ in range(N)]
# pieces : 말의 위치와 방향을 저장하는 리스트(1차원)
pieces = []

for i in range(K):
    x, y, d = map(int, sys.stdin.readline().split())
    pieces.append([x - 1, y - 1, d - 1])
    chess[x - 1][y - 1].append(i)

def change_dir(direction):
    if direction in [0, 2]:
        direction += 1
    elif direction in [1, 3]:
        direction -= 1
    else:
        pass

    return direction

def solution(piece_num):
    x, y, d = pieces[piece_num]
    nx = x + dx[d]
    ny = y + dy[d]

    # 이동하려는 칸이 체스판을 벗어나거나 파란색 칸인 경우
    if (nx < 0) or (nx >= N) or (ny < 0) or (ny >= N) or board[nx][ny] == 2:
        # 방향을 반대로 전환
        d = change_dir(d)
        # 현재 말의 이동 방향 정보를 업데이트
        pieces[piece_num][2] = d

        # 전환된 방향으로 한 칸 이동하기 위해 세팅
        nx = x + dx[d]
        ny = y + dy[d]

        # 방향을 반대로 하고 한 칸 이동하려는 칸이 체스판을 벗어나거나 파란색 칸인 경우
        if (nx < 0) or (nx >= N) or (ny < 0) or (ny >= N) or board[nx][ny] == 2:
            return True

    # 현재 이동하려는 말 위에 쌓여있는 말들을 추출(자신 포함)
    carry = []
    piece_index = chess[x][y].index(piece_num)
    carry.extend(chess[x][y][piece_index:])


    # 이동하려는 칸이 빨간색인 경우 이동하는 말과 그 위에 쌓여있는 말의 순서를 뒤집는다
    if board[nx][ny] == 1:
        carry = carry[::-1]

    # 이동한 말들에 대해 위치 정보를 업데이트
    for piece in carry:
        pieces[piece][0], pieces[piece][1] = nx, ny

    # 이동하는 말들을 이동한 칸에 추가
    chess[nx][ny].extend(carry)
    # 이동하는 말들을 기존 위치에서 제외시킴
    chess[x][y] = chess[x][y][:piece_index]

    # 이동 후에 이동한 위치의 말들의 개수가 4개 이상이라면 게임 종료
    if len(chess[nx][ny]) >= 4:
        return False

    return True


turn = 0
while True:
    if turn > 1000:
        print(-1)
        break

    flag = False
    for i in range(K):
        if solution(i) == False:    # True: 정상적으로 말이 이동한 경우 / False: 말이 이동한 후 4개 이상 쌓인 경우
            flag = True
            break

    turn += 1

    if flag:
        print(turn)
        break