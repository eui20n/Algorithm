"""
    문제 이름 : 도시 건설
    URL : https://www.acmicpc.net/problem/21924
    ----------------------------------------------
    <문제 설명>
    모든 도시를 잇는데 드는 도로의 비용을 최소로 하고 싶을 때, 최소 비용을 구해라
"""


def find(node):
    """ 부모 노드를 찾아주는 함수 """
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


def mst():
    """ 최소 스패닝 함수 """
    road_info.sort()

    result = 0
    sum_num = 0

    for cost, x, y in road_info:
        if find(x) != find(y):
            union(x, y)
            result += cost
        sum_num += cost

    for x in range(1, city + 1):
        find(x)

    if len(set(parent)) != 2:
        return -1
    return sum_num - result


if __name__ == "__main__":
    city, road = map(int, input().split())
    road_info = []
    for _ in range(road):
        city_1, city_2, cost = map(int, input().split())
        road_info.append([cost, city_1, city_2])

    parent = [x for x in range(city + 1)]

    print(mst())
