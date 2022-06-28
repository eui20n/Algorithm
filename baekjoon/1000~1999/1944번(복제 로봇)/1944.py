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


def loc_robot_key():
    """ 로봇과 열쇠의 위치를 찾아주는 함수 """
    temp = []
    for x in range(N):
        for y in range(N):
            if miro[x][y] == 'S':
                temp.append([x, y])

            if miro[x][y] == 'K':
                temp.append([x, y])

    return temp


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[False] * N for _ in range(N)]
    return visited


def check_dist(x, y):
    """ 거리를 확인하는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    start_x, start_y = x, y

    visited = visited_init()
    visited[start_x][start_y] = True

    q = deque()
    # x좌표, y좌표, 길이
    q.append([start_x, start_y, 0])

    node_list = []

    while q:
        x, y, dist = q.popleft()
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
                node_list.append([dist + 1, (start_x, start_y), (nx, ny)])

            q.append([nx, ny, dist + 1])
            visited[nx][ny] = True

    return node_list


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
    robot_key = loc_robot_key()

    graph = []
    for x, y in robot_key:
        graph.extend(check_dist(x, y))

    result = 0
    parent = make_parent_node(graph)

    if len(parent) == 0:
        return -1

    graph.sort()

    for cost, node_1, node_2 in graph:
        if find(parent, node_1) != find(parent, node_2):
            union(parent, node_1, node_2)
            result += cost

    for x in range(len(robot_key) - 1):
        node_1 = tuple(robot_key[x])
        node_2 = tuple(robot_key[x + 1])
        if find(parent, node_1) != find(parent, node_2):
            return -1
    return result


print(find_key_min_cost())


"""
        핵심정리
    1. 열쇠와 시작 위치를 노드로 잡고 그 노드에서 가는데 걸리는 시간을 BFS로 구하기
    2. 그렇게 구한 노드와 시간을 가지고 MST하면 됨
    
"""