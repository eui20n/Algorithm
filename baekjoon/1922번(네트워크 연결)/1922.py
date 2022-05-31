"""
    문제 이름 : 네트워크 연결
    URL : https://www.acmicpc.net/problem/1922
    ----------------------------------------------
    <문제 설명>
    모든 컴퓨터를 연결할 수 없는 경우는 없고, 하고 싶은건 컴퓨터를 연결했을때 최소 비용을 구하고 싶은 것이다
    유니온으로 연결하고 그 때 가중치를 보면 될 듯
"""


def find(x):
    """ 찾아주는 함수 """
    if computer[x] == x: return x

    p = find(computer[x])
    computer[x] = p
    return p


def union(a, b):
    """ 합해주는 함수 """
    a = find(a)
    b = find(b)

    if a == b:
        return

    if a > b:
        computer[a] = b
    else:
        computer[b] = a


def spanning_tree():
    """ 최소 스패닝 트리를 해주는 함수 """
    result = 0
    sorted_weight()
    for x, y, w in graph:
        if find(x) != find(y):
            result += w
            union(x, y)

    return result


def sorted_weight():
    """ 가중치로 정렬을 해주는 함수 """
    graph.sort(key=lambda x: x[2])


N = int(input())
M = int(input())
computer = [x for x in range(N + 1)]
graph = [list(map(int, input().split())) for _ in range(M)]

print(spanning_tree())
