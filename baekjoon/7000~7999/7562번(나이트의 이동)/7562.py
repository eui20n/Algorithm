# 나이트의 이동
# 나이트가 현재 위치에서 원하는 위치로 이동하면 됨
from collections import deque

T = int(input())

dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]

def bfs(start,end,N):
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[start[0]][start[1]] = True
    q = deque()
    q.append([start,0])
    while q:
        p = q.popleft()
        if p[0][0] == end[0] and p[0][1] == end[1]:
            return p[1]
        for z in range(8):
            nx = p[0][0] + dx[z]
            ny = p[0][1] + dy[z]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([[nx,ny],p[1]+1])


for _ in range(T):
    N = int(input())
    loc = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    print(bfs(loc,arr,N))
    
    