# 보물섬
# 보물 지도가 주어진다
# 위에서 주어진 보물지도에서 보물의 위치는 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지에 있다
# 이때 보물이 있는 육지의 최단경로를 구하여라
from collections import deque

R,C = map(int,input().split())
treasure = [list(map(str,input())) for _ in range(R)]
            
dx = [-1,1,0,0]
dy = [0,0,-1,1]
            
def bfs(x,y):
    visited = [[True for _ in range(len(treasure[0]))] for _ in range(len(treasure))]
    for r in range(len(treasure)):
        for c in range(len(treasure[0])):
            if treasure[r][c] == 'L':
                visited[r][c] = False
            
    visited[x][y] = True
    q = deque()
    time = 0
    q.append([x,y,time])
    while q:
        p = q.popleft()
        if time <= p[2]:
            time = p[2]
        for z in range(4):
            nx = p[0] + dx[z]
            ny = p[1] + dy[z]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx,ny,p[2]+1])
    return time
                    
time = []
for x in range(R):
    for y in range(C):
        if treasure[x][y] == 'L':
            time.append(bfs(x,y))
print(max(time))
            
    