"""
    문제 이름 : 모양 만들기
    URL : https://www.acmicpc.net/problem/16932
    ----------------------------------------------
    <문제 설명>
    주어지는 배열에서 숫자 하나만 바꿔서 만들 수 있는 배열의 크기중 제일 큰게 몇인지 구하면 됨
"""
from collections import deque

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
sep_block = [[0] * C for _ in range(R)]


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [0] * C
    return visited


def check_size(x, y, visited):
    """ 모양의 크기를 구하는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[y] |= (1 << x)

    shape_block = [[x, y]]

    q = deque()
    q.append([x, y])
    size = 1

    while q:
        x, y = q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if board[nx][ny] == 0:
                continue
            if visited[ny] & (1 << nx):
                continue

            size += 1
            q.append([nx, ny])
            shape_block.append([nx, ny])
            visited[ny] |= (1 << nx)

    return shape_block, size


def change_size(shape_block, size, cnt):
    """ 크기로 바꿔주는 함수 """
    for x, y in shape_block:
        board[x][y] = size
        sep_block[x][y] = cnt


def max_size(x, y, visited):
    """ 최대 크기를 구해주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    size = 0
    block = set()

    visited[y] |= (1 << x)

    for z in range(4):
        nx = x + dx[z]
        ny = y + dy[z]
        if 0 > nx or nx >= R:
            continue
        if 0 > ny or ny >= C:
            continue
        if sep_block[nx][ny] in block:
            continue

        size += board[nx][ny]
        block.add(sep_block[nx][ny])

    return size + 1


def main():
    """ 함수를 실행 시켜줄 함수 """
    visited = visited_init()
    result = 0
    cnt = 1

    for x in range(R):
        for y in range(C):
            if board[x][y] == 1 and not visited[y] & (1 << x):
                shape_block, size = check_size(x, y, visited)
                change_size(shape_block, size, cnt)
                cnt += 1

    for x in range(R):
        for y in range(C):
            if board[x][y] == 0 and not visited[y] & (1 << x):
                temp = max_size(x, y, visited)
                if result < temp:
                    result = temp
    return result


print(main())


"""
        핵심 정리
    1. 브루트포스로 하면 시간이 초과가 걸린다 -> bfs한번에 답을 구할 수 있어야 함
    2. 먼저 각 구역의 크기와 그 구역을 구분해 준다
    3. 그 후 각각의 0에서 인접한 구역을 더해주면 된다
    4. 3번에서 더할때 같은 구역을 또 발생하는 일이 있어서, 한번 더한 구역은 따로 표시를 해서 다시 더해지지 않게 한다
"""