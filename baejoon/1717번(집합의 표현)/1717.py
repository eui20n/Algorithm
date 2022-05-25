"""
    문제 이름 : 집합의 표현
    URL : https://www.acmicpc.net/problem/1717
    ----------------------------------------------
    <문제 설명>
    Union - find 연습하기

    초기의 집합이 {0}, {1}, {2}, ... , {n} 이렇게 있을때 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고함

    합집합은 0 a b 형태로 주어지고
    두 원소가 같은 집합에 있는지 확인하는 연산은 1 a b 로 주어진다
"""
import sys
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
parent = {}

for x in range(N + 1):
    parent[x] = x


def find(x):
    """ 부모노드를 찾아주는 함수 """
    if parent[x] == x: return x

    p = find(parent[x])
    parent[x] = p
    return p


def union(a, b):
    """ 두 부모 노드를 합해주는 함수 """
    a = find(a)
    b = find(b)

    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(M):
    union_find, a, b = map(int, input().split()) # 유니온 인지 파인드 인지, 원소 1, 원소 2

    if union_find == 0:
        union(a, b)

    else:
        parent_a = find(a)
        parent_b = find(b)

        if parent_a == parent_b:
            print("YES")
        else:
            print("NO")

# 시간 엄청 타이트하네