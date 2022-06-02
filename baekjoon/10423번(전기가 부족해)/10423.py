"""
    문제 이름 : 전기가 부족해
    URL : https://www.acmicpc.net/problem/10423
    ----------------------------------------------
    <문제 설명>
    N개의 도시가 있고, M개의 두 도시를 연결하는 케이블 정보와 K개의 발전소가 설치된 도시가 주어지면 케이블 설비 비용을 최소화 하여
    모든 도시에 전기를 공급해야 한다
    케이블은 무조건 하나의 도시만 연결되어 있다

    -> 모든 도시가 연결이 되어 있을 필요 없음
    -> 기준은 발전소인듯
    -> 발전소를 기준으로 문제를 풀어 나가면 될듯
"""

N, M, K = map(int, input().split())
power_plant = set(map(int, input().split()))
city_info = []
for _ in range(M):
    node_1, node_2, weight = map(int, input().split())
    if node_1 in power_plant or node_2 in power_plant:
        city_info.append([weight, node_1, node_2, 'O'])
    else:
        city_info.append([weight, node_1, node_2, 'X'])

head_city = [x for x in range(N + 1)]


def find(x):
    """ 부모 노드를 찾아주는 함수 """
    if head_city[x] == x: return x

    p = find(head_city[x])
    head_city[x] = p
    return p


def union(a, b):
    """ 두 도시를 합해주는 함수 """
    a = find(a)
    b = find(b)

    if a == b:
        return

    if a in power_plant and b in power_plant:
        if a > b:
            head_city[a] = b

        else:
            head_city[b] = a

        return

    if a in power_plant:
        head_city[b] = a
        return

    if b in power_plant:
        head_city[a] = b
        return

    if a > b:
        head_city[a] = b

    else:
        head_city[b] = a


def connect_city():
    """ 도시를 연결해줄 함수 """
    city_info.sort()
    result = 0

    for cost, city_1, city_2, check_plant in city_info:
        head_city_1, head_city_2 = find(city_1), find(city_2)
        if check_plant == 'X' and head_city_1 != head_city_2:
            if head_city_1 in power_plant and head_city_2 in power_plant:
                continue

            union(city_1, city_2)
            result += cost

        if check_plant == 'O' and head_city_1 != head_city_2:
            if head_city_1 in power_plant and head_city_2 in power_plant:
                continue

            union(city_1, city_2)
            result += cost

    return result


print(connect_city())


"""
        핵심정리
    1. 모두 다 연결하는게 아님
    2. 그렇다면 연결하지 않는 경우를 확실히 알아야함
    3. 위 2개만 주의하면서 풀면 쉽게 해결 가능한 문제

"""