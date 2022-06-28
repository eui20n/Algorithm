# 내리막 길
# 직사각형 모양의 지도가 있다
# 각 칸에는 높이가 쓰여져 있다. 이동은 상하좌우 이웃한 곳끼리만 이동이 가능하다
# 시작점은 (0,0)이고 도착점은 가장 오른쪽 아래이다. 이때 높이가 낮은 곳으로만 이동하는 것이 목표이다.
# 이때 항상 내리막길로 가는 경우의 수를 구하여라
# 입력은 M by N 크기의 직사각형과 높이 행렬이 주어진다6

M,N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(M)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# dp로는 다음껄로 가는 걸 생각하고, 경우의 수를 세는것은 dfs가 하면됨
# 방문처리를 dp로 해주고, dfs에서는 그 길만 따라가면서 경우의 수 구하면 됨

dp = [[True]*N for _ in range(M)]
dp[0][0] = False

for m in range(M):
    for n in range(N):
        for z in range(4):
            nx = m + dx[z]
            ny = n + dy[z]          
            if m <= nx < M and n <= ny < N and not dp[m][n] and dp[nx][ny]:
                dp[nx][ny] = min(graph[m][n],graph[nx][ny])
                if dp[nx][ny] == graph[m][n]:
                    dp[nx][ny] = True
                else:
                    dp[nx][ny] = False
                    

# 일반적인 dfs로 하면 시간 초과가 걸리기 때문에 dp로 조금 손을 봐줘야함
def dfs(x,y):
    print(graph[x][y], end = ' ')
    dp[x][y] = True
    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nx < M and 0 <= ny < N and not dp[nx][ny]:
            dfs(nx,ny)

            

# 대 실패~
# 다른 생각은 옛날에 고등학생때 배웠던 길찾기 개념으로 접근하기
    
    
    
    
    