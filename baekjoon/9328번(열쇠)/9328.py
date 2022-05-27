"""
    문제 이름 : 열쇠
    URL : https://www.acmicpc.net/problem/9328
    ----------------------------------------------
    <문제 설명>
    상하좌우로 이동해서 훔칠 수 있는 문서의 최대 개수를 출력해라
    입력 정리
    . -> 빈공간
    * -> 벽, 통과 불가
    $ -> 훔쳐야하는 문서
    알파벳 대문자 -> 문
    알파벳 소문자 -> 열쇠, 그 문자가 대문자인 문을 열 수 있다
    같은 열쇠는 여러개가 있고 한 열쇠는 계속 사용 가능 -> 같은 열쇠가 있는 곳은 굳이 갈 필요 없음
    시작 위치는 따로 주어지지 않고 바깥쪽의 .에서 시작할 수 있다
"""
from collections import deque


def bfs_doc(start):
    """
    훔치고 싶은 문서를 찾아주는 함수
    start는 start_point 처음 부터 하나씩 받을 것
    """

    # 시작점을 보고 대문자면 열쇠있는지 확인하고, 소문자면 열쇠 획득하고 계속진핸, 문서면 먹고 계속 진행
    start = start_first(start)

    if not (start):  # 만약에 start에 아무것도 없으면 바로 끝냄
        return 0

    cnt = 0

    if board[start[0]][start[1]] == '$':
        cnt += 1
        board[start[0]][start[1]] = '.'

    visited = init_visited()
    visited[start[0]][start[1]] = True

    q = deque()
    q.append(start)

    while q:
        p = q.popleft()
        # 4방향으로 조건을 줄건데 함수가 조건이 길어질거 같아서 함수에다가 줄것
        for z in range(4):
            nx = p[0] + dx[z]
            ny = p[1] + dy[z]
            if dir_con(nx, ny, visited):
                if board[nx][ny].islower():
                    if board[nx][ny] not in key:
                        key.add(board[nx][ny])
                        visited = init_visited()
                    board[nx][ny] = '.'

                if board[nx][ny].isupper():
                    if board[nx][ny].lower() not in key:
                        continue
                    board[nx][ny] = '.'

                if board[nx][ny] == '$':
                    board[nx][ny] = '.'
                    cnt += 1

                q.append([nx, ny])
                visited[nx][ny] = True

    return cnt


def dir_con(x, y, visited):
    """ 방향 조건 """
    if x < 0 or x >= r:
        return False
    if y < 0 or y >= c:
        return False
    if visited[x][y]:
        return False
    if board[x][y] == '*':
        return False
    return True


def init_visited():
    """ 방문처리 리스트를 만들어 주는 함수 """
    visited = [[False for _ in range(c)] for _ in range(r)]
    return visited


def check_start(arr):
    """ 시작점을 찾아주는 함수로 벽빼고 모든 점이 시작점이 될 수 있음 """
    # 여기서 바로 대문자 처리 안하는 이유는 열쇠를 계속해서 먹을 수 있기 때문에 여기서 처리를 안해주는 것임
    start_point = []
    for x in range(c):
        if arr[0][x] != '*':
            start_point.append([0, x])
        if arr[r - 1][x] != '*':
            start_point.append([r - 1, x])

    for y in range(r):
        if arr[y][0] != '*':
            start_point.append([y, 0])
        if arr[y][c - 1] != '*':
            start_point.append([y, c - 1])
    return start_point


def start_first(start):
    """
    시작점을 먼저 정리 해주는 함수
    대문자이고 열쇠가 있으면 처리 후 start 반환
    대문자이고 열쇠 없으면 False 반환
    문서이거나 소문자이면 start 반환
    """
    if not (start):
        return False

    if board[start[0]][start[1]].isupper():
        if board[start[0]][start[1]].lower() not in key:
            return False

        else:
            board[start[0]][start[1]] = '.'
            return start

    elif board[start[0]][start[1]].islower():
        key.add(board[start[0]][start[1]])
        board[start[0]][start[1]] = '.'
        return start

    else:
        return start


T = int(input())

for _ in range(T):
    # 입력 정리
    r, c = map(int, input().split())
    board = [list(map(str, input())) for _ in range(r)]

    start_point = check_start(board)

    key = set(input())

    if len(start_point) == 0:
        start_point = [False]

    # for x in board:
    #     print(x)

    cnt = 0  # 함수의 리턴값으로 다서 빋아줄것

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    len_key = len(key)
    while True:
        for z in start_point:
            cnt += bfs_doc(z)
        if len(key) == len_key:
            break
        else:
            len_key = len(key)
    print(cnt)

    # print(start_point)
    # for x in board:
    #     print(x)
    # print(key)

# 방문처리를 해야함 -> 왔던 곳도 또 갈 수 있음 -> 문을 열거나, 문서를 얻거나, 열쇠를 얻으면 방문처리 리스트를 초기화 해줌
# 생각이 되는 문제점 -> 서로 다른 큐에 대해서 방문처리 리스트는 달라야하는데 위 처럼 하면 다 같아져서 연산의 수가 증가함
# 시작하는 점만 영구적으로 방문처리 해줄지 생각할것
# 시작하는 곳 바꿔주기
# 시작점은 벽이 있는 곳 빼고 전부 다 가능함 -> 구현 아직 안함
# 만약에 소문자나 대문자로 시작하면 그건 bfs 안에서 처리해 주면 됨
# 시간을 줄이는 생각을 해야함
# 시작점을 한번 들어가면 다시는 못들어 가는데 이것도 아님 -> 수정해야함
