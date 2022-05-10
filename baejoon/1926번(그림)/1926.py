# 그림
# 그림중 가장 넓이가 넓은 것을 출력하면 됨
# 신경써야할 것은 그림은 가로 세로 로 연결되어 있음, 대각선으로는 연결안되어 있음
# 출력은 그림의 개수와 가장 넓이가 큰 그림
import sys
sys.setrecursionlimit(10**6)

R,C = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
size = [] # 넓이를 담을 리스트


visited = [[True]*C for _ in range(R)]
for x in range(R):
    for y in range(C):
        if graph[x][y] == 1:
            visited[x][y] = False

def dfs(x,y):
    visited[x][y] = True
    sum_list[0] +=1
    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx,ny)
            

count = 0
for x in range(R):
    for y in range(C):
        sum_list = [0]
        if visited[x][y] == False:
            dfs(x,y)
            count +=1
            size.append(sum_list[0])
    
    
print(count)
if len(size) == 0:
    print(0)
else:
    print(max(size))
    
    
#---------------------------------------------------------------------------------------------------
# bfs

from collections import deque

R,C = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
size = [] # 넓이를 담을 리스트


visited = [[True]*C for _ in range(R)]
for x in range(R):
    for y in range(C):
        if graph[x][y] == 1:
            visited[x][y] = False

def bfs(x,y):
    visited[x][y] = True
    q = deque([[x,y]])
    count = 1
    while q:
        p = q.popleft()
        for z in range(4):
            nx = p[0] + dx[z]
            ny = p[1] + dy[z]
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == 1 and not visited[nx][ny]:
                q.append([nx,ny])
                visited[nx][ny] = True
                count +=1
    size.append(count)
    
count = 0
for x in range(R):
    for y in range(C):
        if visited[x][y] == False:
            dfs(x,y)
            count +=1
            
print(count)
if len(size) == 0:
    print(0)
else:
    print(max(size))
                
    