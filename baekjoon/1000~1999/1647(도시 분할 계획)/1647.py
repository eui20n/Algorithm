"""
    문제 이름 : 도시 분할 계획
    URL : https://www.acmicpc.net/problem/1647
    ----------------------------------------------
    <문제 설명>
    도시가 너무 커서 도시를 2개로 분할하고 싶다
    이 때, 도시를 2개로 분할하고나서 관리하는데 드는 최소 비용을 구해라
"""
city, edge = map(int, input().split())
cities_info = []
for _ in range(edge):
    city_1, city_2, cost = map(int, input().split())
    cities_info.append([cost, city_1, city_2])

city_connect_info = [x for x in range(city + 1)]


def find(node):
    """ 부모 노드를 찾아주는 함수 """
    if city_connect_info[node] == node: return node

    p = find(city_connect_info[node])
    city_connect_info[node] = p
    return p


def union(node_1, node_2):
    """ 두 노드를 합쳐주는 함수 """
    node_1 = find(node_1)
    node_2 = find(node_2)

    if node_1 > node_2:
        city_connect_info[node_1] = node_2
    else:
        city_connect_info[node_2] = node_1


def MST():
    """ 최소 스패닝 트리를 해주는 함수"""
    cities_info.sort()

    result = 0

    for cost, node_1, node_2 in cities_info:
        if find(node_1) != find(node_2):
            union(node_1, node_2)
            result += cost
            final_cost = cost

    return result - final_cost


print(MST())
# print(city_connect_info)


"""
        소요 시간
    10분 정도
    
        핵심 정리
    1. 그냥 MST를 하고 나서 끝나면 마지막에 꺼만 없애주면 됨 -> 그럼 자연스럽게 2개로 분리가 됨
"""