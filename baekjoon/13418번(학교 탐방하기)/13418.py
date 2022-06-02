"""
    문제 이름 : 학교 탐방하기
    URL : https://www.acmicpc.net/problem/13418
    ----------------------------------------------
    <문제 설명>
    오르막길, 내리막길 = 점선, 실선
    건물 입구 0
    오르막길을 k번 오르면 피로도가 k^2이 된다
    입구는 항상 1번 건물과 이어져 있다

    구해야 하는건 최악의 경로의 피로도와 최고의 경로 피로도의 차이이다
"""
N, M = map(int, input().split())
road = []
for _ in range(M + 1):
    build_1, build_2, info_road = map(int, input().split())
    road.append([info_road, build_1, build_2])


def find(parent, x):
    """ 부모 노드를 찾아주는 함수 """
    if parent[x] == x: return x

    p = find(parent, parent[x])
    parent[x] = p
    return p


def union(parent, a, b):
    """ 두 노드를 합해주는 함수 """
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[a] = b

    else:
        parent[b] = a


def MST(check):
    """ MST를 구현해주는 함수 """
    info_connect_build = [x for x in range(N + 1)]
    uphill = 0

    if check == "worst":
        road.sort()

    if check == "best":
        road.sort(reverse=True)

    for info, build_1, build_2 in road:
        if find(info_connect_build, build_1) != find(info_connect_build, build_2):
            union(info_connect_build, build_1, build_2)
            if info == 0:
                uphill += 1

    return uphill**2


def main():
    """ 함수를 실행 시켜줄 함수 """
    return MST("worst") - MST("best")


print(main())


"""
        핵심정리
    1. 그냥 MST 함수 2번하면 됨
"""