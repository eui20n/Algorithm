"""
    문제 이름 : 로봇 청소기
    URL : https://www.acmicpc.net/problem/4991
    ----------------------------------------------
    <문제 설명>
    로봇 청소기가 더러운 칸을 깨끗하게 만드는게 필요한 이동 횟수가 몇번인가

    깨끗한 칸 : .
    더러운 칸 : * -> 10개가 넘지 않음
    가구 : x
    로봇 청소기의 시작 위치 : o -> 로봇 청소기는 무조건 한개 이다

    더러운 칸에 가면 q랑 방문처리 리스트 초기화 하기
"""
from collections import deque


def find_cleaner():
    """ 로봇 청소기의 위치를 찾아주는 함수 """
    for x in range(R):
        for y in range(C):
            if dirty_home[x][y] == 'o':
                dirty_home[x][y] = '.'
                return [x, y]


def cnt_dust():
    """ 더러운 곳이 몇개 있는지 세주는 함수 """
    cnt = 0

    for x in range(R):
        for y in range(C):
            if dirty_home[x][y] == '*':
                cnt += 1

    return cnt


def visited_init():
    """ 방문 처리 리스트를 만들어줄 함수 """
    visited = [[False] * C for _ in range(R)]
    return visited


def clean_house(x, y):
    """ 청소를 해주는 함수 """

    cnt = cnt_dust()

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = visited_init()
    visited[x][y] = True

    q = deque()
    q.append([x, y, 0])

    while q:
        x, y, time = q.popleft()

        if cnt == 0:
            return time

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if clean_con(nx, ny, visited):

                if dirty_home[nx][ny] == '*':
                    cnt -= 1
                    dirty_home[nx][ny] = '.'

                    visited = visited_init()
                    q = deque()

                q.append([nx, ny, time + 1])
                visited[nx][ny] = True

                # print('x:', nx, 'y:', ny, 'time:', time)

    return -1


def clean_con(x, y, visited):
    """ 조건 함수 """
    if 0 > x or x >= R:
        return False
    if 0 > y or y >= C:
        return False
    if visited[x][y]:
        return False
    if dirty_home[x][y] == 'x':
        return False
    return True


while True:
    C, R = map(int, input().split())
    if R == 0 and C == 0:
        break
    dirty_home = [list(map(str, input())) for _ in range(R)]

    robot_cleaner = find_cleaner()
    # print(robot_cleaner)

    print(*dirty_home, sep = '\n')
    print(clean_house(robot_cleaner[0], robot_cleaner[1]))
