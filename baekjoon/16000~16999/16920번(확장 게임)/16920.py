"""
    문제 이름 : 확장 게임
    URL : https://www.acmicpc.net/problem/16920
    ----------------------------------------------
    <문제 설명>
    N x M 격자판 위에서 진행함, 플레이어는 1개 이상의 성을 가지고 있고 한 칸에는 성이 2개 이상일 수 없다
    1번 부터 순서대로 확장함

    각 플레이어가 가진 성의 수를 출력해라
"""

from collections import deque

R, C, player_cnt = map(int, input().split())
player_go = [0] + list(map(int, input().split()))
board = [list(map(str, input())) for _ in range(R)]


def visited_init() -> list:
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [0] * C
    return visited


def first_loc() -> list:
    """ 각 성의 처음 위치를 찾아주는 함수 """
    temp = [[] for _ in range(player_cnt)]
    for x in range(R):
        for y in range(C):
            if board[x][y].isnumeric():
                temp_num = int(board[x][y])
                temp[temp_num - 1].append([x, y, temp_num, 1])

    return temp


def go_castle() -> None:
    """ 성이 움직이는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    go_start = first_loc()

    visited = visited_init()

    for first_visited in go_start:
        for x, y, num, cnt in first_visited:
            visited[y] |= (1 << x)

    q = deque()
    for arr in go_start:
        q.append(arr)

    while q:
        p = q.popleft()
        temp_1 = []
        temp_2 = []

        for castle in p:
            for x, y, num, cnt in [castle]:
                for z in range(4):
                    nx = x + dx[z]
                    ny = y + dy[z]
                    if 0 > nx or nx >= R:
                        continue
                    if 0 > ny or ny >= C:
                        continue
                    if board[nx][ny] == '#':
                        continue
                    if board[nx][ny].isdigit():
                        continue
                    if visited[ny] & (1 << nx):
                        continue

                    if cnt == player_go[num]:
                        temp_1.append([nx, ny, num, 1])
                    elif cnt < player_go[num]:
                        temp_2.append([nx, ny, num, cnt + 1])

                    board[nx][ny] = str(num)
                    visited[ny] |= (1 << nx)

        if len(temp_1) != 0:
            q.append(temp_1)

        if len(temp_2) != 0:
            q.appendleft(temp_2)



def cnt_territory() -> list:
    """ 각각의 영역을 세주는 함수 """
    go_castle()
    result = [0] * player_cnt
    for x in range(R):
        for y in range(C):
            if not board[x][y].isnumeric():
                continue
            idx = board[x][y]
            result[int(idx) - 1] += 1

    return result


print(' '.join(map(str, cnt_territory())))

"""
        핵심정리
    1. bfs를 한번 돌려서 마무리 되어야함 -> 여러번 돌리면 시간 초과가 뜸
    2. appendleft를 쓰면 쉽게 해결 가능 -> 각각의 성에 대해서 묶어서 deque에 넣기
    3. 순서 잘 생각하기
"""