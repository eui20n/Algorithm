# 영역구하기
# M x N인 종이에 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어짐
# 이 분리된 영역의 개수와 넓이를 구해라
import sys
sys.setrecursionlimit(10**6)

M,N,K = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(K)]

graph = [[0 for _ in range(N)] for _ in range(M)]

for k in range(K):
    for y in range(paper[k][0],paper[k][2]):
        for x in range(paper[k][1],paper[k][3]):
            if graph[x][y] == 0:
                graph[x][y] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    graph[x][y] = 'x'
    
    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0:
            dfs(nx,ny)
    num[0] +=1

count = 0
result = []
for x in range(M):
    for y in range(N):
        num = [0]
        if graph[x][y] == 0:
            dfs(x,y)
            count +=1
            result.append(num[0])
            
result.sort()
print(count)
for x in result:
    print(x,end = ' ')
    