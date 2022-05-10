# 낚시왕
# 낚시를 하는 격자가 R x C의 크기이고, 낚시왕은 가장 왼쪽열의 한 칸 왼쪽에 있다
# 낚시왕은 1초 동안 아래의 일을 순서대로 한다
# 1. 낚시왕이 오른쪽으로 한 칸 이동한다
# 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다
# 3. 상어가 이동한다
# 상어는 입력으로 주언진 속도로 이동하고, 단위는 칸/초 이다.
# 상어가 격자판 밖으로 이동하려고 하면 속도를 유지하면서 방향만 바꾼다
# 상어가 이동 후 같은 칸에 상어가 2마리 이상 있으면 크기가 가장 큰 상어가 남는다
# 낚시왕이 잡은 상어 크기의 합을 구해라
# 방향은 위(1) 아래(2) 오른쪽(3) 왼쪽(4)
# 입력에서 상어의 정보는 [R좌표, C좌표, 속력, 방향, 크기]

R,C,M = map(int,input().split())
shark_info = [list(map(int,input().split())) for _ in range(M)]

# 낚시 꾼의 위치 -> 상어의 위치가 1부터 시작이라서 0,0이 현재위치가 됨
angler = [0,0]

# 순서대로 위 아래 오른쪽 왼쪽 -> 0번 인덱스는 그냥 숫자 맞추려고 한것, 이거 필요없으면 제거하기
dx = [0,-1,1,0,0]
dy = [0,0,0,1,-1]

def fishing(shark_info):
    ''' 낚시를 하는 함수'''
    shark_score = 0
    
    while True:
        # 낚시왕이 오른쪽으로 한 칸 이동한다
        angler[1] += 1
        
        # 종료 조건
        if angler[1] >= C+1:
            return shark_score
        
        # 상어를 잡음 -> 람다식을 이용해서 정렬을 함
        shark_info.sort(key = lambda x:(x[1],x[0]))
        for x in range(len(shark_info)):
            if shark_info[x][1] == angler[1]:
                shark_score += shark_info[x][4]
                del shark_info[x]
                break
            
        # 상어 이동 -> 먼저 위 아래, 왼쪽 오른쪽 으로 가는걸 나눔
        # 그 후 그 수가 짝수인지 홀수인지 나눈다음 만약에 홀수이면 방향에 맞는 값을 더해줘서 그 수를 짝수처럼 만들어줌(짝수 : 방향안바뀜, 홀수 : 방향바뀜)
        # 여기서 -1을 해준이유는 한칸씩 이동하는건 처음에 있는 칸을 제외하기 때문
        for x in range(len(shark_info)):
            if shark_info[x][3] == 1 or shark_info[x][3] == 2:
                speed = shark_info[x][2] % (R-1)
                if (shark_info[x][2] // (R-1)) % 2 != 0:
                    speed +=(R-1)
                for _ in range(speed):
                    if shark_info[x][3] == 1: # 위
                        shark_info[x][0] += dx[shark_info[x][3]]
                        if shark_info[x][0] <= 0:
                            shark_info[x][3] = 2
                            shark_info[x][0] = 2
                            
                    elif shark_info[x][3] == 2: # 아래
                        shark_info[x][0] += dx[shark_info[x][3]]
                        if shark_info[x][0] >= R+1:
                            shark_info[x][3] = 1
                            shark_info[x][0] = R-1

                            
            elif shark_info[x][3] == 3 or shark_info[x][3] == 4:
                speed = shark_info[x][2] % (C-1)
                if (shark_info[x][2] // (C-1)) % 2 != 0:
                    speed +=(C-1)              
                for _ in range(speed):
                    if shark_info[x][3] == 3: # 오른쪽
                        shark_info[x][1] += dy[shark_info[x][3]]
                        if shark_info[x][1] >= C+1:
                            shark_info[x][3] = 4
                            shark_info[x][1] = C-1
                        
                    elif shark_info[x][3] == 4: # 왼쪽
                        shark_info[x][1] += dy[shark_info[x][3]]
                        if shark_info[x][1] <= 0:
                            shark_info[x][3] = 3
                            shark_info[x][1] = 2
        #for x in shark_info:
        #    print(x)
        #print('')
                    

                        
        # 만약에 같은 위치에 상어가 있으면 더 큰 상어가 살아남음
        shark_info = remove_shark(shark_info)

        
def remove_shark(shark_info):
    # 우선 빈 리스트를 만들고, 인덱스 번호가 같으면 그 인덱스에 값을 넣음
    # 인덱스 넣는 연산은 반복문인데 만약에 그 자리에 다른 인덱스가 있으면 크기를 비교한 후 작은건 빼고 큰것만 넣음
    
    # 남는 상어의 위치
    live_shark = [[0 for _ in range(C+1)] for _ in range(R+1)]
    for x in shark_info:
        if live_shark[x[0]][x[1]] == 0:
            live_shark[x[0]][x[1]] = x
        else:
            if live_shark[x[0]][x[1]][4] < x[4]:
                live_shark[x[0]][x[1]] = x

    shark_info = []
    # 남은 상어를 shark_info에 넣어주는 과정
    for x in range(1,R+1):
        for y in range(1,C+1):
            if live_shark[x][y] != 0:
                shark_info.append(live_shark[x][y])
    return shark_info

                
            
        
print(fishing(shark_info))
    
