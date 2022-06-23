"""
    문제 이름 : 불켜기
    URL : https://www.acmicpc.net/problem/11967
    ----------------------------------------------
    <문제 설명>
    정사각형의 방이 있다. 각 방에는 (1,1) 부터 (N,N)까지 번호가 매겨져 있다
    처음에 불이 켜져있는 방은 (1,1)이다. 어떤 방에는 다른 방의 불을 끄고 켤 수 있는 스위치가 달려있다.
    이 때 불을 켤 수 있는 최대 방의 개수를 구해라

    각 방의 불을 킬 수 있는 정보를 해쉬와 맵에 저장해서 가장 빠르게 접근할 수 있도록 하기
"""
from collections import deque

N, M = map(int, input().split())
light_info = {}
temp_key = set()
for _ in range(M):
    x_1, y_1, x_2, y_2 = map(int, input().split())
    x_1, y_1, x_2, y_2 = x_1 - 1, y_1 - 1, x_2 - 1, y_2 - 1
    if (x_1, y_1) not in temp_key:
        light_info[(x_1, y_1)] = {(x_2, y_2)}
        temp_key.add((x_1, y_1))

    elif (x_1, y_1) in temp_key:
        light_info[(x_1, y_1)] = light_info[(x_1, y_1)] | {(x_2, y_2)}


def visited_init():
    """  방문 처리 리스트를 만들어 주는 함수 """
    visited = [[False] * N for _ in range(N)]
    return visited


def light_on(x, y, light_board):
    """ 불을 키는 함수 """
    if (x, y) not in temp_key:
        return

    for x, y in light_info[(x, y)]:
        light_board[x][y] = True


def go_light_on():
    """ 불을 켜려고 가는 함수로 BFS로 구현할 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    light_board = visited_init()
    light_board[0][0] = True

    light_on(0, 0, light_board)

    visited = visited_init()
    visited[0][0] = True

    q = deque()
    q.append([0, 0])

    while q:
        x, y = q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= N:
                continue
            if 0 > ny or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            if not light_board[nx][ny]:
                continue

            if (nx, ny) in temp_key:
                light_on(nx, ny, light_board)
                temp_key.remove((nx, ny))
                visited = visited_init()

            q.append([nx, ny])
            visited[nx][ny] = True

    return light_board


def count_light_on_room(light_board):
    """ 불이 켜진 방이 몇개인지 세주는 함수 """
    cnt = 0

    for x in range(N):
        for y in range(N):
            if light_board[x][y]:
                cnt += 1

    return cnt


def main():
    """ 함수를 실행 시켜줄 함수 """
    light_board = go_light_on()
    result = count_light_on_room(light_board)

    return result


print(main())

"""
        핵심 정리
    1. 문제를 잘못 읽었네;;; 이런 실수 많이 하는데, 이런 실수 하면 안되는데;;;
    2. 불을 키면 방문처리 리스트를 초기화해서 다시 탐색을 하는 방식으로 문제를 품 -> 이 방식이 별로 안좋은 것 같음
    3. 또한 불을 키면, 불을 켤 수 있게 정리해논 해쉬와 맵(temp_key)에서 그 좌표를 삭제해줘야함
"""