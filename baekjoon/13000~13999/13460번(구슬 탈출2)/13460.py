# 구슬 탈출2
# 세로 R, 가로 C인 보드가 있다
# 그 보드 안에 빨간 구슬을 구멍을 통해서 빼는게 목표이다
# 중력을 이용해서 이리 저리 굴려서 빼면 되는데 파란 구슬이 빠지면 실패이다, 또한 빨간 구슬과 파란 구슬이 동시에 빠져도 실패이다
# 최소 몇번 기울이면 빨간 구슬을 뺄 수 있는지 출력해라
# 만약 10번 이하로 움직여서 빨간 구슬을 뺄 수 없으면 -1을 출력해라
from collections import deque

R,C = map(int,input().split())
board = [list(map(str,input())) for _ in range(R)]


for x in range(R):
    for y in range(C):
        if board[x][y] == 'B':
            blue_marble = [x,y]
        if board[x][y] == 'R':
            red_marble = [x,y]

# 최악.... 좀 더 깔끔하게 코드 짜기

def marble(blue_marble,red_marble):
    '''구슬을 기울이는 함수'''
    blue_q = deque()
    red_q = deque()
    
    # 큐에 초기값 설정, 좌표 및 시간
    blue_q.append([blue_marble[0],blue_marble[1],0])
    red_q.append([red_marble[0],red_marble[1],0])
    

    
    while True:
        # red_q에 아무것도 없다는 것은 갈곳이 없다는 소리 -> -1 리턴
        if len(red_q) == 0:
            return -1
        # blue_q에 아무것도 업다는 것은 갈곳이 없다는 소리 -> 그냥 넘어감
        elif len(blue_q) == 0:
            pass
        else:
            red_p = red_q.popleft()
            blue_p = blue_q.popleft()
        
        # 종료 조건으로 만약 시간이 10이 되면 -1을 출력
        if red_p[2] == 10:
            return -1
            
        
        # q에 넣을 리스트 -> 반복을 막기 위해서 생성, 중간에 q에 넣으면 계속 반복해버림
        red_list = []
        blue_list = []
        
        # 왼쪽에서 기울이기 -> 오른쪽으로 감(0,1)
        ny_blue = blue_p[1]
        blue_count = 0
        # while문을 통해서 조건에 만족할때까지 반복
        while True:
            # 벽에 부딪히면 종료, 근데 현재 위치가 벽에 있을 수 없으니 왔던 방향 반대로 빼줌
            if board[blue_p[0]][ny_blue] == '#':
                ny_blue -=1
                break
            # 구멍이면 그냥 종료
            if board[blue_p[0]][ny_blue] == 'O':
                break
            # 방향에 맞게 더해줌
            ny_blue +=1
            # 나중에 겹치는 연산할때 사용하기 위해서 카운트를 해줌
            blue_count +=1

        # 위와 같은 연산이지만 이 연산은 red일때 해줌
        ny_red = red_p[1]
        red_count = 0
        while True:
            if board[red_p[0]][ny_red] == '#':
                ny_red -=1
                break
            if board[red_p[0]][ny_red] == 'O':
                break
            ny_red +=1
            red_count +=1
            
        # 빨간 구슬과 파란 구슬이 벽에 부딪힌 경우, 여기에서 반복되는 문장이 너무 많음, 깔끔하게 짜기
        if board[red_p[0]][ny_red] != 'O' and board[blue_p[0]][ny_blue] != 'O':
            # 움직였다면
            if ny_red != red_p[1] and ny_blue != blue_p[1]:
                # 만약에 값이 같으면 겹친다는 소리이다 -> 거리가 긴 녀석 왔던 방향으로 빼주기
                if ny_red == ny_blue and red_p[0] == blue_p[0]:
                    if red_count < blue_count:
                        # 더 긴 쪽에서 왔던 방향의 반대 연산을 해줌
                        red_list.append([red_p[0],ny_red,red_p[2]+1])
                        blue_list.append([blue_p[0],ny_blue-1,blue_p[2]+1])
                    else:
                        red_list.append([red_p[0],ny_red-1,red_p[2]+1])
                        blue_list.append([blue_p[0],ny_blue,blue_p[2]+1])
                # 겹치지 않으면 그냥 append해주면 됨
                else:
                    red_list.append([red_p[0],ny_red,red_p[2]+1])
                    blue_list.append([blue_p[0],ny_blue,blue_p[2]+1])
                    
            # 만약에 blue는 같은데 red는 다를때, 아래 연산은 위와 같음
            elif ny_red != red_p[1] and ny_blue == blue_p[1]:
                if ny_red == ny_blue and red_p[0] == blue_p[0]:
                    if red_count < blue_count:
                        red_list.append([red_p[0],ny_red,red_p[2]+1])
                        blue_list.append([blue_p[0],ny_blue-1,blue_p[2]+1])
                    else:
                        red_list.append([red_p[0],ny_red-1,red_p[2]+1])
                        blue_list.append([blue_p[0],ny_blue,blue_p[2]+1])
                else:
                    red_list.append([red_p[0],ny_red,red_p[2]+1])
                    blue_list.append([blue_p[0],ny_blue,blue_p[2]+1]) 
            # 위의 경우와 반대
            elif ny_red == red_p[1] and ny_blue != blue_p[1]:
                if ny_red == ny_blue and red_p[0] == blue_p[0]:
                    if red_count < blue_count:
                        red_list.append([red_p[0],ny_red,red_p[2]+1])
                        blue_list.append([blue_p[0],ny_blue-1,blue_p[2]+1])
                    else:
                        red_list.append([red_p[0],ny_red-1,red_p[2]+1])
                        blue_list.append([blue_p[0],ny_blue,blue_p[2]+1])
                else:
                    red_list.append([red_p[0],ny_red,red_p[2]+1])
                    blue_list.append([blue_p[0],ny_blue,blue_p[2]+1]) 
                
        # 빨간 구슬만 나간 경우 -> 이 경우만 끝남
        elif board[red_p[0]][ny_red] == 'O' and board[blue_p[0]][ny_blue] != 'O':
            return red_p[2]+1
        
        # 파란 구슬이 나가거나 둘 다 나가는 경우
        else:
            # 실패한 경우니까 생각안하기
            pass
        
        # 아래 연산은 모두 위와 같음
        
        # 오른쪽에서 기울이기 -> 왼쪽으로 감(0,-1)
        ny_blue = blue_p[1]
        blue_count = 0
        while True:
            if board[blue_p[0]][ny_blue] == '#':
                ny_blue +=1
                break
            if board[blue_p[0]][ny_blue] == 'O':
                break
            ny_blue -=1
            blue_count +=1


        ny_red = red_p[1]
        red_count = 0
        while True:
            if board[red_p[0]][ny_red] == '#':
                ny_red +=1
                break
            if board[red_p[0]][ny_red] == 'O':
                break
            ny_red -=1
            red_count +=1
            
        
        if board[red_p[0]][ny_red] != 'O' and board[blue_p[0]][ny_blue] != 'O':    
            if ny_red != red_p[1] and ny_blue != blue_p[1]:
                # 만약에 값이 같으면 거리가 짧은 녀석 왔던 방향으로 빼주기
                if ny_red == ny_blue and red_p[0] == blue_p[0]:
                    if red_count < blue_count: # blue에서 빼줘야함
                        red_list.append([red_p[0],ny_red,red_p[2]+1])
                        blue_list.append([blue_p[0],ny_blue+1,blue_p[2]+1])
                    else:
                        red_list.append([red_p[0],ny_red+1,red_p[2]+1])
                        blue_list.append([blue_p[0],ny_blue,blue_p[2]+1])
                else:
                    red_list.append([red_p[0],ny_red,red_p[2]+1])
                    blue_list.append([blue_p[0],ny_blue,blue_p[2]+1])                
                    
            elif ny_red != red_p[1] and ny_blue == blue_p[1]:
                if ny_red == ny_blue and red_p[0] == blue_p[0]:
                    if red_count < blue_count: # blue에서 빼줘야함
                        red_list.append([red_p[0],ny_red,red_p[2]+1])
                        blue_list.append([blue_p[0],ny_blue+1,blue_p[2]+1])
                    else:
                        red_list.append([red_p[0],ny_red+1,red_p[2]+1])
                        blue_list.append([blue_p[0],ny_blue,blue_p[2]+1])
                else:
                    red_list.append([red_p[0],ny_red,red_p[2]+1])
                    blue_list.append([blue_p[0],ny_blue,blue_p[2]+1]) 
            
            elif ny_red == red_p[1] and ny_blue != blue_p[1]:
                if ny_red == ny_blue and red_p[0] == blue_p[0]:
                    if red_count < blue_count: # blue에서 빼줘야함
                        red_list.append([red_p[0],ny_red,red_p[2]+1])
                        blue_list.append([blue_p[0],ny_blue+1,blue_p[2]+1])
                    else:
                        red_list.append([red_p[0],ny_red+1,red_p[2]+1])
                        blue_list.append([blue_p[0],ny_blue,blue_p[2]+1])
                else:
                    red_list.append([red_p[0],ny_red,red_p[2]+1])
                    blue_list.append([blue_p[0],ny_blue,blue_p[2]+1]) 
                
        
        elif board[red_p[0]][ny_red] == 'O' and board[blue_p[0]][ny_blue] != 'O':
            return red_p[2]+1
    
        else:
            pass

        
        # 위쪽에서 기울이기 -> 아래로 감(1,0)
        nx_blue = blue_p[0]
        blue_count = 0
        while True:
            if board[nx_blue][blue_p[1]] == '#':
                nx_blue -=1
                break
            if board[nx_blue][blue_p[1]] == 'O':
                break
            nx_blue +=1
            blue_count +=1


        nx_red = red_p[0]
        red_count = 0
        while True:
            if board[nx_red][red_p[1]] == '#':
                nx_red -=1
                break
            if board[nx_red][red_p[1]] == 'O':
                break
            nx_red +=1
            red_count +=1
            
        if board[nx_red][red_p[1]] != 'O' and board[nx_blue][blue_p[1]] != 'O':
            if nx_red != red_p[0] and nx_blue != blue_p[0]:
                # 만약에 값이 같으면 거리가 짧은 녀석 왔던 방향으로 빼주기
                if nx_red == nx_blue and red_p[1] == blue_p[1]:
                    if red_count < blue_count: # blue에서 빼줘야함
                        red_list.append([nx_red,red_p[1],red_p[2]+1])
                        blue_list.append([nx_blue-1,blue_p[1],blue_p[2]+1])
                    else:
                        red_list.append([nx_red-1,red_p[1],red_p[2]+1])
                        blue_list.append([nx_blue,blue_p[1],blue_p[2]+1])
                else: # 두 값이 겹치지 않은 경우
                    red_list.append([nx_red,red_p[1],red_p[2]+1])
                    blue_list.append([nx_blue,blue_p[1],blue_p[2]+1])                
                    
            elif nx_red != red_p[0] and nx_blue == blue_p[0]:
                if nx_red == nx_blue and red_p[1] == blue_p[1]:
                    if red_count < blue_count: # blue에서 빼줘야함
                        red_list.append([nx_red,red_p[1],red_p[2]+1])
                        blue_list.append([nx_blue-1,blue_p[1],blue_p[2]+1])
                    else:
                        red_list.append([nx_red-1,red_p[1],red_p[2]+1])
                        blue_list.append([nx_blue,blue_p[1],blue_p[2]+1])
                else: # 두 값이 겹치지 않은 경우
                    red_list.append([nx_red,red_p[1],red_p[2]+1])
                    blue_list.append([nx_blue,blue_p[1],blue_p[2]+1])  
            
            elif nx_red == red_p[0] and nx_blue != blue_p[0]:
                if nx_red == nx_blue and red_p[1] == blue_p[1]:
                    if red_count < blue_count: # blue에서 빼줘야함
                        red_list.append([nx_red,red_p[1],red_p[2]+1])
                        blue_list.append([nx_blue-1,blue_p[1],blue_p[2]+1])
                    else:
                        red_list.append([nx_red-1,red_p[1],red_p[2]+1])
                        blue_list.append([nx_blue,blue_p[1],blue_p[2]+1])
                else: # 두 값이 겹치지 않은 경우
                    red_list.append([nx_red,red_p[1],red_p[2]+1])
                    blue_list.append([nx_blue,blue_p[1],blue_p[2]+1])  
                
                
        elif board[nx_red][red_p[1]] == 'O' and board[nx_blue][blue_p[1]] != 'O':
            return red_p[2]+1
        
        else:
            pass
        
        # 아래로 기울이기 -> 위로 감(-1,0)
        nx_blue = blue_p[0]
        blue_count = 0
        while True:
            if board[nx_blue][blue_p[1]] == '#':
                nx_blue +=1
                break
            if board[nx_blue][blue_p[1]] == 'O':
                break
            nx_blue -=1
            blue_count +=1

        nx_red = red_p[0]
        red_count = 0
        while True:
            if board[nx_red][red_p[1]] == '#':
                nx_red +=1
                break
            if board[nx_red][red_p[1]] == 'O':
                break
            nx_red -=1
            red_count +=1
            
        if board[nx_red][red_p[1]] != 'O' and board[nx_blue][blue_p[1]] != 'O':
            if nx_red != red_p[0] and nx_blue != blue_p[0]:
                # 만약에 값이 같으면 거리가 짧은 녀석 왔던 방향으로 빼주기
                if nx_red == nx_blue and red_p[1] == blue_p[1]:
                    if red_count < blue_count: # blue에서 빼줘야함
                        red_list.append([nx_red,red_p[1],red_p[2]+1])
                        blue_list.append([nx_blue+1,blue_p[1],blue_p[2]+1])
                    else:
                        red_list.append([nx_red+1,red_p[1],red_p[2]+1])
                        blue_list.append([nx_blue,blue_p[1],blue_p[2]+1])
                else: # 두 값이 겹치지 않은 경우
                    red_list.append([nx_red,red_p[1],red_p[2]+1])
                    blue_list.append([nx_blue,blue_p[1],blue_p[2]+1])                
                    
            elif nx_red != red_p[0] and nx_blue == blue_p[0]:
                if nx_red == nx_blue and red_p[1] == blue_p[1]:
                    if red_count < blue_count: # blue에서 빼줘야함
                        red_list.append([nx_red,red_p[1],red_p[2]+1])
                        blue_list.append([nx_blue+1,blue_p[1],blue_p[2]+1])
                    else:
                        red_list.append([nx_red+1,red_p[1],red_p[2]+1])
                        blue_list.append([nx_blue,blue_p[1],blue_p[2]+1])
                else: # 두 값이 겹치지 않은 경우
                    red_list.append([nx_red,red_p[1],red_p[2]+1])
                    blue_list.append([nx_blue,blue_p[1],blue_p[2]+1])  
            
            elif nx_red == red_p[0] and nx_blue != blue_p[0]:
                if nx_red == nx_blue and red_p[1] == blue_p[1]:
                    if red_count < blue_count: # blue에서 빼줘야함
                        red_list.append([nx_red,red_p[1],red_p[2]+1])
                        blue_list.append([nx_blue+1,blue_p[1],blue_p[2]+1])
                    else:
                        red_list.append([nx_red+1,red_p[1],red_p[2]+1])
                        blue_list.append([nx_blue,blue_p[1],blue_p[2]+1])
                else: # 두 값이 겹치지 않은 경우
                    red_list.append([nx_red,red_p[1],red_p[2]+1])
                    blue_list.append([nx_blue,blue_p[1],blue_p[2]+1])  
                
        elif board[nx_red][red_p[1]] == 'O' and board[nx_blue][blue_p[1]] != 'O':
            return red_p[2]+1
        
        else:
            pass
            
        # 큐에 추가해주기
        for x in red_list:
            red_q.append(x)
        for x in blue_list:
            blue_q.append(x)            
        
        
    
        
    
print(marble(blue_marble,red_marble))
    
# 별로 좋은 코드는 아니니 참고만 하세요
# 나중에 다시 짤것