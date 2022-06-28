"""
    문제 이름 : 정복자
    URL : https://www.acmicpc.net/problem/14950
    ----------------------------------------------
    <문제 설명>
    N개의 도시와 M개의 도로가 있다. 도로는 양방향 도로이고, 각 도로는 사용하는데 필요한 비용이 존재한다
    만약에 도시를 점령하고 싶으면 그 도시와 연결된 도시를 점령하고 있어야 한다
    -> 처음에는 1번 도시만 점령하고 있으니, 1번 도시와 연결된 도시를 점령해야 하고, 그 다음에는 1번 도시와 점령하고 있는 도시 중 가장 가까운걸
    찾아서 점령하면 된다. 이러한 과정을 반복해서 스패팅 트리를 만들면 된다.
"""
city, road, increase_cost = map(int, input().split())
road_info = []
for _ in range(road):
    city_1, city_2, cost = map(int, input().split())
    # 무조건 작은 숫자가 앞으로 갈거임 -> 제일 처음 도시는 1이라서 이 과정을 해줌
    if city_1 > city_2:
        road_info.append([city_2, city_1, cost])
    else:
        road_info.append([city_1, city_2, cost])

conqueror = [x for x in range(city + 1)]


def find(node, parent) -> int:
    """ 부모노드를 찾아주는 함수 """
    if parent[node] == node: return node

    p = find(parent[node], parent)
    parent[node] = p
    return p


def union(node_1, node_2, parent) -> None:
    """ 두 노드를 연결해 주는 함수 """
    node_1 = find(node_1, parent)
    node_2 = find(node_2, parent)

    if node_1 > node_2:
        parent[node_1] = node_2
    else:
        parent[node_2] = node_1


def MST():
    """ 최소 스패닝을 해주는 함수 """
    road_info.sort(key=lambda x: x[2])
    result = 0
    cnt = 0

    for node_1, node_2, weight in road_info:
        if find(node_1, conqueror) != find(node_2, conqueror):
            union(node_1, node_2, conqueror)
            result += weight + (increase_cost * cnt)
            cnt += 1

    return result


print(MST())


"""
        핵심 정리
    1. 그냥 아주아주 평범한 MST문제
    2. 30분도 안걸림....;
"""