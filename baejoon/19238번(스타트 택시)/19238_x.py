# 스타트 택시
# 스타트 택시는 손님을 도착지로 데려다줄 때마다 연료가 충전되고, 연료가 바닥나면 그 날의 업무가 끝난다
# 택시기타는 M명의 승객을 태우는게 목표이다
# 활동 영역은 N x N 이며 각 칸은 비어있거나 벽이 있다, 택시가 빈칸에 있을때 상하좌우 중 인접한 빈칸으로 이동할 수 있다
# 택시기사는 최단경로로만 이동한다
# 승객은 M명 있으며 한 택시에 여러명의 승객을 태울 수 없다
# 승객을 태우는 방법
# 1. 승객은 현재위치에서 가장 가까운 위치에 있는 승객을 태운다
# 2. 그런 승객이 여러명이라면 가장 행 번호가 낮은 승객을 태운다
# 3. 그런 승객이 또 여러명이면 열번호가 가장 작은 승객을 태운다
# 택시와 승객이 같은 위치에 서 있으면 그 승객까지의 최단거리는 0이고 연료는 한칸 이동할 때마다 1만큼 소모된다
# 승객을 목적지에 이동시키면, 해당 승객한테 쓴 연료의 2배가 충전된다, 만약 이동중 연료가 다 떨어지면 그 날 영업은 종료된다
# 만약 목적지와 동시에 연료가 바닥이 나면 이는 실패한 것으로 간주하지 않는다

from collections import deque

N,M,C = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
start = list(map(int,input().split()))
cus = []
arrive = []
for _ in range(M):
    a = list(map(int,input().split()))
    cus.append([a[0]-1,a[1]-1])
    arrive.append([a[2]-1,a[3]-1])
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]
    
def bfs_cus(x,y,C): # 손님만 찾아, 나중에 main함수에 for문 돌림
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True
    q = deque()
    q.append([x,y,0]) # 현재 좌표와 남은 연료의 양
    cus_det = [] # 손님의 우선순위를 정해주기 위해서 만듬
    while q:
        for z in cus:
            for i in q:
                if z == i[:2]:
                    cus_det.append(z)
        if len(cus_det) >= 2:
            print(cus_det)
            cus_det.sort(key = lambda x:x[1]) # 열 기준으로 정렬
            cus_det.sort(key = lambda x:x[0]) # 행 기준으로 정렬
        if len(cus_det) >= 1:
            return [cus_det[0],p[2]]
    
        p = q.popleft()
        for z in range(4):
            nx = p[0] + dx[z]
            ny = p[1] + dy[z]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0 and p[2] > 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx,ny,p[2]-1])
    return -1


def bfs_arr(x,y,C): # 이건 손님의 위치가 인자로 들어감, 또한 남아있는 연료도 인자로 들어감 -> bfs_cus의 결과임
    # 손님의 인덱스 번호를 찾아줌
    for z in range(len(cus)):
        if [x,y] == cus[z]:
            cus_index = z
            break
    arr = [arrive[z][0],arrive[z][1]]
    del cus[cus_index]
    del arrive[cus_index]
    
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[x][y] = True
    
    q = deque()
    q.append([x,y,C])
    while q:
        p = q.popleft()
        for z in range(4):
            nx = p[0] + dx[z]
            ny = p[1] + dy[z]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0 and p[2] > 0:
                visited[x][y] = True
                if nx == arr[0] and ny == arr[1]:
                    return [nx,ny,(p[2]-1)*2]
                q.append([nx,ny,p[2]-1])
    return -1
                
def main():
    k = bfs_cus(start[0]-1,start[1]-1,C)
    if k == -1:
        return k
    b = bfs_arr(k[0][0],k[0][1],k[1])
    if b == -1:
        return b
    for _ in range(M-1):
        k = bfs_cus(b[0]-1,b[1]-1,b[2])
        if k == -1:
            return k
        b = bfs_arr(k[0][0],k[0][1],k[1])
        if b == -1:
            return b
    return b[2]
    
#print(main())

# 목적지에 가는 함수가 잘못됨 -> 이거 다시 구현하기
# 그냥 bfs를 두번해면 되는것 같음 -> 연료의 총량을 구하는 방법을 다시 생각해야함

# 순서 : 손님 태움 -> 목적지에 내려줌 => 이 과정 손님 없을 때까지 반복
# 손님이 있으면 검사를 해야함 -> 누구를 먼저태워야 하는지 알아야 하기 때문
# 위의 검사하는 과정을 통해서 손님을 누굴 태울지 정했다면, 그 손님이 누군지, 목적지가 어딘지 명확히 알아야함
# 손님을 태운 후 행동이 변해야함
# 일단 구현해보고 만약에 시간 초가가 뜨고 더 이상 머리가 안돌아 갈때 deque가 아닌 heapq를 쓸것
# 함수를 합해서 main함수에서 구현해줄것