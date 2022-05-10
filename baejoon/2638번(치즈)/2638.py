# 치즈
# N x M 의 모눈종이 위에 아주 얇은 치즈가 있다, 이 치즈는 천천히 녹는다
# 4변중 2변 이상이 공기와 접촉하면 한시간만에 녹아 없어진다
# 그림에서는 C로 표시된다
# 하지만 내부에 있는 공기는 공기와의 접촉으로 치지 않는다
# 치즈가 모두 녹아 없어지는데 걸리는 정확한 시간을 구해라

from collections import deque

R,C = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for x in range(R):
    graph[x][0] = '.'
    graph[x][C-1] = '.'
for x in range(C):
    graph[0][x] ='.'
    graph[R-1][x] = '.'
    
def bfs_wall():
    """ 치즈를 제외하고 -1이 닿은 부분은 -1로 바꿔주는 함수, 외부를 나누는 함수"""
    visited = [[False for _ in range(C)] for _ in range(R)]
    q = deque()
    q.append([0,0])
    while q:
        p = q.popleft()
        for z in range(4):
            nx = p[0] + dx[z]
            ny = p[1] + dy[z]
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = '.'
                q.append([nx,ny])

def good_bye_cheese():
    ''' 녹는 치즈를 찾아주고 녹이는 함수 '''
    for x in range(R):
        for y in range(C):
            if graph[x][y] != 1:
                pass
            else:
                count = 0
                for z in range(4):
                    if graph[x + dx[z]][y + dy[z]] == '.':
                        count +=1
                if count >= 2:
                    graph[x][y] = 'o' # 녹을 치즈
                    
    for x in range(R):
        for y in range(C):
            if graph[x][y] == 'o':
                graph[x][y] = '.'
                
def main():
    time = 0
    while True:
        count = 0
        time +=1
        bfs_wall()
        good_bye_cheese()
        for x in range(R):
            for y in range(C):
                if graph[x][y] == '.':
                    count +=1
                    
        if count == R*C:
            return time
        
print(main())
                
    









# 안과 밖을 나눠줘야함
# 외벽을 .이라고 함
# 치즈는 1초에 한번씩 녹음