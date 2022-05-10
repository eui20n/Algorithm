# 움직이는 미로 탈출
# 8 x 8 인 체스판에서 탈출하는 게임을 만들었다, 이 체스판의 모든 칸은 빈 칸 또는 벽 중 하나이다
# 탈출할 캐릭터는 왼쪽 아랫칸에 있고, 오른쪽 윗 칸으로 이동해야 한다
# 벽이 움직인다, 1초마다 모든 벽이 아래에 있는 행으로 한 칸씩 내려가고, 가장 아래에 있어서 내려갈 곳이 없는 벽은 사라진다
# 캐릭터는 1초에 인접한 한 칸 또는 대각선 방향으로 인접한 한 칸으로 이동하거나, 현재 위치에 서 있을 수 있고, 이동은 빈칸으로 한다
# 캐릭터가 먼저 움직이고 벽이 움직인다, 벽이 캐릭터가 있는 칸으로 이동하면 더 이상 캐릭터는 이동할 수 없다
# 캐릭터가 가장 오른쪽 윗 칸으로 이동할 수 있는지 없는지 구해라
# .은 빈칸, #은 벽이다
# 캐릭터가 오른쪽위에 도착할 수 있으면 1, 없으면 0을 출력해라

from collections import deque

graph = [list(input()) for _ in range(8)]

dx = [-1,1,0,0,-1,-1,1,1,0]
dy = [0,0,-1,1,-1,1,1,-1,0]

visited = [[False for _ in range(8)] for _ in range(8)] # 필요 없으면 제거해도됨
start = [7,0]
end = [0,7]


def bfs(start,end):
    q = deque()
    depth = 1
    new_start = [start[0],start[1],0]
    q.append(new_start)
    place_list = []
    
    while q:
        # 서 있는 경우에 대해서 생각해보기 -> visited 없이 하면 해결 가능
        p = q.popleft()
        place = [p[0],p[1]]
        if place not in place_list:
            place_list.append(place)
        #print(p)
        if depth == p[2]:
            move_wall(graph)
            change_wall(graph)
            depth +=1
        for z in range(9):
            nx = p[0] + dx[z]
            ny = p[1] + dy[z]
            if 0 <= nx < 8 and 0 <= ny < 8 and graph[nx][ny] == '.' and not visited[nx][ny]:
                if not stand(graph):
                    if graph[p[0]][p[1]] == '#' or graph[p[0]][p[1]] == 'o':
                        break
                    else:
                        q.append([nx,ny,p[2] + 1])
                else:
                    place_list = 'end'
                    #visited[nx][ny] = True
                    #q.append([nx,ny,p[2] + 1])
                    break
        if place_list == 'end':
            break
    if place_list == 'end':
        print('1')
    else:
        if end in place_list:
            print('1')
        else:
            print('0')
                
                
                
def move_wall(graph):
    # 벽이 연속으로 있을 경우를 대비해서 역순으로 계산
    for x in range(7,-1,-1):
        for y in range(7,-1,-1):
            if graph[x][y] == '#':
                if x + 1 > 7:
                    graph[x][y] = '.'
                else:
                    graph[x][y] = '.'
                    graph[x+1][y] = 'o'

def change_wall(graph):
    for x in range(8):
        for y in range(8):
            if graph[x][y] == 'o':
                graph[x][y] = '#'
                
def stand(graph):
    count = 0
    for x in range(8):
        for y in range(8):
            if graph[x][y] == "#":
                count +=1
                break
    if count == 0:
        return True
    else:
        return False
            
                
# 시간 줄이는 방법 고민할 것 -> 본인 위치에 서있는 경우 때문에 시간이 너무 많이 잡아먹힘 -> 해결
# 서있는 연산 때문에 답이 안나옴 -> 연산을 다른 방식으로 해야함
# 벽 움직이는 연산만 신경써서 다시 구현
                
bfs(start,end)
    
    
    
