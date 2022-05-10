# 안전영역
# 각 지역의 높이가 있음, 장마철에 비가 오면 일정 높이는 물에 잠김
# 그 지역은 각 변의 길이가 N인 정사각형임
# 비에 잠기지 않은 지역이 안정영역임
# 이때 비에 양에 따라서 안전영역의 수가 달리지는데, 안전영역의 최대값을 구하라
# 입력은 첫줄에는 정사각형의 변 N, 다음줄 부터는 높이가 입력이 된다

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

# 최대 높이 구하기
h_max = 0
for x in range(N):
    for y in range(N):
        if graph[x][y] > h_max:
            h_max = graph[x][y]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,h): 
    visited[x][y] = True
    
    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] > h:
            dfs(nx,ny,h)
            
            

count = 0
max_count = []

for k in range(h_max+1):
    visited = [[True]*N for _ in range(N)]
    for n in range(N):
        for m in range(N):
            if graph[n][m] > k:
                visited[n][m] = False
                
    for x in range(N):
        for y in range(N):
            if visited[x][y] == False:
                dfs(x,y,k)
                count +=1
                
    max_count.append(count)
    count = 0
            
print(max(max_count))
            
    