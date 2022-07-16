"""
    문제 이름 : 별자리 만들기
    URL : https://www.acmicpc.net/problem/4386
    ----------------------------------------------
    <문제 설명>
    별자리를 만들 것인데 조건은 아래와 같다
    1. 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다
    2. 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다
    2차원 평면위에 별들의 좌표가 있을 때, 별자리를 만드는데 드는 최소 비용을 구해라

    여기서 거리는 유클리디안 거리를 이용해서 구하면 됨
"""
num_star = int(input())
loc_star = []
for _ in range(num_star):
    a, b = map(float, input().split())
    loc_star.append([a, b])

parent = [x for x in range(num_star + 1)]


def find(node):
    """ 부모노드를 찾아주는 함수 """
    if parent[node] == node: return node

    p = find(parent[node])
    parent[node] = p
    return p


def union(node_1, node_2):
    """ 두 노드를 합쳐주는 함수 """
    node_1 = find(node_1)
    node_2 = find(node_2)

    if node_1 > node_2:
        parent[node_1] = node_2
    else:
        parent[node_2] = node_1


def dist_star():
    """ 별들의 거리를 구해주는 함수 """
    dist = []
    for node_1 in range(num_star):
        node_1_loc = loc_star[node_1]
        for node_2 in range(node_1, num_star):
            if node_1 == node_2:
                continue

            node_2_loc = loc_star[node_2]
            dist.append([get_dist(node_1_loc, node_2_loc), node_1 + 1, node_2 + 1])

    return dist


def get_dist(node_1, node_2):
    """ 유클리디안 거리 구하는 함수 """
    x_1, y_1 = node_1
    x_2, y_2 = node_2

    dist = (abs(x_1 - x_2) ** 2 + abs(y_1 - y_2) ** 2) ** (1/2)
    return dist


def MST():
    """ 최소 스패닝 트리를 구현해주는 함수 """
    dist = dist_star()
    dist.sort()

    result = 0

    for cost, node_1, node_2 in dist:
        if find(node_1) != find(node_2):
            union(node_1, node_2)
            result += cost

    return "{:.2f}".format(result)


print(MST())

"""
        소요 시간
    20분 정도 걸림
        
        핵심 정리
    1. 주어지는 좌표로 거리를 구한 후, 그 거리를 바탕으로 최소 스패닝 트리 하면 됨
"""