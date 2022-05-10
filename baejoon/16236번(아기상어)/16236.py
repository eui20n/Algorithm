# 아기상어
# N by N 크기의 공간에 물고기 M 마리와 아기 상어 1 마리가 있다, 한 칸은 1 by 1이고, 한 칸에 물고기는 최대 1마리 존재한다
# 아기상어와 물고기는 모두 크기를 가지고 있다. 아기상어의 처음 크기는 2이다. 아기상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다
# 아기상어는 자기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다
# 아기상어는 자기보다 작은 크기의 물고기만 먹을 수 있다, 그래서 크기가 같은 물고기는 먹을순 없지만, 그 칸은 지나갈 수 있다
# 아기상어가 어디로 이동할지 결정하는 방법
# 1. 더 이상 먹을 수 있는 물고기가 없다면 엄마상어에게 도움을 청한다
# 2. 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다
# 3. 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다
# 3-1. 거리는 아기상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다
# 3-2. 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면 가장 왼쪽에 있는 물고기를 먹는다
# 아기상어의 이동은 1초가 걸리고, 먹는데는 시간이 안걸리다고 한다
# 아기상어가 물고기를 먹었으면, 그 칸은 빈 칸이 된다
# 아기상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다(경험치 개념으로 증가를 하면 물고기를 먹은 수는 초기화됨)
# 아기상어가 몇초동안 엄마상어에게 도움을 청하지 않고 물고기를 먹을 수 있는지 구하라
# 입력은 첫줄에는 공간의 크기 N
# 둘째 줄부터 공간의 상태가 주어진다. (0은 빈 칸, 1, 2, 3, 4, 5, 6은 물고기의 크기, 9는 아기상어 위치)
# 출력은 아기상어가 엄마상어에게 도움을 청하지 않고 물고기를 먹을 수 있는 시간이다.

from collections import deque

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

# 물고기가 많을때 위에 있는 물고기 먼저 먹음, 그 경우가 많으면 왼쪽에 있는 것을 먼저 먹음
dx = [-1,1,0,0]
dy = [0,0,-1,1]

size_shark = 2
feet_count = 0
second = 0


# bfs를 반복해야함, bfs는 어딜로 움직일지 정해주는 함수임 -> 움직일 방향을 정해주는 함수를 만들어야함
# x,y는 상어의 현재위치

result = []
def bfs(x,y,size_shark):
    visited = [[True] * N for _ in range(N)]
    for n in range(N):
        for m in range(N):
            if graph[n][m] <= size_shark:
                visited[n][m] = False
                
    
    depth = 0
    q = deque([[x,y,depth,graph[x][y]]])
    while q:
        p = q.popleft()
        depth = p[2]
        result.append(p)
        for z in range(4):
            nx = p[0] + dx[z]
            ny = p[1] + dy[z]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and size_shark >= graph[nx][ny]:
                visited[nx][ny] = True
                q.append([nx,ny,depth+1,graph[nx][ny]])
                

# 어딜로 움직여줄지 정해주고 먹고 크기까지 커지는 함수, 결과값으로는 먹이를 먹는 곳의 인덱스가 나와야힘
#move = []
def decide_move(size_shark):
    move = []
    # bfs결과로 리스트(이동하는 곳) 중 먹을 수 있는 곳만 고르는 과정
    for z in range(len(result)):
        if 0 < result[z][3] < size_shark:
            move.append(result[z])
    
    if len(move) == 0:
        return []
            
    # 조건에 맞게 하기 위해서 각각을 나누는 과정
    index_x = []
    index_y = []
    depth_size = []
    fish_size = []
    place_move = [] # 최종적으로 갈 곳
    for z in range(len(move)): # 나눌때 인덱스가 몇번 이였는지 추가함으로써 헷갈리지 않게함
        index_x.append(move[z][0])
        index_y.append(move[z][1])
        depth_size.append(move[z][2])
        fish_size.append(move[z][3])

    # 만약 거리가 짧은게 여러개 일때
    if depth_size.count(min(depth_size)) > 1:
        for x in range(len(depth_size)-1,-1,-1): # 만약에 처음순으로 삭제하면 뒤에 있는 것을 삭제할때 인덱스 번호가 안맞아서 에러남 -> 역순으로 해결
            if depth_size[x] != min(depth_size):
                del depth_size[x]
                del index_x[x]
                del index_y[x]
                del fish_size[x]
                #depth_size.remove(depth_size[x])
                #index_x.remove(index_x[x])
                #index_y.remove(index_y[x])
                #fish_size.remove(fish_size[x])
        # 거리가 짧은 후 가장 위에 있는 것을 고르는 과정, 이 과정에서 상어 보다 위에 없는 경우도 생각해야함(상어의 현재위치 인덱스를 계속 업데이트 해서 할것)
        if index_x.count(min(index_x)) > 1:
            for x in range(len(index_x)-1,-1,-1):
                if index_x[x] != min(index_x):
                    del depth_size[x]
                    del index_x[x]
                    del index_y[x]
                    del fish_size[x]
                    #depth_size.remove(depth_size[x])
                    #index_x.remove(index_x[x])
                    #index_y.remove(index_y[x])
                    #fish_size.remove(fish_size[x])
            # 마지막으로 가장 왼쪽에 있는 경우 -> 많아 봤자 2개가 남음
            if index_y[0] < index_y[1]:
                place_move.append(index_x[0])
                place_move.append(index_y[0])
                place_move.append(depth_size[0])
                place_move.append(fish_size[0])
            else:
                place_move.append(index_x[1])
                place_move.append(index_y[1])
                place_move.append(depth_size[1])
                place_move.append(fish_size[1])
        # 위의 경우가 아닐때
        else:
            place_move.append(index_x[index_x.index(min(index_x))])
            place_move.append(index_y[index_x.index(min(index_x))])
            place_move.append(depth_size[index_x.index(min(index_x))])
            place_move.append(fish_size[index_x.index(min(index_x))])
    #위의 경우가 아닐때
    else:
        place_move.append(index_x[depth_size.index(min(depth_size))])
        place_move.append(index_y[depth_size.index(min(depth_size))])
        place_move.append(depth_size[depth_size.index(min(depth_size))])
        place_move.append(fish_size[depth_size.index(min(depth_size))])
    
    return place_move
        
# 조건에 맞게 설정했으면, 반복문으로 끝날때 까지 반복해주고, 끝나면 second출력하기


# 초기 상어 위치 찾기
shark_index = []

for x in range(N):
    for y in range(N):
        if graph[x][y] == 9:
            shark_index.append(x)
            shark_index.append(y)
            
bfs(shark_index[0],shark_index[1], size_shark)
a = decide_move(size_shark)
graph[shark_index[0]][shark_index[1]] = 0
if len(a) == 0:
    print(0)
else:
    graph[a[0]][a[1]] = 9 # 자기 위치
    second += a[2]
    feet_count +=1
    while a:
        result = [] # 함수가 들어가기 전에 초기화 해줘야함
        graph[a[0]][a[1]] = 0 # 이제 이동하니까 0으로 바꿈
        bfs(a[0],a[1],size_shark)
        a = decide_move(size_shark)
        if len(a) != 0:
            second += a[2]
            feet_count +=1
            graph[a[0]][a[1]] = 9 # 자기위치
        if feet_count == size_shark:
            size_shark +=1
            feet_count = 0
    
    print(second)


# 뭔가 이상함
# 잘 안됨

            
            
        

    
    
        
            
    
    
        
        
        
        

