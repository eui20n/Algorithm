"""
    문제 이름 : 다리 만들기 2
    URL : https://www.acmicpc.net/problem/17472
    ----------------------------------------------
    <문제 설명>
    각 섬에 다리를 만들어야 한다 -> 모든 섬을 연결하고 싶다
    다리의 양 끝은 섬과 인접한 바다 위에 있어야 하고, 한 다리의 방향이 중간에 바뀌면 안되며, 다리의 길이는 2 이상이어야 한다
    이 때 다리의 최솟 값을 구해라 -> 만약에 교차하는 다리가 있다면 교차하는 지점을 1로 보는게 아님 -> 다리 각각의 길이만 더해주면 될 듯
"""
from collections import deque

R, C = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(R)]


def print_arr(arr) -> None:
    """ 출력을 원하는 배열을 넣으면 배열을 출력 해주는 함수 """
    print(*arr, sep='\n')


def node_init() -> dict:
    """ 노드 초기값 """
    temp = {}
    for x in range(R):
        for y in range(C):
            if land[x][y] != 0:
                temp[(x, y)] = (x, y)

    return temp


def visited_init() -> list:
    """ 방문 처리 리스트를 만들어 줄 함수 """
    visited = [[False] * C for _ in range(R)]
    return visited


def sep_land() -> dict:
    """ 섬을 구분해줄 함수 """
    visited = visited_init()
    parent = node_init()
    cnt = 1

    for x in range(R):
        for y in range(C):
            if not visited[x][y] and land[x][y] != 0:
                sep_bfs_land(x, y, cnt, visited, parent)
                cnt += 1

    return parent


def sep_bfs_land(x, y, cnt, visited, parent) -> None:
    """ 각각의 영역을 구분해 주는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited[x][y] = True
    land[x][y] = cnt

    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if visited[nx][ny]:
                continue
            if land[nx][ny] == 0:
                continue

            q.append([nx, ny])
            visited[nx][ny] = True
            land[nx][ny] = cnt
            parent[(nx, ny)] = (x, y)


def find(parent, node) -> tuple:
    """ 부모 노드를 찾아주는 함수 """
    if parent[node] == node: return node

    p = find(parent, parent[node])
    parent[node] = p
    return p


def union(parent, node_1, node_2) -> None:
    """ 두 노드를 합쳐주는 함수 """
    node_1 = find(parent, node_1)
    node_2 = find(parent, node_2)

    if node_1 > node_2:
        parent[node_1] = node_2

    else:
        parent[node_2] = node_1


def go_vertical(x, y, visited, parent) -> list:
    """ 세로로 가는 것 """
    dx = [-1, 1]
    dy = [0, 0]

    visited[x][y] = True
    standard = find(parent, (x, y))

    q = deque()
    q.append([x, y, 0])

    while q:
        x, y, time = q.popleft()
        for z in range(2):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if visited[nx][ny]:
                continue

            if land[standard[0]][standard[1]] == land[nx][ny]:
                q.append([nx, ny, 0])
                visited[nx][ny] = True
            elif land[nx][ny] == 0:
                q.append([nx, ny, time + 1])
                visited[nx][ny] = True
            else:
                end = find(parent, (nx, ny))
                if time >= 2:
                    return [time, standard, end]

    return []


def go_horizontal(x, y, visited, parent) -> list:
    """ 가로로 가는 것 """
    dx = [0, 0]
    dy = [-1, 1]

    visited[x][y] = True
    standard = find(parent, (x, y))

    q = deque()
    q.append([x, y, 0])

    while q:
        x, y, time = q.popleft()
        for z in range(2):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= R:
                continue
            if 0 > ny or ny >= C:
                continue
            if visited[nx][ny]:
                continue

            if land[standard[0]][standard[1]] == land[nx][ny]:
                q.append([nx, ny, 0])
                visited[nx][ny] = True
            elif land[nx][ny] == 0:
                q.append([nx, ny, time + 1])
                visited[nx][ny] = True
            else:
                end = find(parent, (nx, ny))
                if time >= 2:
                    return [time, standard, end]

    return []


def dist_land() -> tuple:
    """ 각각의 섬 마다 거리를 구해주는 함수 """
    visited_horizontal = visited_init()
    visited_vertical = visited_init()

    parent = sep_land()

    dist = []

    for x in range(R):
        for y in range(C):
            if land[x][y] == 0:
                continue
            if not visited_vertical[x][y]:
                if temp := list(go_vertical(x, y, visited_vertical, parent)):
                    dist.append(temp)

            if not visited_horizontal[x][y]:
                if temp := list(go_horizontal(x, y, visited_horizontal, parent)):
                    dist.append(temp)

    return dist, parent


def main() -> int:
    """ 함수를 실행 시켜줄 함수 """
    dist, parent = dist_land()

    dist.sort()
    result = 0

    for weight, node_1, node_2 in dist:
        if find(parent, node_1) != find(parent, node_2):
            union(parent, node_1, node_2)
            result += weight

    for node in parent:
        find(parent, node)

    if len(set(parent.values())) == 1:
        return result

    return -1


print(main())

"""
        소요 시간
    2시간 30분
    
        핵심 정리
    1. 각각의 섬을 노드라고 생각한다.
    2. 각 노드에서 서로 가는데 걸리는 시간을 구한다.
    3. 그 구한 시간으로 MST하면 된다.
"""