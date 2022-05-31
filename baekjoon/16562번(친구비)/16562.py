"""
    문제 이름 : 친구비
    URL : https://www.acmicpc.net/problem/16562
    ----------------------------------------------
    <문제 설명>
    "친구의 친구는 친구다"를 이용한다고 할때 가장 적은 비용으로 모든 사람과 친구가 되는 방법을 구해라
"""
import sys
sys.setrecursionlimit(10**5)


def find(x):
    """ 찾아주는 함수 """
    if friend[x] == x: return x

    p = find(friend[x])
    friend[x] = p
    return p


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if friend_bill[a] > friend_bill[b]:
        friend[a] = b
    else:
        friend[b] = a


def check_friend():
    """ 모두 친구가 될수 있는지 없는지 확인해주는 함수 """
    temp = set(friend)
    bill = 0
    for x in temp:
        bill += friend_bill[x]

    if bill > k:
        return 'Oh no'
    return bill


N, M, k = map(int, input().split())
friend_bill = [0] + list(map(int, input().split()))
friend = [x for x in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    union(x, y)

for x in range(len(friend)):
    find(x)

print(check_friend())

# 소문자 대문자 잘보자!