"""
    문제 이름 : 수영장 만들기
    URL : https://www.acmicpc.net/problem/1113
    ----------------------------------------------
    <문제 설명>
    그래프가 주어질때 물이 고일 수 있는지, 그리고 고인다면 얼마나 고이는지 출력하면 된다.
    1 <= 물의 높이 <= 9 이다
    무조건 물이 고일 수 있다고 생각할 것 -> 물이 고일 수 없을시 출력값이 없음
"""
from collections import deque

R, C = map(int, input().split())
graph = [list(map(int, input())) for _ in range(R)]


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[False] * C for _ in range(R)]
    return visited


def temp_init(layer):
    """ 임시 리스트를 만들어 주는 함수 """
    # 만약에 이거 없이 방문처리 리스트로 처리 가능하면 이거 뺄 것
    temp = [[layer] * C for _ in range(R)]
    return temp

def cnt_water(layer):
    """ 각층 마다 물이 얼마나 고이는지 확인하는 함수 """
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    # 시작은 무조건 0,0에서 할 예정
    visited = visited_init()
    visited[0][0] = True

    temp = temp_init(layer)

    q = deque()
    q.append([0, 0])

    cnt = 0

    while q:
        x, y = q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if cnt_water_con(nx, ny, visited, layer):
                pass


def cnt_water_con(x, y, visited, layer):
    """ cnt_water 조건 함수 """
    if 0 > x or x >= R:
        return False
    if 0 > y or y >= C:
        return False
    if visited[x][y]:
        return False
    if graph[x][y] > layer: # 만약에 뭔가 이상하고 애매하면 이거 먼저 의심하기
        return False
    return True



# 먼저 물이 가장 높은 높이 까지 있다고 가정을 한고, 그 높이에서 흘러넘치는 물이 있는지 체크하고, 남은 물이 있으면 count한다 -> 이 방식을 1층까지 해서 총 남은 물의 양을 더한다
# 아니면 1층 부터 높이 쌓아가는 방식도 있음 -> 우선 이 방식으로 하기

# 물이 고일 수 있는 조건
# 1. 가장 자리이면 안된다.
# 2. 둘러 쌓여 있어야 한다.

# 가장 자리로 못가면 절대로 잠길 수 없음