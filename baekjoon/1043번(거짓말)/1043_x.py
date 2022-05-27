"""
    문제 이름 : 거짓말
    URL : https://www.acmicpc.net/problem/1043
    ----------------------------------------------
    <문제 설명>
    진실을 알고 있는 노드와 연결되어 있지 않는 파티가 몇개인지 구해라
"""
import sys
sys.setrecursionlimit(10**5)


def parent_change():
    """ 진실이 있는 사람의 부모 노드를 바꿔주는 함수 """
    standard = min(truth_cnt)

    for x in truth_cnt[1:]:
        parent[x] = standard


def find(x):
    """ 부모 노드를 찾아주는 함수 """
    if parent[x] == x: return x

    p = find(parent[x])
    parent[x] = p
    return p


def union(party_person):
    """ 합해주는 함수 """
    # 이 함수 바꾸기 -> 한번에 합칠 수 있게
    for x in range(len(party_person)):
        party_person[x] = find(party_person[x])

    if len(set(party_person)) == 1:
        return

    standard = min(party_person)
    for x in party_person:
        parent[x] = standard


person_cnt, party_cnt = map(int, input().split())
truth_cnt = list(map(int, input().split()))
parent = [x for x in range(person_cnt + 1)]

parent_change()
party = []
cnt = 0

for _ in range(party_cnt):
    temp = list(map(int, input().split()))
    party.append(temp)
    union(temp[1:])


for x in range(person_cnt + 1):
    find(x)


for x in range(len(party)):
    if len(truth_cnt) == 1:
        cnt += 1
        continue

    if parent[party[x][1]] != parent[truth_cnt[1]]:
        cnt += 1

print(cnt)
# print(parent)



# 하나씩 받으면 안됨, 이전에 만났으면 더 이상 만나면 안되는 듯