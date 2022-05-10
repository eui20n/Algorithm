"""
union - find 구현 해보기
"""


def getParent(parents, x):
    """ 보모 노드의 값을 얻는 함수, 경로 압축도 함 """
    if parents[x] == x: return x

    p = getParent(parents, parents[x])
    parents[x] = p
    return p


def unionParent(parents, x1, x2, cnt):
    """ 두 부모 노드를 합치는 함수 """
    a = getParent(parents, x1)
    b = getParent(parents, x2)

    if a != b:
        parents[b] = a
        cnt[a] += cnt[b]


def findParent(x, parents):
    """ 루트를 찾아 주는 함수 """
    if parents[x] == x: return x

    return findParent(parents[x], parents)
