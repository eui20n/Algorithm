"""
    문제 이름 : 전력난
    URL : https://www.acmicpc.net/problem/6497
    ----------------------------------------------
    <문제 설명>
    그냥 전체 가중치에서 최소 가중치 빼주면 됨
    그리고 0 0 이 입력되면 끝임
"""


def find(x):
    """ 찾아 주는 함수 """
    if parent[x] == x: return x

    p = find(parent[x])
    parent[x] = p
    return p


def union(node_1, node_2):
    """ 합해주는 함수 """
    node_1 = find(node_1)
    node_2 = find(node_2)

    if node_1 > node_2:
        parent[node_1] = node_2
    else:
        parent[node_2] = node_1


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    total_cost = 0

    graph = []

    for _ in range(n):
        a, b, weight = map(int, input().split())
        total_cost += weight
        graph.append([weight, a, b])

    parent = [x for x in range(m)]
    graph.sort()

    for weight, node_1, node_2 in graph:
        if find(node_1) != find(node_2):
            union(node_1, node_2)
            total_cost -= weight

    print(total_cost)
