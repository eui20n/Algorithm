# 적록색약
# 한 변의 길이가 N인 정사각형에 RGB중 하나가 칠해져 있다
# 각 RGB의 구역을 출력하면 된다
# 여기서 적록색약이 보는 경우도 같이 출력하면 된다(R과 G를 같은 색상으로 본다)
# 입력은 첫줄에는 정사각형의 한변, 그 다음에는 RGB가 입력이 된다
# 출력은 일반 사람이 본 RGB구역과 적록색약이 본 RGB구역이 출력이 되면 된다

import sys
sys.setrecursionlimit(100000)

N = int(input())
graph = [list(map(str,input())) for _ in range(N)]

# R = 0, B = 1, G = 2
for x in range(N):
    for y in range(N):
        if graph[x][y] == 'R':
            graph[x][y] = 0
        elif graph[x][y] == 'B':
            graph[x][y] = 1
        else:
            graph[x][y] = 2
            
dx = [-1,1,0,0]
dy = [0,0,-1,1]


# 일반사람인 경우
def dfs(x,y,c):
    if c == 0:
        graph[x][y] = 'R'
    elif c == 1:
        graph[x][y] = 'B'
    elif c == 2:
        graph[x][y] = 'G'
        
    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nx < N and 0 <= ny < N and type(graph[nx][ny]) == int and graph[nx][ny] == c:
            dfs(nx,ny,c)

            
count = 0
for c in range(3):
    for x in range(N):
        for y in range(N):
            if graph[x][y] == c:
                dfs(x,y,c)
                #print('x :',x,'y :',y,'c :',c)
                count +=1
                
# 적록색약인 경우

# B = 1, R-G = 0
for x in range(N):
    for y in range(N):
        if graph[x][y] == 'B':
            graph[x][y] = 1
        else:
            graph[x][y] = 0

def dfs_RRB(x,y,c):
    if c == 0:
        graph[x][y] = 'RG'
    elif c == 1:
        graph[x][y] = 'B'
    
    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nx < N and 0 <= ny < N and type(graph[nx][ny]) == int and graph[nx][ny] == c:
            dfs(nx,ny,c)
            
count_RG = 0
for c in range(2):
    for x in range(N):
        for y in range(N):
            if graph[x][y] == c:
                dfs_RRB(x,y,c)
                count_RG +=1
    
        
print(count,count_RG)
        
        
        
        
        
        
