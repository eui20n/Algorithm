"""
    문제 이름 : 버스 갈아타기
    URL : https://www.acmicpc.net/problem/2536
    ----------------------------------------------
    <문제 설명>
    버스는 수평선 또는 수직선을 왕복한다
    이 때, 출발지점에서 도착지점 까지 가고 싶을 때, 갈아타는 버스의 최소값은 무엇인가
"""
from collections import deque

R, C = map(int, input().split())
bus_cnt = int(input())
bus_road = [[] for _ in range(bus_cnt + 1)]
for _ in range(bus_cnt):
    bus_num, x_1, y_1, x_2, y_2 = map(int, input().split())
    bus_road[bus_num].append([x_1 - 1, y_1 - 1])
    bus_road[bus_num].append([x_2 - 1, y_2 - 1])
x_1, y_1, x_2, y_2 = map(int, input().split())
start = [x_1 - 1, y_1 - 1]
arrive = [x_2 - 1, y_2 - 1]


def visited_init():
    """ 방문처리 리스트를 만들어 주는 함수 """
    visited = [False] * (bus_cnt + 1)
    return visited


print(*bus_road, sep='\n')


# 최소 시간을 구하는게 아니라, 버스를 최소로 갈아타는게 몇번인지 구하는 것

# 생각해본 방법
# 1. 해당 위치에서 탈 수 있는 버스가 무엇이 있는가 => 해당 자리로 방문처리를 해야함 -> O(100000^2)이 될거 같음
# 2. 방향 벡터를 설정하지 않음, 해당 위치의 버스의 크기만큼 갈 것 -> O(100000^2)보다는 작을 것 같음음
# 3. 버스로 보고, 5000번을 계산해야함 -> 이게 맞는 듯

