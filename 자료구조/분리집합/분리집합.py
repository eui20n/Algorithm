"""
union - find 구현 해보기
"""


def getParent(parents, x): # 사실 이게 찾아주는 역할을 해줌
    """
    보모 노드의 값을 얻는 함수, 경로 압축도 함
    parent : 리스트
    x : 정수
    """
    if parents[x] == x: return x

    p = getParent(parents, parents[x])
    parents[x] = p
    return p


def unionParent(parents, x1, x2, cnt):
    """
    두 부모 노드를 합치는 함수
    parents : 리스트
    x1 : 정수
    x2 : 정수
    ==> 부모 노드를 합침으로써 같은 그룹의 노드가 됨
    """
    a = getParent(parents, x1)
    b = getParent(parents, x2)

    if a != b:
        parents[b] = a
        cnt[a] += cnt[b]


def findParent(x, parents):
    """ 루트를 찾아 주는 함수 """
    if parents[x] == x: return x

    return findParent(parents[x], parents)