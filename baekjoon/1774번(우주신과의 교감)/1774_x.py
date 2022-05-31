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
    dist = (temp_1 + temp_2) ** (1/2)
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

    parent[b] = a


def god_connected():
    """ 연결 되어 있는 신들 연결 해주는 함수 """
    for num_1, num_2 in connected_space_god:
        if find(space_god[num_1 - 1]) != find(space_god[num_2 - 1]):
            union(space_god[num_1 - 1], space_god[num_2 - 1])


def connect():
    """ 연결해주는 함수 """
    god_connected()

    space_god.sort(key=lambda x: (x[0], x[1]))
    dist = 0

    for x in range(len(space_god) - 1):
        prev_node, next_node = space_god[x], space_god[x + 1]
        if find(prev_node) != find(next_node):
            union(prev_node, next_node)
            dist += distance(prev_node, next_node)

    return round(dist, 2)


god_connected()
print(parent)
print(connect())

# 생각할 것 -> 부모 노드의 키 값을 정수로 해서 순서를 바로 처리할지, 그냥 튜플로 받고 연결 된거랑 안된거 나눌지 생각하기
# 문제 진짜 잘 읽자 -> 총 통로 길이가 아니라 새로 만들어야 하는 통로 길이네
# 정렬 말고 거리가 가장 적게 걸리는게 뭔지 파악하기
