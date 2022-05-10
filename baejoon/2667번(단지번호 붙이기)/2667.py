# 단지번호붙이기
# 정사각형 모양의 지도에 1은 집이 있는 부분, 0은 집이 없는 부분이다
# 지도에서 연결되어 있는 곳을 찾아서 한 그룹으로 한다
# 이때 몇개의 그룹이 나오는지 출력해라
# 입력은 정사각형의 크기 N이 입력된 후, 지도(0과1)이 입력된다
# 출력은 그룹의 수와, 각 그룹의 단지가 몇개가 있는지 오름차순으로 출력하면 된다

N = int(input())
graph = [list(map(int,input())) for _ in range(N)]

visited = [[True] * N for _ in range(N)]
for n in range(N):
    for m in range(N):
        if graph[n][m] == 1:
            visited[n][m] = False
            
dx = [-1,1,0,0]
dy = [0,0,-1,1]
a = []
c = 1
b = []


def dfs(x,y):
    visited[x][y] = True
    fx,fy = x,y
    a.append(1)
    for z in range(4):
        nx = fx + dx[z]
        ny = fy + dy[z]
        if  0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(nx,ny)


count = 0
for x in range(N):
    for y in range(N):
        if visited[x][y] == False:
            dfs(x,y)
            if len(a) >= 1:
                b.append(len(a))
                a = []
            count +=1
        

b.sort()
if len(b) == 0:
    print(0)
    print(0)

else:
    for i in range(len(b)+1):
        if i == 0:
            print(count)
        else:
            print(b[i-1])

