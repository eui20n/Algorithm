# 전쟁 - 전투
# 영역을 나누고, 그 영역의 제곱을 한걸 더하면 됨

# 이거 신경쓰기, 문제가 반대로 되어있음;;
C,R = map(int,input().split())
graph = [list(map(str,input())) for _ in range(R)] # 그래프 입력받음

# 방향 벡터 설정
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 영역별로 숫자를 받을 리스트를 미리 만듬
num = [[],[]]

# dfs함수 만듬
def dfs(x,y,visited):
    global power # 계산을 편하게 하기 위해서 전역변수로 받아줌
    power+=1 # dfs 한번 실행한거면 1씩 더해줌
    visited[x][y] = True # 현재 위치 방문처리
    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]: # 만약에 조건에 안맞으면 이미 방문했거나 적임
            dfs(nx,ny,visited) # 재귀 호출
            
visited_W = [[False for _ in range(C)] for _ in range(R)] # W에 대해서 방문처리 리스트 생성
visited_B = [[False for _ in range(C)] for _ in range(R)] # B에 대해서 방문처리 리스트 생성

# 각 방문처리 리스트에 반대가 되는걸 True로 해줌 -> True로 하면 함수가 실행이 안됨
for x in range(R):
    for y in range(C):
        if graph[x][y] == 'W':
            visited_B[x][y] = True
        if graph[x][y] == 'B':
            visited_W[x][y] = True
            
# 조건에 맞게 함수를 실행해줌
for x in range(R):
    for y in range(C):
        # 만약에 W가 방문을 안했으면 실행해줌 -> 위에서 B는 True로 했기때문에 B는 실행안됨
        if not visited_W[x][y]:
            power = 0
            dfs(x,y,visited_W)
            num[0].append(power**2)
        # 위와 동일
        if not visited_B[x][y]:
            power = 0
            dfs(x,y,visited_B)
            num[1].append(power**2)
            
# 마지막으로 더해서 출력해줌            
for x in num:
    print(sum(x),end = ' ')

            