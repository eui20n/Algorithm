"""
    문제 이름 : 물대기
    URL : https://www.acmicpc.net/problem/1368
    ----------------------------------------------
    <문제 설명>
    자기 자신도 MST에 포함되어야 함 -> 트리가 아니긴함
    MST를 만드는 문제가 아니라 최소 비용을 구하는 문제임
"""
N = int(input())
cost = [0]
for _ in range(N):
    temp_cost = int(input())
    cost.append(temp_cost)

matrix = [list(map(int, input().split())) for _ in range(N)]

connect_field = [x for x in range(N + 1)]


def change_matrix() -> list:
    """ 행렬 형태를 그래프 형태로 바꾸기 -> 대칭 행렬이라서 한쪽만 봐도 됨, 그리고 0번 노드에 우물과의 비용 추가 """
    graph = []
    for r in range(N):
        for c in range(r, N):
            if r == c:
                continue
            graph.append([r + 1, c + 1, matrix[r][c]])

    for x in range(1, len(cost)):
        graph.append([0, x, cost[x]])

    return graph


def find(node) -> int:
    """ 부모 노드를 찾아주는 함수 """
    if connect_field[node] == node: return node

    p = find(connect_field[node])
    connect_field[node] = p
    return p


def union(node_1, node_2) -> None:
    """ 두 노드를 연결해주는 함수 """
    node_1 = find(node_1)
    node_2 = find(node_2)

    if node_1 > node_2:
        connect_field[node_1] = node_2
    else:
        connect_field[node_2] = node_1


def min_cost_water() -> int:
    """ 울을 댈수 있는 최소 비용을 구하는 함수 """
    graph = change_matrix()
    result = 0

    graph.sort(key=lambda x: x[2])

    for node_1, node_2, weight in graph:
        if find(node_1) != find(node_2):
            union(node_1, node_2)
            result += weight

    return result


print(min_cost_water())


"""
        핵심 정리
    1. 처음에 자기 자신과 우물을 연결하면 나오는 비용이 주어지는데, 이걸로 새로운 노드 관계(우물 - 자기자신)을 만들어서 MST를 하면 됨
    2. 시간은 30분 정도 걸림
"""