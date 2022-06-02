"""
    문제 이름 : 복제 로봇
    URL : https://www.acmicpc.net/problem/1944
    ----------------------------------------------
    <문제 설명>
    복제 로봇이 미로로 감 -> 입구와 열쇠가 있는 곳에 로봇을 복제함
    --> 모든 열쇠를 찾으면서 로봇이 움직이는 횟수의 합을 최소로 하는 프로그램을 만들어라
    --> 만약에 열쇠를 다 먹을 수 없으면 -1 출력
"""
from collections import deque

N, cnt_key = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]


def loc_robot():
    """ 초기의 시작점을 찾아주는 함수 """
    for x in range(N):
        for y in range(N):
            if miro[x][y] == 'S':
                return x, y


def visited_init():
    """ 방문 처리 리스트를 만들어 주는 함수 """
    visited = [[False] * N for _ in range(N)]
    return visited


def search_miro(x, y):
    """ 미로를 탐색하는 함수 """
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]
            if 0 > nx or nx >= N:
                continue
            if 0 > ny or ny >= N:
                continue
            if miro[nx][ny] == 1:
                continue

            q.append([nx, ny])

# 최소 스패닝 트리로 푸는 방법이 뭘까
# 부모 노드로 방문 처리 하는게 맞을 듯
# 집합을 이용해서 유니온 파인드를 계산해야함
# 출발하는 곳에 닿으면 또 복제함
# 현재 상태를 담아줘야함
