"""
    문제 이름 : 세부
    URL : https://www.acmicpc.net/problem/13905
    ----------------------------------------------
    <문제 설명>
    집에서 섬까지 다리의 무게가 주어지고, 거기에서 최대 무게로 가져갈 수 있는 경로가 어딘지 구하면 됨
"""
import sys
sys.setrecursionlimit(10**5)


bridge_cnt, bridge_connect = map(int, input().split())
start, end = map(int, input().split())
board = []
kind_of_bridge = set([])
for _ in range(bridge_connect):
    node_1, node_2, weight = map(int, sys.stdin.readline().split())
    board.append([weight, node_1, node_2])


def connecting_init():
    """ 부모 노드를 초기화 해주는 함수 """
    connecting = [x for x in range(bridge_cnt + 1)]
    return connecting


def find(parent, node):
    if parent[node] == node: return node

    p = find(parent, parent[node])
    parent[node] = p
    return p


def union(parent, node_1, node_2):
    """ 합해주는 함수 """
    node_1 = find(parent, node_1)
    node_2 = find(parent, node_2)

    if node_1 == start:
        parent[node_2] = node_1
        return

    elif node_2 == start:
        parent[node_1] = node_2
        return

    if node_1 > node_2:
        parent[node_1] = node_2
        return

    else:
        parent[node_2] = node_1
        return


def connected():
    """ 주어진 연결 관계를 연결해 주는 함수 """
    connecting = connecting_init()
    board.sort(reverse=True)

    # 크루스칼 MST(최대 스패닝 트리 활용할 것)
    for weight, node_1, node_2 in board:
        if find(connecting, node_1) != find(connecting, node_2):
            union(connecting, node_1, node_2)

            if find(connecting, end) == start:
                return weight

    return 0


print(connected())

"""
        핵심정리
    1. 이거 최소 스패닝 트리가 아니라 최대 스패닝 트리로 풀면됨
    2. 근데 생각하는게 굉장히 어려움
    3. 로직자체는 쉽지만 생각이 어려워서 개인적으로 꽤 고전했던 문제
    4. 생각 : 최대 스패닝 트리로 구현해서, 각각의 간선을 연결하는 경우에서 만약 끝점의 부모 노드와 시작 점이 같으면 종료하고 그 때의 가중치를 출력하면 됨
             왜냐하면, 최대 무게이기 때문에 연결 시켜준 상태가 최대 무게가 되는 거임
             
"""
