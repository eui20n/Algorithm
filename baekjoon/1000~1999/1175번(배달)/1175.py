"""
    문제 이름 : 배달
    URL : https://www.acmicpc.net/problem/1175
    ----------------------------------------------
    <문제 설명>
    S : 현재 있는 곳으로 1개만 있음
    C : 배달해야 하는 곳으로 2개 있음
    # : 갈 수 없는 곳
    . : 갈 수 있는 곳
    같은 방향으로 두 번 연속 이동 할 수 없음 -> 큐에 현재 방향에 대한 정보도 넣어야 함
    한 개를 배달해주면, 초기화 되고 다시 해야함
    배달을 하는데 걸리는 최소값을 출력해라
    만약에 최소 시간이 없으면 -1을 출력해라
"""
from collections import deque

R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]


def find_loc():
    """ 현재 위치를 찾아주는 함수 """
    for x in range(R):
        for y in range(C):
            if board[x][y] == 'S':
                return x, y


def change_delivery():
    """ 배달할 장소를 C가 아닌 1과 2로 바꿔주는 함수 """
    cnt = 1
    for x in range(R):
        for y in range(C):
            if board[x][y] == 'C':
                board[x][y] = str(cnt)
                cnt += 1


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[0] * C for _ in range(R)]
    return visited


def delivery(x, y):
    """ 배달 해주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = visited_init()
    visited[x][y] = 8

    q = deque()
    # x좌표, y좌표, 방향, 시간, 배달1, 배달2, 방문처리 리스트 = > 처음은 시작점임
    q.append([x, y, 0, 0, 0, 0, visited])

    while q:
        x, y, d, time, delivery_1, delivery_2, visited = q.popleft()
        if delivery_1 == 1 and delivery_2 == 1:
            return time

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if board[nx][ny] == '#':
                continue
            if visited[nx][ny] & (1 << z):
                continue
            if time != 0 and d == z:
                continue

            if board[nx][ny] == '1' and delivery_1 == 0:
                visited = visited_init()

                visited[nx][ny] |= (1 << z)
                q.append([nx, ny, z, time + 1, 1, delivery_2, visited])
                break

            if board[nx][ny] == '2' and delivery_2 == 0:
                visited = visited_init()

                visited[nx][ny] |= (1 << z)
                q.append([nx, ny, z, time + 1, delivery_1, 1, visited])
                break

            visited[nx][ny] |= (1 << z)
            q.append([nx, ny, z, time + 1, delivery_1, delivery_2, visited])

    return -1


def main():
    """ 함수를 실행 시켜줄 함수 """
    x, y = find_loc()
    change_delivery()
    result = delivery(x, y)
    return result


print(main())

""" 
        핵심 정리
    1. 같은 곳을 2번 이상 갈 수 없음 -> 2번 이상 가게 되면 그 경우에 대해서는 무조건 무한 루프임(방향에 대해서)
    2. 큐를 초기화 시키면 안됨 -> 이러면 최단 경로를 구하는게 아니게 됨
    
        소요 시간 : 약 2시간(15:00 ~ 17:00)
"""