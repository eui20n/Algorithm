"""
    문제 이름 : 불
    URL : https://www.acmicpc.net/problem/5427
    ----------------------------------------------
    <문제 설명>
    매 초 마다 불은 동서남북 방향으로 인접한 빈 공간으로 펴져나간다. 상근이도 동서남북 인접한 칸으로 이동할 수 있으며 1초가 걸린다
    상근이는 불이 있는칸, 불이 붙으려는 칸으로는 이동할 수 없다 -> 상근이가 있는 칸에 불이 옮겨옴과 동시에 다른 칸으로 이동할 수 있다
"""
from collections import deque


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[False] * C for _ in range(R)]
    return visited


def loc_start_fire() -> tuple:
    """ 시작점과 불의 위치를 찾아 주는 함수 """
    start = []
    fire = []
    for x in range(R):
        for y in range(C):
            if board[x][y] == '@':
                start.append([x, y])
                continue

            if board[x][y] == '*':
                fire.append([x, y, '*'])

    return start, fire


def escape_building() -> str:
    """ 탈출하는데 걸리는 최소 시간을 반환해주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    start, fire = loc_start_fire()

    q = deque()

    visited = visited_init()
    visited[start[0][0]][start[0][1]] = True
    for fire_x, fire_y, check in fire:
        visited[fire_x][fire_y] = True
        q.append([fire_x, fire_y, check])

    q.append([start[0][0], start[0][1], 1])

    while q:
        x, y, check = q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R or 0 > ny or ny >= C:
                if check != '*':
                    return check
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == '#':
                continue

            if check != '*':
                q.append([nx, ny, check + 1])

            else:
                q.append([nx, ny, check])

            visited[nx][ny] = True

    return "IMPOSSIBLE"


T = int(input())
for _ in range(T):
    C, R = map(int, input().split())
    board = [list(map(str, input())) for _ in range(R)]
    q = deque()
    q_fire = deque()
    print(escape_building())

# 내일하자
