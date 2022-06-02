"""
    문제 이름 : 우주신과의 교감
    URL : https://www.acmicpc.net/problem/1774
    ----------------------------------------------
    <문제 설명>
    그냥 연결하면 되는데, 가중치가 가장 적어야 한다
    -> 가중치가 없다...!
    -> 가중치는 유클리디안 거리인듯
"""

N, M = map(int, input().split())
space_god = [tuple(map(int, input().split())) for _ in range(N)]
connected_space_god = [tuple(map(int, input().split())) for _ in range(M)]
parent = {space_god[x]: space_god[x] for x in range(len(space_god))}


def distance(a, b):
    """ 거리 구해주는 함수 """
    temp_1 = (a[0] - b[0]) ** 2
    temp_2 = (a[1] - b[1]) ** 2
    dist = (temp_1 + temp_2) ** (1 / 2)
    return dist


def find(x):
    """ 부모 노드를 찾아 주는 함수 """
    if parent[x] == x: return x

    p = find(parent[x])
    parent[x] = p
    return p


def union(a, b):
    """ 합해주는 함수 """
    a = find(a)
    b = find(b)

    if a == b:
        return

    if a[0] > b[0]:
        parent[a] = b
        return

    if a[0] < b[0]:
        parent[b] = a
        return

    if a[1] > b[1]:
        parent[a] = b
        return

    if a[1] < b[1]:
        parent[b] = a
        return


def god_connected():
    """ 연결 되어 있는 신들 연결 해주는 함수 """
    for num_1, num_2 in connected_space_god:
        if find(space_god[num_1 - 1]) != find(space_god[num_2 - 1]):
            union(space_god[num_1 - 1], space_god[num_2 - 1])


def make_weight():
    """ 각 좌표에 거리는 구해주는 함수 """
    temp = []
    for x in range(len(space_god)):
        for y in range(len(space_god)):
            node_1, node_2 = space_god[x], space_god[y]

            if node_1 == node_2:
                continue

            temp.append([distance(node_1, node_2), node_1, node_2])

    return temp


def connect():
    """ 연결해주는 함수 """
    god_connected()
    new_space_god = make_weight()
    new_space_god.sort()
    dist = 0

    for weight, node_1, node_2 in new_space_god:
        if find(node_1) != find(node_2):
            union(node_1, node_2)
            dist += distance(node_1, node_2)

    return dist


print(format(connect(), ".2f"))


"""
    음 찝찝하구만....
    아마도 문제에 적혀 있지는 않지만 겹치는 노드가 있는 듯
"""
