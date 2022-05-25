"""
    문제 이름 : 여행 가자
    URL : https://www.acmicpc.net/problem/1976
    ----------------------------------------------
    <문제 설명>
    서로 다른 지역을 갈 수 있는지 구하면 된다
"""
import sys
sys.setrecursionlimit(10**5)


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

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def go_travel():
    """ 여행을 갈 수 있는지 없는지 확인해 주는 함수 """

    idx = 0
    while True:
        if idx > len(travel_city) - 1:
            break
        if parent[travel_city[idx]] == parent[travel_city[0]]:
            idx += 1
        else:
            return 'NO'
    return 'YES'


N = int(input())
M = int(input())
parent = [x for x in range(N + 1)]

for x in range(1, N + 1):
    city = list(map(int, input().split()))

    for y in range(len(city)):
        if city[y] == 1:
            union(x, y + 1)

travel_city = list(map(int, input().split()))

print(go_travel())


"""
    문제 정리
1. 유니온 파인드에 대해서 조금은 감이 온다 -> 이건 정리가 아니다.
2. union할때 기준 정해주기 -> 나는 그냥 다르면 union했는데, 이게 아니라 '더 작은 원소가 부모 노드가 되게 하기'와 같은 기준 잡기 => 이것땜에 틀렸네;
"""