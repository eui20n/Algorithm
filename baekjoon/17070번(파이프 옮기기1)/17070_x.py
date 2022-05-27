# 파이프 옮기기1
# 파이프는 연속된 2칸을 차지한다
# 파이프는 벽으로 갈 수 없고 90도로 꺾을수 없다, 45도로 하든가 아니면 앞으로 가든가 이다
# 뒤로는 못간다
# 처음 파이프는 (0,0)과 (0,1)에 있다
from collections import deque

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

# 앞으로 가는 경우
dx_f = [0]
dy_f = [1]

# 45도로 가는 경우, 45도 가는 경우를 마지막에 탐색하려고 이렇게 함
dx_x = [0,1,1]
dy_x = [1,0,1]

# 아래로 가는 경우
dx_b = [1]
dy_b = [0]

# 처음 위치와 온 방향
start_x = [[0,0],[0,1,'f']]

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1
dp[0][1] = 1


def move():
    count = 0
    q = deque()
    q.append([[0,1,'f']])
    # 어느 방향으로 가든 45도로 가는 경우를 탐색해야함
    while q:
        start = q.popleft()
        for z in range(3):
            nx = dx_x[z] + start[0][0]
            ny = dy_x[z] + start[0][1]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                count +=1
            if 0 <= nx < N and 0 <= ny < N and z == 0 and graph[nx][ny] == 0:
                if start[0][2] == 'f' or start[0][2] == 'x':
                    dp[nx][ny] = max(dp[start[0][0]][start[0][1]], dp[nx][ny] + 1)
                    q.append([[nx,ny,'f']])
            if 0 <= nx < N and 0 <= ny < N and z == 1 and graph[nx][ny] == 0:
                if start[0][2] == 'b' or start[0][2] == 'x':
                    dp[nx][ny] = max(dp[start[0][0]][start[0][1]], dp[nx][ny] + 1)
                    q.append([[nx,ny,'b']])
            if 0 <= nx < N and 0 <= ny < N and z == 2 and count == 0 and graph[nx][ny] == 0:
                if start[0][2] == 'x' or start[0][2] == 'f' or start[0][2] == 'b':
                    dp[nx][ny] = max(dp[start[0][0]][start[0][1]], dp[nx][ny] + 1)
                    q.append([[nx,ny,'x']])
        count = 0
        

move()
print(dp[N-1][N-1])
        
# 나중에 다시 풀어보기 꼭꼭
        
    