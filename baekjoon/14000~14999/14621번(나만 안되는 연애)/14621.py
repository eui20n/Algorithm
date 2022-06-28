"""
    문제 이름 : 나만 안되는 연애
    URL : https://www.acmicpc.net/problem/14621
    ----------------------------------------------
    <문제 설명>
    1. 사심 경로는 사용자들의 사심을 만족시키기 위해 남초 대학교와 여초 대학교들을 연결하는 도로로만 이루어져 있다
    2. 사용자들이 다양한 사람과 미팅할 수 있도록 어떤 대학교에서든 모든 대학교로 이동이 가능한 경로이다
    3. 시간을 낭비하지 않고 미팅할 수 있도록 이 경로의 길이는 최단 거리가 되어야 한다

    -> 남대와 여대만 이을 수 있다, 모든 노드는 연결되어 있어야 하면 최소 길이여야 한다
    -> 만약에 연결을 할 수 없으면 -1을 출력하면 된다
"""

N, M = map(int, input().split())
school_gender_info = list(map(str, input().split()))
school_connect_info = [list(map(int, input().split())) for _ in range(M)]
parent_school = [x for x in range(N + 1)]


def find(x):
    """ 합해주는 함수 """
    if parent_school[x] == x: return x

    p = find(parent_school[x])
    parent_school[x] = p
    return p


def union(a, b):
    """ 합해주는 함수 """
    a = find(a)
    b = find(b)

    if a > b:
        parent_school[a] = b
    else:
        parent_school[b] = a


def MST():
    """ 최소 신장트리로 연결해주는 함수 """
    school_connect_info.sort(key=lambda x: x[2])
    result = 0

    for x, y, dist in school_connect_info:
        if school_gender_info[x - 1] == school_gender_info[y - 1]:
            continue

        if find(x) == find(y):
            continue

        union(x, y)
        result += dist

    for x in range(1, N + 1):
        find(x)

    if len(set(parent_school)) == 2:
        return result

    return -1


print(MST())


