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
    """ 최대값과 최소값을 찾아주는 함수 """
    max_num = 0
    min_num = float('inf')

    for x in range(R):
        for y in range(C):
            if graph[x][y] > max_num:
                max_num = graph[x][y]

            if graph[x][y] < min_num:
                min_num = graph[x][y]

    return min_num, max_num


def make_pool(x, y, layer, visited):
    """ 수영장을 만들어 주는 함수 """
    if graph[x][y] >= layer:
        visited[x][y] = True
        return 0

    if x == 0 or x == R - 1 or y == 0 or y == C - 1:
        return 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = True

    q = deque()
    q.append([x, y])
    result = 1
    side = False

    while q:
        x, y = q.popleft()

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if make_pool_con(nx, ny, layer, visited):
                if nx == 0 or nx == R - 1 or ny == 0 or ny == C - 1:
                    side = True

                visited[nx][ny] = True
                q.append([nx, ny])
                result += 1

    if side:
        return 0

    return result


def make_pool_con(x, y, layer, visited):
    """ make_pool의 조건 함수 """
    if 0 > x or x >= R:
        return False
    if 0 > y or y >= C:
        return False
    if visited[x][y]:
        return False
    if graph[x][y] >= layer:
        return False
    return True


def main():
    """ 함수를 실행 시킬 함수 """
    cnt = 0
    min_num, max_num = find_min_max()

    for layer in range(min_num + 1, max_num + 1):
        visited = visited_init()

        for x in range(R):
            for y in range(C):
                if not visited[x][y]:
                    cnt += make_pool(x, y, layer, visited)
                    # print(f"layer: {layer}", f"cnt: {cnt}")
                    # print(*visited, sep = '\n')
                    # print()

        # print(f"layer: {layer}")
        # print(f"cnt: {cnt}")

    return cnt


print(main())

# 높이가 1이면 2가 와야지 물을 채울 수 있음 -> 이런 식으로 구현할 것
# (6, 10)이 1번씩 더해짐
