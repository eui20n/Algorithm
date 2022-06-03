"""
    문제 이름 : 복제 로봇
    URL : https://www.acmicpc.net/problem/1944
    ----------------------------------------------
    <문제 설명>
    복제 로봇이 미로로 감 -> 입구와 열쇠가 있는 곳에 로봇을 복제함
    --> 모든 열쇠를 찾으면서 로봇이 움직이는 횟수의 합을 최소로 하는 프로그램을 만들어라
    --> 만약에 열쇠를 다 먹을 수 없으면 -1 출력
"""
from collections import deque

N, cnt_key = map(int, input().split())
miro = [list(map(str, input())) for _ in range(N)]


def loc_robot():
    """ 초기의 시작점을 찾아주는 함수 """
    for x in range(N):
        for y in range(N):
            if miro[x][y] == 'S':
                return x, y


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[False] * N for _ in range(N)]
    return visited


def check_dist(x, y):
    """ 거리를 확인하는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = visited_init()
    visited[x][y] = True

    q = deque()

    # x, y, 길이, 좌표(시작점이나 열쇠), 시작한 곳이 시작 점인지 아닌지 구분해주는 문자, 미로 정보
    q.append([x, y, 0, (x, y), 'O'])

    # 가중치, 노드, 노드를 담아줄 리스트 -> 정수, 튜플, 튜플
    node_node_list = []

    while q:
        x, y, dist, check, start_check = q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= N:
                continue
            if 0 > ny or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            if miro[nx][ny] == '1':
                continue

            if miro[nx][ny] == 'K':
                if check[0] == nx and check[1] == ny:
                    continue

                miro[nx][ny] = '0'
                node_node_list.append([dist + 1, (nx, ny), check])

                q.append([nx, ny, 0, (nx, ny), start_check])
                visited = visited_init()
                visited[nx][ny] = True

                if start_check == 'O':
                    q = deque()
                    q.append([nx, ny, 0, (nx, ny), 'X'])
                    break
                continue

            q.append([nx, ny, dist + 1, check, start_check])
            visited[nx][ny] = True

    return node_node_list


def find(parent, node):
    """ 부모 노드를 찾아 주는 함수 """
    if parent[node] == node: return node

    p = find(parent, parent[node])
    parent[node] = p
    return p


def union(parent, node_1, node_2):
    """ 두 노드를 합해주는 함수 """
    node_1 = find(parent, node_1)
    node_2 = find(parent, node_2)

    if node_1 == node_2:
        return

    if node_1[0] == node_2[0]:
        if node_1[1] > node_2[1]:
            parent[node_1] = node_2

        else:
            parent[node_2] = node_1

    else:
        if node_1[0] > node_2[0]:
            parent[node_1] = node_2
        else:
            parent[node_2] = node_1


def make_parent_node(arr):
    """ 부모 노드를 만들어 주는 함수 """
    temp = set([])
    for weight, node_1, node_2 in arr:
        temp.add(node_1)
        temp.add(node_2)

    parent = {list(temp)[x]: list(temp)[x] for x in range(len(temp))}

    if len(temp) != cnt_key + 1:
        return set([])
    return parent


def find_key_min_cost():
    """ 최소 비용으로 열쇠를 찾아 주는 함수 """
    x, y = loc_robot()
    graph = check_dist(x, y)
    result = 0
    parent = make_parent_node(graph)

    if len(parent) == 0:
        return -1

    graph.sort()

    for cost, node_1, node_2 in graph:
        if find(parent, node_1) != find(parent, node_2):
            union(parent, node_1, node_2)
            result += cost

    return result


# print(find_key_min_cost())

x, y = loc_robot()
print(check_dist(x, y))


# 시작점 - K
# 다른 K - 다른 K
# 방문 처리 고민하기
# 좀만 손 보면 될듯