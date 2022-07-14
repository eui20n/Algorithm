"""
    문제 이름 : 공항
    URL : https://www.acmicpc.net/problem/10775
    ----------------------------------------------
    <문제 설명>
    게이트 번호가 1부터 G까지 있고 공항에는 P개의 비행기가 순서대로 도착한다
    i번째 비행기를 1번부터 gi번재 게이트 중 하나에 영구적으로 도킹하려 한다
    비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이 후 어떤 비행기고 도착할 수 없다
    비행기를 최대 몇 대 도킹 시킬 수 있나?

    게이트 하나에 비행기는 하나만 도킹을 할 수 있음

"""
G = int(input())
P = int(input())
plane_info = []
for _ in range(P):
    plane_info.append(int(input()))

gate_parent = [x for x in range(G + 1)]


def find(node):
    """ 부모 노드를 찾아주는 함수 """
    if gate_parent[node] == node: return node

    p = find(gate_parent[node])
    gate_parent[node] = p
    return p


def union(node_1, node_2):
    """ 두 노드를 합해주는 함수 """
    node_1 = find(node_1)
    node_2 = find(node_2)

    if node_1 > node_2:
        gate_parent[node_1] = node_2

    else:
        gate_parent[node_2] = node_1


def docking():
    """ 도킹을 최대 몇개 할 수 있는지 구해주는 함수 """
    max_docking_num = 0

    for node in plane_info:
        find_node = find(node)

        if find_node == 0:
            return max_docking_num

        max_docking_num += 1
        union(node, find_node - 1)

    return max_docking_num


print(docking())


"""
        핵심 로직
    1. 무조건 자기 번호가 있는 위치로 가야함
    1-1. 2번이면 2번으로 가야함
    2. 1번을 한 후, 그 게이트의 부모 노드와 그 부노 노드 - 1 노드를 union해줌 => 다음에 그 게이트로 가게 되면 그 부모 노드 - 1로 가게함
    3. 2번을 반복하면 0번 노드로 가는 경우가 생기는데, 이 경우는 끝을 의미함
"""