#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 19237                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/19237                          #+#        #+#      #+#     #
#    Solved: 2025/04/28 15:12:54 by ydh9516       ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

N,M,K = map(int, input().split())

directions = [(-1,0),(1,0),(0,-1),(0,1)]

class Smell:
    def __init__(self, shark, k):
        self.lifetime = k
        self.owner = shark

class Shark:
    K = K
    TOTAL_NUM = M
    
    def __init__(self, id):
        self.id = id
        self.alive = True
        self.moves = 0
        self.r, self.c = (0,0)
        self.d = 0
    
    def set_location(self, r,c):
        self.r = r
        self.c = c
    
    def set_direction(self, d):
        self.d = d
    
    def set_priority(self, priority):
        self.priority = priority

    def make_smell(self) -> Smell:
        if self.alive:
            return Smell(self, K)
    
    def move(self, smell_info, shark_info):
        if not self.alive: return

        success = False
        candidate = None
        for nd in self.priority[self.d]:
            nr = self.r + directions[nd][0]
            nc = self.c + directions[nd][1]

            if not (0<=nr<N and 0<=nc<N): continue
            if smell_info[nr][nc]: 
                if smell_info[nr][nc].owner is self and candidate is None:
                    candidate = (nr,nc,nd)
                continue

            candidate = (nr,nc,nd)
            success = True
            break

        self.moves += 1
        if shark_info[self.r][self.c] is self:
            shark_info[self.r][self.c] = None

        if success:
            nr, nc, nd = candidate
            # many sharks in a single grid.
            if another_shark:=shark_info[nr][nc]:  
                if another_shark.moves == self.moves:  # fail
                    self.alive = False
                    Shark.TOTAL_NUM -= 1
                    return

            # at this point, success to move
            shark_info[nr][nc] = self
            self.r, self.c, self.d = nr, nc, nd

        elif not success and candidate:
            self.r, self.c, self.d = candidate
            shark_info[self.r][self.c] = self
            

sharks = [None]+[Shark(i) for i in range(1,M+1)]

# set location
sgraph = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if sgraph[i][j] != 0:
            sharks[sgraph[i][j]].set_location(i,j)
            sgraph[i][j] = sharks[sgraph[i][j]]
        else:
            sgraph[i][j] = None

# set directions
for i,d in enumerate(list(map(int, input().split()))):
    sharks[i+1].set_direction(d-1)

# set priority
for i in range(1,M+1):
    sharks[i].set_priority([list(map(lambda x: int(x)-1, input().split())) for _ in range(4)])

smell_info = [[None] * N for _ in range(N)]

# smell
for i in range(1,M+1):
    if sharks[i].alive:
        smell_info[sharks[i].r][sharks[i].c] = sharks[i].make_smell()


time = 1
while time < 1001:
    # move
    for i in range(1,M+1):
        sharks[i].move(smell_info, sgraph)

    if Shark.TOTAL_NUM == 1:
        print(time)
        break

    # decrease each smell's lifetime
    for i in range(N):
        for j in range(N):
            if smell_info[i][j]:
                if smell_info[i][j].lifetime == 1:
                    smell_info[i][j] = None
                else:
                    smell_info[i][j].lifetime -= 1
    
    # smell
    for i in range(1,M+1):
        if sharks[i].alive:
            smell_info[sharks[i].r][sharks[i].c] = sharks[i].make_smell()

    time += 1

if time == 1001:
    print(-1)
    