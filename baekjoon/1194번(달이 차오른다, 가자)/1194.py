"""
    문제 이름 : 달이 차오른다, 가자
    URL : https://www.acmicpc.net/problem/1194
    ----------------------------------------------
    <문제 설명>
    열쇠를 먹어서 탈출하면 됨, 이때 가장 탈출할때 걸리는 최소값을 구하면 됨
    만약 탈출을 못하는 경우이면 -1 출력하면 됨
    열쇠를 먹고 방문처리를 초기화 시키면 될거 같음 -> 이 계산은 큐안에서 해야함, 각각의 상태는 서로 독립
    하지만 깊이(depth)는 초기화 시키면 안됨, 최종적으로 출력할껀 depth임
"""
from collections import deque

R, C = map(int, input().split())
board = [list(map(str, input())) for _ in range(R)]
kind_keys = {'a': 0b1, 'b': 0b10, 'c': 0b100, 'd': 0b1000, 'e': 0b10000, 'f': 0b100000}


def find_loc():
    """ 현재 위치 찾아주는 함수 """
    result = []

    for r in range(R):
        for c in range(C):
            if board[r][c] == '0':
                result.extend([r, c])
                board[r][c] = '.'
                return result


def escape_borad(x, y):
    """ 탈출 해주는 함수 """

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = init_visited()
    visited[0][y] |= 1 << x

    q = deque()
    q.append([x, y, 0, set([])])

    while q:
        p = q.popleft()

        for z in range(4):
            nx = p[0] + dx[z]
            ny = p[1] + dy[z]
            if con_1(nx, ny, visited, p[3]):
                loc_info = board[nx][ny]
                keys = key_change(p[3])

                if loc_info.isupper():
                    if loc_info.lower() not in p[3]:
                        continue

                if loc_info.islower():
                    if loc_info not in p[3]:
                        q.append([nx, ny, p[2] + 1, p[3] | {loc_info}])
                        keys = key_change(p[3] | {loc_info})
                        visited[keys][ny] |= 1 << nx
                        continue

                if loc_info == '1':
                    return p[2] + 1

                q.append([nx, ny, p[2] + 1, p[3]])
                visited[keys][ny] |= 1 << nx
    return -1


def init_visited():
    """ 방문처리 리스트 만들어 주는 함수 """
    visited = [[0] * C for _ in range(64)]
    return visited


def con_1(x, y, visited, get_keys):
    """ 방향 조건 함수 """
    keys = key_change(get_keys)

    if 0 > x or x >= R:
        return False
    if 0 > y or y >= C:
        return False
    if board[x][y] == '#':
        return False
    if visited[keys][y] & (1 << x):
        return False
    return True


def key_change(get_keys):
    """ 열쇠 정보를 숫자로 바꿔주는 함수 """
    keys = 0
    if len(get_keys) == 0:
        keys = 0

    else:
        for x in get_keys:
            keys += kind_keys.get(x)

    return keys


def main():
    start = find_loc()
    result = escape_borad(start[0], start[1])

    return result


print(main())

# 열쇠를 q안에서 관리해야할 듯
# 방문처리를 q안에서 관리하면 될듯
# q에 다 넣지말고 3차원 리스트를 생성해서 관리할 것 => q에 다 넣으니 메모리 초과가 뜨는거 같음
