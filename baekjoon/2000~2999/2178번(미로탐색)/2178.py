# 미로 탐색
# N by M크기의 미로가 있다
# 1은 이동할 수 있는 칸이고, 0은 이동할 수 없는 칸이다
# (1,1)에서 출발해서 (N,M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하면 됨
# 처음 칸과 마지막 칸을 포함해서 출력하면 됨

from collections import deque
N,M = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(N,M):
    depth = 0
    q = deque([[0,0,depth]])
    visited[0][0] = True
    while q:
        p = q.popleft()
        depth = p[2]
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            if (0 <= nx < N and 0 <= ny < M) and not visited[nx][ny] and graph[nx][ny] == 1:
                q.append([nx,ny,depth+1])
                visited[nx][ny] = depth+1
                
    print(visited[N-1][M-1]+1)
                
bfs(N,M)
    
    
    