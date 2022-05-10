# 토마토
# 이전에 있던 토마토 문제의 2차원 형태

from collections import deque

M,N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

start = []
for x in range(N):
    for y in range(M):
        if graph[x][y] == 1:
            start.append([x,y])
            
def bfs(start):
    q = deque()
    time = 0
    q.append([start,time])
    while q:
        p = q.popleft()
        time = p[1]
        for x in p[0]:
            for z in range(4):
                nx = x[0] + dx[z]
                ny = x[1] + dy[z]
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    q.append([[[nx,ny]],p[1] + 1])
    for x in range(N):
        for y in range(M):
            if graph[x][y] == 0:
                return -1
    return time
        
print(bfs(start))
        
        