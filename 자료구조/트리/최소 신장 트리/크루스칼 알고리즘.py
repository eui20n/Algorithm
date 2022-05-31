"""
    백준 1197번을 기준으로 구현한 최소 신장 트리
    https://www.acmicpc.net/problem/1197

    짧은 과정
    1. 가중치로 정렬
    2. 유니온 파인드를 이용해서 연결해줌
    2-1. 근데 만약 이 과정에서 연결했을때 사이클이 생기면 하면 안됨
    2-2. 사이클이 안생기면 하면 됨
    3. 위 과정을 모든 노드에 대해서 반복해주면 됨
"""


V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]
parent = [x for x in range(V + 1)] # 부모를 노드의 수만큼 해주면 됨 -> +1인건 계산하기 편하게 하기 위해서


def sorted_weight():
    """ 가중치를 정렬해주는 함수 """
    # 입력에서 인덱스2번째 값이 가중치라서, 가중치로 정렬해준 것임
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
        # 아직 연결을 안했는데 부모가 서로 같다면 그것은 사이클이 있다는 소리임
        if find(x) != find(y):
            union(x, y)
            result += w
            spanning_tree.add(x)
            spanning_tree.add(y)

    return result


print(MST())
