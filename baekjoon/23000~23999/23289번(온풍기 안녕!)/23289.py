# 온풍기 안녕!
# 온풍기의 성능을 측정하는 방식은 아래와 같다
# 1. 집에 있는 모든 온풍이에서 바람이 한 번 나옴
# 2. 온도가 조절됨
# 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
# 4. 초콜릿을 하나 먹는다(?)
# 5. 조사하는 모든 칸의 온도가  k 이상이 되었는지 검사, 모든 칸의 온도가 k 이상이면 테스트를 중단하고, 아니면 1번 반복
# 온풍기에 바람이 나오는 곳이 있는데, 이 곳은 위 아래 오른쪽 왼쪽 중 하나이다
# 온풍기가 나오는 방향의 온도는 5도 올라가고 그 후 온도가 1도씩 줄어들면서 확산이 되는데 (x-1,y+1) (x,y+1) (x+1,y+1)로 된다
# 확산되는 바람의 크기가 1이거나 벽에 부딪히면 더 이상 확산하지 않는다
# 온풍기는 2대 이상 있을 수도 있다, 만약에 이 경우 각 칸의 상승한 온도는 두 온풍기에 나온 바람의 합이다
# 온풍기가 있는 칸도 다른 온풍기에 의해서 온도가 상승할 수 있다
# 온도가 조절되는 과정의 아래와 같다
# 1. 모든 인접한 칸에 대해서, 온도가 높은 칸에서 낮은 칸으로 (두 칸의 온도차)/4 만큼 온도가 조절된다
# 1-1. 이 과정에서 온도가 높은 칸은 다른 칸에 온도를 준 만큼 감소하고 낮은 온도의 칸은 상승한다
# 위 과정은 모두 동시에 진행되며 벽이 있는 경우 온도가 조절되지 않는다
# 이때 초콜릿을 먹은 횟수를 출력해라 - 뜬금없네;
# 입력 정보
# 0 빈칸, 1~4 온풍기 정보(1 오른쪽, 2 왼쪽, 3 위, 4 아래), 5 온도를 조사해야 하는 칸
# 위의 정보와 그에 맞는 그래프가 주어진 후 벽의 개수와 벽의 정보가 입력됨
# 벽에 대한 정보에서 t가 0이면 (x,y)와 (x-1,y)사이에 벽이 있고, t가 1이면 (x,y)와 (x,y+1) 사이에 벽이 있다
# 입력이 되는 벽의 인덱스 정보는 +1이 되어 있음 -> 1씩 빼서 사용하면 됨
# 출력은 초콜릿을 먹은 횟수를 출력하면 되는데 만약 100이 넘으면 101을 출력하면 된다

R,C,K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(R)]
W = int(input())
wall_0 = [] # 가로 벽
wall_1 = [] # 세로 벽
for _ in range(W):
    a,b,c = map(int,input().split())
    # 인덱스 시작이 0이니까 그거에 맞춰서 만들어줌
    if c == 0:
        wall_0.append([a-1,b-1,a-2,b-1])
    if c == 1:
        wall_1.append([a-1,b-1,a-1,b])


    
# 방향을 딕셔너리 형태로 저장
dir = {1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)}


# 온도가 기록될 그래프
temp_graph = [[0]*C for _ in range(R)]

# 검사해야할 칸과 온풍기가 있는 칸을 검사함 -> 시간을 줄이기 위해서 진행
result = []
hot_air_blower = []
for x in range(R):
    for y in range(C):
        if graph[x][y] == 5:
            result.append([x,y])
        if 0 < graph[x][y] < 5:
            hot_air_blower.append([x,y,graph[x][y]]) # 온풍기의 방향까지 넣어줌
            
            
def wind():
    '''온풍기에서 바람이 나오는 함수'''
    # 식의 간결함을 위해서 바람이 나오는 방향은 (위 아래) (오른쪽 왼쪽) 으로 구분해서 계산함
    for x in hot_air_blower:
        visited = [[False]*C for _ in range(R)] # 방문처리를 해줘서 같은 온풍기에서 중복이 되지 않게 해줌
        temp_list = [] # 임시 리스트를 만들어서 퍼져나가는걸 확인해줌
        temp_list_2 = []
        for y in range(5,0,-1):
            if x[2] == 1 or x[2] == 2:
                dir_1 = 1*dir[x[2]][1]
                if y == 5:
                    if 0 <= x[1] + dir_1 < C: 
                        temp_graph[x[0]][x[1]+dir_1] += 5
                        visited[x[0]][x[1]+dir_1] = True
                        temp_list.append([x[0],x[1]+dir_1])
                else: # 1번 벽
                    while temp_list:
                        p = temp_list.pop()
                        if 0 <= p[0]-1 < R and 0 <= p[1]+dir_1 < C and not visited[p[0]-1][p[1]+dir_1]:
                            # 모든 경우에서 벽이 없으면
                            if [p[0],p[1],p[0]-1,p[1]] not in wall_0 and [p[0]-1,p[1],p[0],p[1]] not in wall_0 and [p[0]-1,p[1],p[0]-1,p[1]+dir_1] not in wall_1 and [p[0]-1,p[1]+dir_1,p[0]-1,p[1]] not in wall_1:
                                temp_graph[p[0]-1][p[1]+dir_1] += y
                                visited[p[0]-1][p[1]+dir_1] = True
                                temp_list_2.append([p[0]-1, p[1]+dir_1])
                            
                        if 0 <= p[0] < R and 0 <= p[1]+dir_1 < C and not visited[p[0]][p[1]+dir_1]:
                            if [p[0],p[1],p[0],p[1]+dir_1] not in wall_1 and [p[0],p[1]+dir_1,p[0],p[1]] not in wall_1:
                                temp_graph[p[0]][p[1]+dir_1] += y
                                visited[p[0]][p[1]+dir_1] = True
                                temp_list_2.append([p[0], p[1]+dir_1])
                            
                        if 0 <= p[0]+1 < R and 0 <= p[1]+dir_1 < C and not visited[p[0]+1][p[1]+dir_1]:
                            if [p[0],p[1],p[0]+1,p[1]] not in wall_0 and [p[0]+1,p[1],p[0],p[1]] not in wall_0 and [p[0]+1,p[1],p[0]+1,p[1]+dir_1] not in wall_1 and [p[0]+1,p[1]+dir_1,p[0]+1,p[1]] not in wall_1:
                                temp_graph[p[0]+1][p[1]+dir_1] += y
                                visited[p[0]+1][p[1]+dir_1] = True
                                temp_list_2.append([p[0]+1, p[1]+dir_1])
                    
                    # 리스트에 넣어줌
                    for i in temp_list_2:
                        temp_list.append(i)                      
            
            # 위와 동일함
            if x[2] == 3 or x[2] == 4:
                dir_1 = 1*dir[x[2]][0]
                if y == 5:
                    if 0 <= x[0]+dir_1 < R:
                        temp_graph[x[0]+dir_1][x[1]] += 5
                        visited[x[0]+dir_1][x[1]] = True
                        temp_list.append([x[0]+dir_1,x[1]])
                else:
                    while temp_list:
                        p = temp_list.pop()
                        if 0 <= p[0]+dir_1 < R and 0 <= p[1] - 1 < C and not visited[p[0]+dir_1][p[1]-1]:
                            if [p[0],p[1],p[0],p[1]-1] not in wall_1 and [p[0],p[1]-1,p[0],p[1]] not in wall_1 and [p[0],p[1]-1,p[0]+dir_1,p[1]-1] not in wall_0 and [p[0]+dir_1,p[1]-1,p[0],p[1]-1] not in wall_0:
                                temp_graph[p[0]+dir_1][p[1]-1] += y
                                visited[p[0]+dir_1][p[1]-1] = True
                                temp_list_2.append([p[0]+dir_1, p[1]-1])
                            
                        if 0 <= p[0]+dir_1 < R and 0 <= p[1] < C and not visited[p[0]+dir_1][p[1]]:
                            if [p[0],p[1],p[0]+dir_1,p[1]] not in wall_0 and [p[0]+dir_1,p[1],p[0],p[1]] not in wall_0:                             
                                temp_graph[p[0]+dir_1][p[1]] += y
                                visited[p[0]+dir_1][p[1]] = True
                                temp_list_2.append([p[0]+dir_1, p[1]])
                            
                        if 0 <= p[0]+dir_1 < R and 0 <= p[1] + 1 < C and not visited[p[0]+dir_1][p[1]+1]:
                            if [p[0],p[1],p[0],p[1]+1] not in wall_1 and [p[0],p[1]+1,p[0],p[1]] not in wall_1 and [p[0],p[1]+1,p[0]+dir_1,p[1]+1] not in wall_0 and [p[0]+dir_1,p[1]+1,p[0],p[1]+1] not in wall_0:
                                temp_graph[p[0]+dir_1][p[1]+1] += y
                                visited[p[0]+dir_1][p[1]+1] = True
                                temp_list_2.append([p[0]+dir_1, p[1]+1])
                    
                    for i in temp_list_2:
                        temp_list.append(i)
                        
                        
def spread():
    '''온도가 확산하는 함수'''
    # 온도가 동시에 변하기 때문에 동시에 변할때 도움을 줄 임시 리스트 생성
    temp = [[0]*C for _ in range(R)]
    temp_p = [[0]*C for _ in range(R)]
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    # 두 칸의 온도차이 //4
    # 동시 온도가 확산하는 것을 표현
    # 온도가 큰쪽에서 작은 쪽으로 확산함 -> 나는 무조건 현재위치 기준으로 갈거임
    for x in range(R):
        for y in range(C):
            if temp_graph[x][y] >= 4:
                sum = 0
                for z in range(4):
                    nx = x + dx[z]
                    ny = y + dy[z]
                    if (0 <= nx < R and 0 <= ny < C and temp_graph[x][y] > temp_graph[nx][ny]):
                        if [x,y,nx,ny] not in wall_1 and [nx,ny,x,y] not in wall_1 and [x,y,nx,ny] not in wall_0 and [nx,ny,x,y] not in wall_0:
                            temp[nx][ny] += (temp_graph[x][y] - temp_graph[nx][ny])//4
                            sum += (temp_graph[x][y] - temp_graph[nx][ny])//4
                temp_p[x][y] = sum
    
    for x in range(R):
        for y in range(C):
            # temp의 역할은 얼마나 증가했는지 알려주는 역할, temp_p는 얼마나 줄어드는지 알려주는 역할
            temp_graph[x][y] = temp_graph[x][y] - temp_p[x][y] + temp[x][y]
                             
            
def over_k(result):
    '''우리가 원하는 부분의 온도가 K가 넘었는지 확인하고 만약에 넘었다면 종료'''
    for x in result:
        if temp_graph[x[0]][x[1]] < K:
            return False  
    return True

def out_temp_decrease():
    '''가장 바깥쪽 온도가 1이상이면 1빼줌'''
    # 1부터 가는 이유는 0부터 가면 바깥쪽은 중복이 일어나기때문
    for x in range(1,R-1):
        if temp_graph[x][0] >= 1:
            temp_graph[x][0] -= 1
            
        if temp_graph[x][C-1] >= 1:
            temp_graph[x][C-1] -= 1
    
    for y in range(1,C-1):
        if temp_graph[0][y] >= 1:
            temp_graph[0][y] -= 1
        
        if temp_graph[R-1][y] >= 1:
            temp_graph[R-1][y] -= 1
    
    # 중복을 피하기 위해서 따로 계산
    if temp_graph[0][0] >= 1:
        temp_graph[0][0] -= 1
        
    if temp_graph[0][C-1] >= 1:
        temp_graph[0][C-1] -= 1
        
    if temp_graph[R-1][0] >= 1:
        temp_graph[R-1][0] -= 1
    
    if temp_graph[R-1][C-1] >= 1:
        temp_graph[R-1][C-1] -= 1
        
        
def main(): # 안에 함수들 순서 바꿔주기, 바람 나옴 -> 온도 조절 -> 바깥쪽 온도 1 감소 -> 초콜릿 먹음 -> 조사하는 칸 온도 조사
    '''메인 함수로 함수를 실행시켜줄 함수'''
    chocolate = 0
    while True:
        wind()
        spread()
        out_temp_decrease()
        chocolate +=1
        if over_k(result):
            return chocolate # 스펠링 확인하기
        if chocolate == 101:
            return 101

print(main())
#for x in temp_graph:
#    print(x)

# 순서대로 구현하면 될듯
# 순서가 한번 돌면 조사해야 하는 칸을 검사해야함
# 오른쪽 (x-1, y+1)  (x, y+1) (x+1, y+1) (0,1)
# 왼쪽 (x-1, y-1) (x, y-1) (x+1, y-1) (0,-1)
# 위 (x-1, y-1) (x-1, y) (x-1, y+1) (-1,0)
# 아래 (x+1, y-1) (x+1, y) (x+1, y+1) (1,0)
# 영상을 보여주는 방식 -> 여러개의 사진을 이어붙여서 보여준다
# 위의 방식처럼 확산하는걸 미리 구하고 계속 더하기만 하기 -> 나중에 도전해보기
# 만약에 맞으면 코드 짧게 만들어 보기 -> for문 이용해서 반복하는 부분 없애기
# in연산 말고 다른 연산으로 해야함 -> in을 쓸거면 4개씩 쓰면 안됨
# 시간 좀 더 줄여보기