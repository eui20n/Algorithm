# 연구소
# 연구소에 바이러스가 유출되어 퍼지는걸 막기 위해서 연구소에 벽을 세우려고 한다
# 연구소의 크기는 N x M 인 직사각형으로 나타낼 수 있고, 직사각형은 1 x 1인 정사각형으로 나누어져 있다
# 연구소는 빈칸, 벽으로 이루어져 있고 벽은 칸 하나를 가득 차지한다
# 일부 칸에는 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다
# 벽을 3개 세운뒤 바이러스가 퍼질 수 없는 곳을 안전영역이라고 한다
# 이때 안전영역의 최대값을 구해라

from collections import deque
from copy import deepcopy


N,M = map(int,input().split())
wall_1 = []
for _ in range(N):
    a = list(map(int,input().split()))
    wall_1.append(a)


dx = [-1,1,0,0]
dy = [0,0,-1,1]

start = []
change_wall = []
max_list = []
for x in range(N):
    for y in range(M):
        if wall_1[x][y] == 2:
            start.append([x,y])
        if wall_1[x][y] == 0:
            change_wall.append([x,y])
            
def count_wall(graph):
    count = 0
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 0:
                count +=1
    return count

def wall():
    for x in range(len(change_wall)):
        for y in range(x+1,len(change_wall)):
            for z in range(y+1,len(change_wall)):
                wall_1[change_wall[x][0]][change_wall[x][1]] = 1
                wall_1[change_wall[y][0]][change_wall[y][1]] = 1
                wall_1[change_wall[z][0]][change_wall[z][1]] = 1
                #for i in wall:
                #    print(i)
                #print('-------------------------------')
                bfs(start,wall_1)
                wall_1[change_wall[x][0]][change_wall[x][1]] = 0
                wall_1[change_wall[y][0]][change_wall[y][1]] = 0
                wall_1[change_wall[z][0]][change_wall[z][1]] = 0

                
def bfs(start,wall_1):
    graph = deepcopy(wall_1)
    q = deque()
    q.append(start)
    while q:
        p = q.popleft()
        for x in p:
            for z in range(4):
                nx = x[0] + dx[z]
                ny = x[1] + dy[z]
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                    q.append([[nx,ny]])
                    graph[nx][ny] = 2
    
    max_list.append(count_wall(graph))

wall()
print(max(max_list))

# 3중 for문을 활용해서 벽을 세움
# 이 for문에 들어가는건 0인 부분만 들어가서 아무런 조건없이 그냥 돌려주어도 답이 나옴
