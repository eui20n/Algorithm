# 미세먼지 안녕!
# R x C의 격자 위를 1 x 1로 나눴다
# 공기청정기는 항상 1열에 설치 되어 있고, 크기는 2개의 행을 차지한다
# 1초동안 아래의 일이 일어난다
# 1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
# 1-1. 미세먼지는 인접한 네 방향으로 확산된다
# 1-2. 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
# 1-3. 확산 되는 양은 (원래의 양)/5 이고 소수점은 버린다 -> 원래의 양에 5로 나눈 몫
# 1-4. 원래 칸의 남아 있는 미세먼지 양은 (원래의 양) - (원래의 양/5) * (확산된 방향의 개수)
# 2. 공기청정기가 작동한다.
# 2-1. 공기청정기에서 바람이 나온다.
# 2-2. 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
# 2-3. 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 2-4. 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다
# 주어진 시간 후에 남아있는 미세먼지의 양을 출력해라
# 공기청정기가 있는 위치는 -1, 아무것도 없는 칸은 0, 미세먼지는 0 이상의 정수이다

R,C,T = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(R)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def spread(dust): # dust는 리스트임
    sub_graph = [[0 for _ in range(C)] for _ in range(R)] # 동시에 확산이 일어나기 때문에 계산을 위해 만들어줌
    
    # 동시에 확산이 일어나는 과정
    for x in dust:
        count = 0
        for z in range(4):
            nx = x[0] + dx[z]
            ny = x[1] + dy[z]
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                sub_graph[nx][ny] += graph[x[0]][x[1]] // 5 # sub_graph에 얼만큼 확산이 됬는지 더해줌, 이 후 이 과정이 끝나면 graph에 전체 다 더해주면 됨
                count +=1
        graph[x[0]][x[1]] = graph[x[0]][x[1]] - (graph[x[0]][x[1]] // 5) * count
    
    # sub_graph와 graph를 합해서 현재의 상태를 만들어줌
    for x in range(R):
        for y in range(C):
            graph[x][y] += sub_graph[x][y]
            
def car_wind(car): # car는 리스트임
    # 차의 위와 아래에 따라서 연산이 바뀜
    #for x in graph:
    #    print(x)
    #print('')
    
    # 반시계 순환
    # 처음 행 옆으로 밀기
    graph[car[0][0]].reverse()
    graph[car[0][0]].append(0)
    graph[car[0][0]].reverse()
    graph[car[0][0]][0],graph[car[0][0]][1] = graph[car[0][0]][1],graph[car[0][0]][0]
    cycle_num = graph[car[0][0]].pop()
    
    # 그 행을 기준으로 위로 밀기
    for x in range(car[0][0]-1,-1,-1):
        graph[x][C-1],cycle_num = cycle_num,graph[x][C-1]
        
    # 제일 위 행 기준으로 왼쪽으로 밀기
    for x in range(C-2,-1,-1):
        graph[0][x],cycle_num = cycle_num,graph[0][x]
    
    # 제일 위 행 기준으로 공기청정기 위치까지 아래로 밀기, 이거 다시 생각하기
    for x in range(1,car[0][0]):
        if graph[x][0] == -1:
            cycle_num = 0
        else:
            cycle_num,graph[x][0] = graph[x][0],cycle_num
    
    #for x in graph:
    #    print(x)
    #print('')

    # 시계 순환 -> 이거 다시 하기, 이게 이상함
    # 처음 행 옆으로 밀기
    graph[car[1][0]].reverse()
    graph[car[1][0]].append(0)
    graph[car[1][0]].reverse()
    graph[car[1][0]][0],graph[car[1][0]][1] = graph[car[1][0]][1],graph[car[1][0]][0]
    cycle_num = graph[car[1][0]].pop()
    
    # 그 행을 기준으로 아래로 밀기 -> 이게 잘못됨, 이거 다시 짜야함, 천천히 이거 다시 만들기, 최대한 생각을 해서 절대로 모든 경우에 대해서 안틀리게
    if R - car[1][0] - 1== 2:
        graph[car[1][0]+1][C-1], cycle_num = cycle_num, graph[car[1][0]+1][C-1]
        graph[car[1][0]+2][C-1], cycle_num = cycle_num, graph[car[1][0]+2][C-1]
    else:
        for x in range(car[1][0]+1,R):
            graph[x][C-1],cycle_num = cycle_num,graph[x][C-1]

        
    # 제일 아래 행 기준으로 왼쪽으로 밀기
    for x in range(C-2,-1,-1):
        graph[R-1][x],cycle_num = cycle_num,graph[R-1][x]
    
    # 제일 아래 행 기준으로 공기청정기 위치까지 위로 밀기
    for x in range(R-2,car[1][0],-1):
        if graph[x][0] == -1:
            cycle_num = 0
        else:
            cycle_num,graph[x][0] = graph[x][0],cycle_num
            
    #for x in graph:
    #    print(x)
    #print('----------------------------------')
    
    
    

# 이 아래로 전부 다 while문을 돌려야함
time = 0
while T != 0:
    time+=1
    dust = []
    car = []
    for x in range(R):
        for y in range(C):
            if graph[x][y] == -1:
                car.append([x,y]) # 인덱스가 0인 것이 위에 있는것, 1인 것이 아래인것
            if graph[x][y] > 0:
                dust.append([x,y])
    spread(dust)
    car_wind(car)
    if time == T:
        break

count = 0

for x in range(R):
    for y in range(C):
        if graph[x][y] > 0:
            count += graph[x][y]

print(count)

