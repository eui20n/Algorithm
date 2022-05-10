"""
    문제 이름 : 공항
    URL : https://www.acmicpc.net/problem/10775
    ----------------------------------------------
    <문제 설명>
   게이트 번호가 1부터 G까지 있고 공항에는 P개의 비행기가 순서대로 도착한다
    i번째 비행기를 1번부터 gi번재 게이트 중 하나에 영구적으로 도킹하려 한다
    비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이 후 어떤 비행기고 도착할 수 없다
    비행기를 최대 몇 대 도킹 시킬 수 있나?

    게이트 하나에 비행기는 하나만 도킹을 할 수 있음

"""

G = int(input())
P = int(input())
gate_num = []
for x in range(P):
    a = int(input())
    gate_num.append([x, a])  # 비행기 번호와 도킹을 해야할 게이트의 범위

docking_num = list(range(P))  # 이게 parent 역할을 할 것
gate = [False] * G  # 방문 처리해줄 리스트 하나 생성

def find_parents(x):
    pass

def union(x, y):
    pass

print('gate_num: ', gate_num)
print('docking_num: ', docking_num)
print('gate: ', gate)

# 도킹을 할때 숫자는 무조건 큰 쪽으로 가야함 -> 최대로 도킹할 수 있음
# 도킹이 몇번 비행기에 되었는지 확인하면됨
