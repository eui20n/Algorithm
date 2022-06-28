"""
    문제 이름 : 친구 네트워크
    URL : https://www.acmicpc.net/problem/4195
    ----------------------------------------------
    <문제 설명>
    그냥 친구 네트워크를 구하면 되는데 입력이 이름으로 주어짐 -> 딕셔너리 활용하면 될듯
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

    if a == b:
        return

    if a > b:
        parent[a] = b
        cnt[b] += cnt[a]
        cnt[a] = cnt[b]
    else:
        parent[b] = a
        cnt[a] += cnt[b]
        cnt[b] = cnt[a]


T = int(input())
for _ in range(T):
    friend_relationship = int(input())
    parent = {}
    cnt = {}
    friend_list = set([]) # 지금 까지 들어온 친구 담아줄 리스트

    for _ in range(friend_relationship):
        friend_1, friend_2 = map(str, input().split())

        if friend_1 not in friend_list:
            parent[friend_1] = friend_1
            cnt[friend_1] = 1

        if friend_2 not in friend_list:
            parent[friend_2] = friend_2
            cnt[friend_2] = 1

        union(friend_1, friend_2)

        friend_list.add(friend_1)
        friend_list.add(friend_2)

        print(cnt[parent[friend_1]])

"""
        핵심 정리
1. 시간이 엄청 타이트 하다.
2. 딕셔너리를 활용해야 한다. 
3. 카운트를 출력할때 부모노드가 출력하게 하면 된다 -> 이거 생각 못해서 조금 걸린 문제
"""