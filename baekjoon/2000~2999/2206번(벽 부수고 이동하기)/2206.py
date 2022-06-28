# 벽 부수고 이동하기
# (0,0)에서 (R,C)까지 이동하는데 걸리는 최단 경로
# 그래프에서 0은 이동 가능한 칸, 1은 벽인데 벽은 딱 한번 부술 수 있음
# 이때 최단경로를 출력해라, 시작하는 칸과 끝나는 칸도 포함시킨다
# 만약 최단 경로가 없다면 -1을 출력해라

# 꼭 벽을 부술 필요는 없음

from collections import deque

R,C = map(int,input().split())
graph = [list(map(int,input())) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[[False for _ in range(C)],[False for _ in range(C)]] for _ in range(R)]

def bfs(x,y):
    q = deque()
    q.append([x,y,1,False])
    visited[x][0][y] = True
    while q:
        p = q.popleft()
        if p[0] == R-1 and p[1] == C - 1:
            return p[2]
        for z in range(4):
            nx = dx[z] + p[0]
            ny = dy[z] + p[1]
            if 0 <= nx < R and 0 <= ny < C:
                if p[3] == False: # 벽을 안부순 상태
                    if graph[nx][ny] == 1: # 벽을 만남
                        q.append([nx,ny,p[2]+1,True])
                        visited[nx][1][ny] = True
                    else: # 벽을 안만남
                        if not visited[nx][0][ny]: 
                            visited[nx][0][ny] = True
                            q.append([nx,ny,p[2]+1,False])
                else: # 벽을 부순 상태
                    if graph[nx][ny] == 0 and not visited[nx][1][ny]:
                        visited[nx][1][ny] = True
                        q.append([nx,ny,p[2]+1,True])
    return -1
    
print(bfs(0,0))


# 현재 위치에서 벽을 이미 부셨는데 앞에 1이 있는 경우 부술수 없음
# 이렇게 2차원으로 풀면 모든 경우를 다 보지 못함
# 3차원 정리 [x축][h축][y축]
# 3차원에서 봐야하는건 벽을 부순적이 있나 없나임 -> 각각의 방문처리 해줘야함
# 그리고 큐에 벽을 부순적이 있나 없나를 체크함
# 벽을 부순적이 없으면 방문처리에 안걸리게하기
# 만약에 벽을 부순적이 있던 없던 그 곳에 도달했는데 그 곳이 방문처리가 됬다는 소리는 이미 그 곳의 최단경로는 지금 온 경로가 아니라는 소리이다 -> 이 경우는 제외하면 된다
# 그 위치가 가장 먼저 도달한 것이 그 위치로 가는 최단 경로라는 소리이다