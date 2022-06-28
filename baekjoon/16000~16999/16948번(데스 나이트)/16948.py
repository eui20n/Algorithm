# 데스 나이트
# 나이트가 있다, 이 나이트는 아래의 좌표중 하나로 움직인다
# (r-2,c-1), (r-2,c+1), (r,c-2), (r,c+2), (r+2,c-1),(r+2,c+1)
# 입력 첫줄에는 체스판의 크기 N과 그 다음 줄에는 현재 위치와 도착점이 주어진다
# 도착점까지 가는데 필요한 최소 연산을 구해라

from collections import deque

N = int(input())
start_end = list(map(int,input().split()))

start = start_end[0:2]
end = start_end[2:4]

graph = [[False for _ in range(N)] for _ in range(N)]

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]


def bfs(start,end):
    q = deque()
    q.append([start,0])
    graph[start[0]][start[1]] = True
    while q:
        p = q.popleft()
        if p[0][0] == end[0] and p[0][1] == end[1]:
            return p[1]
        for z in range(6):
            nx = p[0][0] + dx[z]
            ny = p[0][1] + dy[z]
            if 0 <= nx < N and 0 <= ny < N and not graph[nx][ny]:
                graph[nx][ny] = True
                q.append([[nx,ny],p[1] + 1])
    return -1

print(bfs(start,end))
    
    
    
    
    
    
