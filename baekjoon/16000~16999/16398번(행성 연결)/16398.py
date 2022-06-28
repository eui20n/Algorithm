"""
    문제 이름 : 행성 연결
    URL : https://www.acmicpc.net/problem/16398
    ----------------------------------------------
    <문제 설명>
    평범한 최소 스패팅 트리 문제인데 입력이 행렬도 들어옴
    -> 이렇게 들어온 입력만 잘 처리 하면 되는 문제
    -> 행렬도 대각 행렬임
"""
N = int(input())
matrix = [list(map(int ,input().split())) for _ in range(N)]
parent = [x for x in range(N + 1)]


def change_matrix():
    """ 입력에서 행렬형태로 주어지는걸 노드 형태로 바꾸기 """
    temp = []
    for x in range(N):
        for y in range(x, N):
            if x == y:
                continue
            temp.append([matrix[x][y], x, y])

    return temp


def find(x):
    """ 부모 노드를 찾아 주는 함수 """
    if parent[x] == x: return x

    p = find(parent[x])
    parent[x] = p
    return p


def union(a, b):
    """ 두 노드를 합해주는 함수 """
    a = find(a)
    b = find(b)

    if a == b:
        return

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def MST():
    """ 최소 스패닝 트리 """
    graph = change_matrix()
    result = 0

    graph.sort()

    for weight, x, y in graph:
        if find(x) != find(y):
            union(x, y)
            result += weight

    return result


print(MST())
