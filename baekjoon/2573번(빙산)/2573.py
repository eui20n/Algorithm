# 빙산
# 빙산이 녹아서 두 부분으로 나누어지는데 걸리는 최소 시간을 구하는 문제
# 빙산은 물과 인접해 있으면 더 빨리 녹음(1당 1씩 녹음) -> 물에 인접해있지 않으면 녹지 않음
# 만약에 두 부분이상으로 나눠지지 않으면 0을 출력하면 됨
import sys
sys.setrecursionlimit((10**4)*2)

R,C = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    # 범위나 조건에 벗어나는 경우 바로 종
    if x <= 0 or x > R or y <= 0 or y > C or graph[x][y] == 0 or visited[x][y]:
        return
    
    # 방문처리
    visited[x][y] = True
    
    # 네방향 탐색
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    
    count_n = 0
    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if graph[nx][ny] == 0:
            count_n +=1
    if graph[x][y] <= count_n:
        graph[x][y] = '*' # 동시 변하게 하고 싶어서 0이 아니라 임의의 문자로 대체함
    else:
        graph[x][y] -= count_n
                   
time = 0        
while True:
    count_1 = 0
    visited = [[False for _ in range(C)] for _ in range(R)]
    count = 0
    for x in range(R):
        for y in range(C):
            # 임의의 문자를 0으로 다시 바꿔주고, 0인 부분은 방문처리 해줌
            if graph[x][y] == '*':
                graph[x][y] = 0
            if graph[x][y] == 0:
                visited[x][y] = True
                count +=1
                
    # 만약에 2덩이로 나누어 지는 빙산이 없을때 0을 출력 -> 0의 개수가 R*C한것과 같으면 출력
    if count == R*C:
        print(0)
        break
    
    
    for x in range(R):
        for y in range(C):
            if visited[x][y] == False:
                dfs(x,y)
                count_1 +=1
                
    time +=1
    if count_1 >= 2:
        print(time-1)
        break
                
# time-1 을 해준이유 
# count_1은 빙산이 덩어리로 나누어질때를 세는게 아니라 dfs한 횟수를 카운트함 -> 만약 2덩이로 나눠졌어도 그건 dfs를 한 후 나누어진것, 즉 한 번 더 해야 2덩이인걸 인식을 함 -> 한번 더 하니까 time - 1 을 해줌
    