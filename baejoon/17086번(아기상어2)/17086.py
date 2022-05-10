# 아기상어2
# N x M 의 크기에 1 x 1 크기의 정사각형에 아기상어가 최대 1마리 존재한다
# 어떤 칸에서의 안전거리는 가장 가까운 아기상어와의 거리이다
# 이 때 안전거리의 최대값을 구해라

from collections import deque

R,C = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(R)]

dx = [-1,1,0,0,-1,1,1,-1]
dy = [0,0,-1,1,1,1,-1,-1]

max_value = []


def bfs(x,y):
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[x][y] = True
    q = deque()
    q.append([x,y,0])
    while q:
        p = q.popleft()
        if graph[p[0]][p[1]] == 1:
            max_value.append(p[2])
            return
        for z in range(8):
            nx = p[0] + dx[z]
            ny = p[1] + dy[z]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx,ny,p[2] + 1])
                


for x in range(R):
    for y in range(C):
        if graph[x][y] == 0:
            bfs(x,y)
print(max(max_value))
    
    


