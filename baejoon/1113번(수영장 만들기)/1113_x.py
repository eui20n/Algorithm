"""
    문제 이름 : 수영장 만들기
    URL : https://www.acmicpc.net/problem/1113
    ----------------------------------------------
    <문제 설명>
    그래프가 주어질때 물이 고일 수 있는지, 그리고 고인다면 얼마나 고이는지 출력하면 된다.
    1 <= 물의 높이 <= 9 이다
    무조건 물이 고일 수 있다고 생각할 것 -> 물이 고일 수 없을시 출력값이 없음
"""
from collections import deque

R, C = map(int, input().split())
graph = [list(map(int, input())) for _ in range(R)]


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[False] * C for _ in range(R)]
    return visited


def find_min_max():
    """ 최소값과 최대값을 찾아주는 함수 """
    max_num = 0
    min_num = float('inf')

    for x in range(R):
        for y in range(C):
            if graph[x][y] > max_num:
                max_num = graph[x][y]

            if graph[x][y] < min_num:
                min_num = graph[x][y]

    return [min_num, max_num]


def make_pool(x, y, layer, visited):
    """ 수영장을 만들어 주는 함수 """
    # 잠길 곳이 없어서 0을 반환해줌
    if graph[x][y] > layer:
        visited[x][y] = True
        return 0

    if x == 0 or y == 0 or x == R - 1 or y == C - 1:
        check_connect(x, y, visited, layer)
        return 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = True

    q = deque()
    q.append([x, y])
    result = 1

    while q:
        x, y = q.popleft()

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if make_pool_con(nx, ny, visited, layer):
                if nx == 0 or nx == R - 1 or ny == 0 or ny == C - 1:
                    check_connect(nx, ny, visited, layer)
                    return 0

                q.append([nx, ny])
                visited[nx][ny] = True
                result += 1

    return result


def make_pool_con(x, y, visited, layer):
    """ make_pool의 조건 함수 """
    if 0 > x or x >= R:
        return False
    if 0 > y or y >= C:
        return False
    if visited[x][y]:
        return False
    if graph[x][y] > layer:
        return False
    return True


def check_connect(x, y, visited, layer):
    """ 가장 자리와 만나는 것이 뭔지 알려주는 함수 """

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = True

    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if make_pool_con(nx, ny, visited, layer):
                visited[nx][ny] = True
                q.append([nx, ny])


def main():
    """ 함수를 실행 시키는 함수 """
    cnt = 0

    min_num, max_num = find_min_max()

    for layer in range(min_num, max_num + 1):
        visited = visited_init()

        for x in range(R):
            for y in range(C):
                if not visited[x][y]:
                    # print(layer)
                    # print(*visited, sep = '\n')
                    cnt += make_pool(x, y, layer, visited)
                    # print('cnt', cnt)

        # print('layer', layer)
        # print('cnt', cnt)

    return cnt


print(main())