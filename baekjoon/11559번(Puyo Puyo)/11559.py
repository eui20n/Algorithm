# Puyo Puyo
# 뿌요뿌요의 룰은 아래와 같다
# - 필드에 여러가지 색깔의 뿌요를 놓는다. 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다
# - 뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다
# - 뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어진다
# - 아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다
# - 터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다
# 입력이 들어올때 연쇄가 몇 번 연속으로 일어날지 출력해라
# 색은 R,G,B,P,Y가 있고 판은 12 x 6 이다

from collections import deque

board = [list(map(str,input())) for _ in range(12)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

remove_puyo = []

# 제거 하는 것을 bfs로 하는 것임
def bfs(x,y,color,visited):
    if visited[x][y] == True:
        return
    q = deque()
    q.append([x,y,color]) # 현재 위치, 색
    visited[x][y] = True
    board[x][y] = '.'
    while q:
        p = q.popleft()
        for z in range(4):
            nx = p[0] + dx[z]
            ny = p[1] + dy[z]
            if 0 <= nx < 12 and 0 <= ny < 6 and board[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx,ny,p[2]])
                board[nx][ny] = '.'
                
    
# 각 색이 몇번 나왔는지 확인하는 함수
# 필요한 값 -> x,y,색
def check_col(x,y,color,visited): # 색별로 구분할것, 색은 board[x][y] 로 인자를 받을 것임
    global count
    count +=1
    visited[x][y] = True
    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 <= nx < 12 and 0 <= ny < 6 and board[nx][ny] == color and not visited[nx][ny]:
            check_col(nx,ny,color,visited)
    if count >= 4:
        return remove_puyo.append([x,y])
    
# 중력에 의해서 뿌요가 내려오는 함수
# 먼저 동시에 터지지만, 동시가 없다는 가정하에 코드를 짤것임
def gravity():
    # 그래프의 아래부터 탐색할것
    for c in range(6):
        count = 0
        for r in range(11,-1,-1):
            if board[r][c] != '.':
                if 11 - count != r:
                    board[11 - count][c] = board[r][c]
                    board[r][c] = '.'
                count +=1
                    

def main():
    count_game = 0
    while True:
        visited = [[False for _ in range(6)] for _ in range(12)]
        for r in range(12):
            for c in range(6):
                if visited[r][c] == False and board[r][c] != '.':
                    global count
                    count = 0
                    check_col(r,c,board[r][c],visited)
                
        if len(remove_puyo) == 0:
           return count_game
    
        visited = [[False for _ in range(6)] for _ in range(12)]
        for _ in range(len(remove_puyo)):
            start = remove_puyo.pop()
            bfs(start[0],start[1],board[start[0]][start[1]],visited)
        gravity()
        count_game +=1
        
    # 구현은 여기서 하기
    # dfs는 여러번 돌려서 조건에 맞는것은 다 골라낼 것임
    # dfs함수의 반환값은 remove_puyo함수를 반복돌릴것 -> pop으로 해서 빼줄거임 -> 최종적으로는 반복을 다 하면 빈 리스트가 되게 하고 싶음
print(main())

# 색깔 별로 구분해서 풀어야 할듯 -> 구분을 함수로 만들지 말고, q에 저장하는 식으로 해야할듯
# 중력 때문에 모든 블록들은 아래에 있음, 중간에 있을 수 없음
# 시작점은 나중에 알아서 잡아줄것
# 방문처리는 연쇄마다 해줘야함