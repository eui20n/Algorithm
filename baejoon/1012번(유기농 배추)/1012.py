# 1012번 유기농 배추
# 배추를 심는데, 농약을 안쓰려면 배추흰지렁이가 있어야 한다
# 한 구역에 배추흰지렁이는 1마리만 있어도 된다
# 배추가 고르게 심어지지 않아서 구역이 여러개가 있다, 이때 필요한 배추지렁이의 수를 출력하면 된다
# 입력은 첫줄에 테스트케이스, 다음줄에는 배추밭의 가로길이, 세로길이, 배추가 심어져 있는 위치의 개수를 입력한다
# 그 다음 줄에는 배추의 위치가 입력이 된다

from collections import deque

T = int(input())
for i in range(T):
    M,N,K = map(int,input().split())
    
    graph = [list(map(int,input().split())) for _ in range(K)]
    
    mat = [[0] * M for _ in range(N)]
    visited = [[True] * M for _ in range(N)]
    
    for x in range(len(graph)):
        mat[graph[x][1]][graph[x][0]] = 1
        visited[graph[x][1]][graph[x][0]] = False
        
    N_M = [N,M]
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(N,M):
        q = deque([[N,M]])
        visited[graph[0][0]][graph[0][1]] = True
        while q:
            #print(q)
            p = q.popleft()
            for z in range(4):
                nx = p[0] + dx[z]
                ny = p[1] + dy[z]
                if (0 <= nx < N_M[0] and 0 <= ny < N_M[1]) and not visited[nx][ny] and mat[nx][ny] == 1:
                    #print('nx :',nx,'ny :',ny)
                    q.append([nx,ny])
                    visited[nx][ny] = True
        
    count = 0
    for x in range(N):
        for y in range(M):
            if visited[x][y] == False:
                bfs(x,y)
                count +=1
                
    print(count)
    