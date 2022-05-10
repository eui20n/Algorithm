# 탈출
# R 행 C열로 이루어진 숲의 지도가 있다
# 이 지도에 비어있는 곳은 '.', 물이 있는 곳은 '*', 돌은 'X'이다
# D로 가야하고, 현재위치는 S이다
# 매 분마다 현재 칸에서 동서남북중 한 칸 이동 가능하고 물도 매 분마다 비어있는 곳으로 확장한다
# 물이 있는 칸과 인접해있는 비어있는 칸은 물이 차게 된다
# 돌이 있는 곳은 가지 못한다, 물도 역시 가지 못한다
# 도착점 역시 물은 가지 못한다
# 도착점에 가는데 걸리는 최소시간을 구해라
# 만약에 탈출을 못한다면 KAKTUS 출력

from collections import deque
R,C = map(int,input().split())
graph = [list(input()) for _ in range(R)]

visited = [[False] * C for _ in range(R)]
for x in range(R):
    for y in range(C):
        if graph[x][y] == '*' or graph[x][y] == 'X':
            visited[x][y] = True
        if graph[x][y] == 'D':
            d_x = x
            d_y = y
        if graph[x][y] == 'S':
            p_x = x
            p_y = y
            
dx = [-1,1,0,0]
dy = [0,0,-1,1]
p_list = []

def bfs(p_x,p_y,d_x,d_y):
    depth = 0
    count = 0
    q = deque([[p_x,p_y,depth]])
    visited[p_x][p_y] = True
    while q:
        p = q.popleft()
        p_list.append(p)
        if p[0] == d_x and p[1] == d_y:
            #print(p[2])
            break
        if p[2] > count:
            changeWater()
            changeStar()
            count = p[2]
        if graph[p[0]][p[1]] == '*':
            pass
        else:
            for z in range(4):
                nx = p[0] + dx[z]
                ny = p[1] + dy[z]
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and graph[nx][ny] != '*' and graph[nx][ny] != 'o' and graph[nx][ny] != 'O' and graph[nx][ny] != 'X':
                    visited[nx][ny] = True
                    q.append([nx,ny,p[2]+1])

    
    
# 물이랑 고슴도치랑 같은 위치에 있어도 됨
    
def changeWater():
    r = len(graph)
    c = len(graph[0])
    counting = countingStar()
    for x in range(r):
        for y in range(c):
            if graph[x][y] == '*':
                counting -= 1
                if counting < 0:
                    break
                graph[x][y] = "o" # 아래에서 *이 되기 때문에 바꾸지 않으면 또 *이 반복됨
                for z in range(4):
                    nx = x + dx[z]
                    ny = y + dy[z]
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != "D" and graph[nx][ny] != "X" and graph[nx][ny] != 'o':
                        graph[nx][ny] = "O"
                        
def countingStar():
    r = len(graph)
    c = len(graph[0])
    counting = 0
    for x in range(r):
        for y in range(c):
            if graph[x][y] == '*':
                counting += 1
    return counting

def changeStar():
    r = len(graph)
    c = len(graph[0])
    for x in range(r):
        for y in range(c):
            if graph[x][y] == 'O':
                graph[x][y] = '*'

            

bfs(p_x,p_y,d_x,d_y)
if p_list[len(p_list)-1][0] == d_x and p_list[len(p_list)-1][1] == d_y:
    print(p_list[len(p_list)-1][2])
else:
    print("KAKTUS")


