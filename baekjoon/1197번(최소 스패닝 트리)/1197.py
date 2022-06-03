"""
    문제 이름 : 최소 스패닝 트리
    URL : https://www.acmicpc.net/problem/1197
    ----------------------------------------------
    <문제 설명>
    노드와 노드, 그리고 그 사이의 가중치가 주어질때 최소 스패닝 트리를 만들어라
    출력은 최소 스패닝 트리의 가중치를 모두 더한 값이다
"""

V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]
parent = [x for x in range(V + 1)]


def sorted_weight():
    """ 가중치를 정렬해주는 함수 """
    graph.sort(key=lambda x: x[2])


def find(x):
    """ 부모 노드를 찾아주는 함수 """
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

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def MST():
    """ 최소 스패닝 트리 만들어 주는 함수 """
    sorted_weight()
    spanning_tree = set([])
    result = 0

    for x, y, w in graph:
        if find(x) != find(y):
            union(x, y)
            result += w
            spanning_tree.add(x)
            spanning_tree.add(y)

    return result


print(MST())

# 나중에 제출하기