# 섬의 개수
# 정사각형으로 이루어진 지도가 있다. 여기서 섬의 수를 세서 출력하면 된다
# 대각선도 연결이 되어 있는 경우다
# 입력은 첫줄에 가로와 세로, 그 다음 줄에는 지도가 입력이 된다(1은 땅, 0은 바다)
# 마지막 줄에 0 0 이 출력이 되면 출력이 끝이 나는 것이다
# 출력은 섬의 수를 출력하면 된다
import sys
sys.setrecursionlimit(1000000)

while True:
    W,H = map(int,input().split())
    if W == 0 and H == 0:
        break
    
    graph = [list(map(int,input().split())) for _ in range(H)]
    visited = [[True] * W for _ in range(H)]
    
    for x in range(H):
        for y in range(W):
            if graph[x][y] == 1:
                visited[x][y] = False
                
    dx = [-1,1,0,0,-1,1,-1,1]
    dy = [0,0,-1,1,1,-1,-1,1]
    
    def dfs(x,y):
        visited[x][y] = True
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and graph[nx][ny] == 1:
                dfs(nx,ny)
                
    count = 0
    
    for n in range(H):
        for m in range(W):
            if visited[n][m] == False:
                dfs(n,m)
                count +=1
                
    print(count)
                

            
    
    