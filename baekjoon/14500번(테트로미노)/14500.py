# 테트로미노
# 크기가 1 x 1인 정사각형 여러 개 이어서 붙인 도형이 있다, 이 도형은 아래의 규칙을 따른다
# 1. 정사각형은 서로 겹치면 안된다
# 2. 도형은 모두 연결되어 있어야 한다
# 3. 정사각형의 변끼리 연결되어 있다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안된다
# 테트로미노란 1 x 1 정사각형을 4개를 붙인 것이다
# N x M 종이 각 칸에 숫자가 적혀있다. 이 종이위에 테트로미노를 1개 올려서 겹쳐진 정수의 합이 최대인 경우를 출력해라

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

# 위에서 아래를 보기때문에 아래에에서 위를 보는 경우는 빼고 방향을 설정해줌
dx = [1,0,0]
dy = [0,-1,1]

# 나의 실력으로는 dfs로 ㅗ 모양을 구현 못해서 직접 만듬
fx = [[0,0,0,1],[0,0,0,-1],[0,0,0,1],[0,0,0,-1],[0,1,2,1],[0,1,2,1],[0,-1,-2,-1],[0,-1,-2,-1]]
fy = [[0,1,2,1],[0,1,2,1],[0,-1,-2,-1],[0,-1,-2,-1],[0,0,0,1],[0,0,0,-1],[0,0,0,1],[0,0,0,-1]]

# shape_f함수로 ㅗ모양 구현
def shape_f(x,y):
    max_num = 0
    for i in range(8):
        num = 0
        for z in range(4):
            if 0 <= x + fx[i][z] < N and 0 <= y + fy[i][z] < M:
                num += graph[x+fx[i][z]][y+fy[i][z]]
            else:
                break
        if max_num < num:
            max_num = num
    return max_num
            

# dfs로 나머지 모양을 봄
def dfs(x,y):
    num.append(graph[x][y])
    visited[x][y] = True
    # 만약에 num의 길이가 4이면 그 값들을 더해주고 max_list에 있던 값보다 크면 새로 갱신해줌
    if len(num) == 4:
        if max_list[0] < sum(num):
            max_list[0] = sum(num)
        return
    for z in range(3):
        nx = dx[z] + x
        ny = dy[z] + y
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            dfs(nx,ny)
            # dfs함수에서 나오면 num에 늦게 들어간거 빼주고 방문처리도 안한걸로 해줌
            num.pop()
            visited[nx][ny] = False
    # 함수가 아예 끝나면 제일 처음 것도 방문처리가 안했던 걸로 해줌
    visited[x][y] = False

# 최대값을 가질 리스트의 첫번째 값을 0으로 해줌
max_list = [0]         
num = []
visited = [[False for _ in range(M)] for _ in range(N)]
# 그래프의 원소 하나씩 다 보기 위해서 이중for문
for x in range(N):
    for y in range(M):
        num = []
        dfs(x,y)
        # 만약에 shape_f의 값이 최대값보다 크면 바꿔주고 아니면 안바꿈
        if max_list[0] < shape_f(x,y):
            max_list[0] = shape_f(x,y)

# 최대값을 출력
print(max_list[0])