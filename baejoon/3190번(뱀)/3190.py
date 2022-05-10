# 뱀
# 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀의 길이가 늘어난다
# 뱀이 벽이나 자기자신의 몸과 부딪히면 게임은 끝난다
# N x N 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있고 이 보드 상하좌우 끝은 벽이다
# 처음엔 뱀은 맨위 좌측(0,0)에 위치하고 길이가 1이다
# 뱀은 처음 오른쪽으로 향한다. 뱀은 매 초마다 이동을 하는데 아래 규칙을 따른다
# 1. 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다
# 2. 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다
# 3. 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다, 즉 몸길이는 변하지 않는다
# 이 게임이 몇 초에 끝나는지 출력해라
# 입력에서 D는 오른쪽으로 90도 회전, L은 왼쪽으로 90도 회전이다

from collections import deque

N = int(input())
apple_count = int(input())
apple_loc = []
for _ in range(apple_count):
    a,b = map(int,input().split())
    apple_loc.append([a-1,b-1])
snake_count = int(input())
snake_dir = []
for _ in range(snake_count):
    a,b = map(str,input().split())
    snake_dir.append([int(a),b])
    
    
# 방향은 오른쪽 기준이고, 만약에 왼쪽으로 가면 인덱스를 반대로 가면 됨
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 그래프와 같은건 그리지 않고 현재 위치만을 가지고 계산할것
def snake():
    direct = 0
    time = 0
    body = deque()
    body.append([0,0]) # 현재 좌표가 body에 들어가 있음
    # 방향으로 return이 걸리기 전까지 계속 가는 거임
    while True:
        
        # 가장 앞에 좌표를 추가해줌, 만약에 사과를 만나면 그냥 두고, 못만나면 가장 뒤쪽을 제외해주면됨
        body.appendleft([body[0][0] + dx[direct],body[0][1] + dy[direct]])
        time +=1
        # 만약에 벽에 부딪히면 종룧마
        if body[0][0] < 0 or body[0][1] < 0 or body[0][0] >= N or body[0][1] >= N:
            return time
        
        # 자기 자신을 만나면 종료함
        for x in range(1,len(body)):
            if [body[0][0],body[0][1]] == body[x]:
                return time
            
            
        # 사과 만나는 연산
        if len(apple_loc) != 0:
            index = -1
            for x in range(len(apple_loc)):
                if apple_loc[x][0] == body[0][0] and apple_loc[x][1] == body[0][1]:
                    index = x
                    break
            if index != -1:
                del apple_loc[index] # 만약에 사과를 만났으면 만난 사과는 삭제
            else:
                body.pop() # 사과를 안맞으면 몸의 길이를 원래대로 만들어야함
        else:
            body.pop()
            
        # 만약에 시간이 맞으면 방향으로 돌려줌
        for x in range(len(snake_dir)):
            if snake_dir[x][0] == time:
                if snake_dir[x][1] == 'D':
                    direct +=1
                    if direct > 3:
                        direct = 0
                else:
                    direct -=1
                    if direct < 0:
                        direct = 3
                break
    
    
    
                
print(snake())
