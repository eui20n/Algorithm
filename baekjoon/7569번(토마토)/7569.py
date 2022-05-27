# 토마토
# 토마토가 M X N X H 의 통에 있다
# 이 토마토중 익은 토마토가 있고 안익은 토마토가 있다
# 익은 토마토의 위,아래,앞,뒤,왼쪽,오른쪽의 토마토는 하루가 지나면 익는다
# 이때 모든 토마토가 익는데 걸리는 최소 시간을 구해라
# 익은 토마토는 1, 안익은 토마토는 0, 토마토가 없으면 -1
# 모든 토마토가 익는데 걸리는 최소시간을 출력해라, 만약 처음부터 토마토가 다 익은 상태라면 0을 출력
# 토마토가 모두 다 익지 못하는 상황이면 -1을 출력

from collections import deque

M,N,H = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N*H)]
box = [[[0 for _ in range(M)]for _ in range(N)] for _ in range(H)]
first = []
for h in range(H):
    for x in range(N):
        for y in range(M):
            box[h][x][y] = graph[x+N*h][y]
            if graph[x+N*h][y] == 1:
                first.append([x,y,h])
                
dx = [-1,1,0,0]
dy = [0,0,-1,1]
dh = [-1,1]

def bfs(M,N,H):
    q = deque()
    depth = 0
    q.append([first,depth])
    while q:
        p = q.popleft()
        #print('--------------------')
        #print('q: ',q)
        #print('p: ',p)
        #print(box)
        for x in p[0]:
            for z in range(4):
                nx = dx[z] + x[0]
                ny = dy[z] + x[1]
                if 0 <= nx < N and 0 <= ny < M and box[x[2]][nx][ny] == 0:
                    box[x[2]][nx][ny] = 1
                    q.append([[[nx,ny,x[2]]],p[1] + 1])
            for z in range(2):
                nh = dh[z] + x[2]
                if 0 <= nh < H and box[nh][x[0]][x[1]] == 0:
                    box[nh][x[0]][x[1]] = 1
                    q.append([[[x[0],x[1],nh]],p[1] + 1])
        depth = p[1]
        
    for h in range(H):
        for x in range(N):
            for y in range(M):
                if box[h][x][y] == 0:
                    depth = -1
                    break
    print(depth)
    
bfs(M,N,H)
            
            
            
            
            
            
            
            
            